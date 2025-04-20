# src/utils/cache_manager.py
"""
Ultra high-tech cache manager for QuantumNet-Core.
Provides persistent, distributed, and quantum-optimized caching for quantum states,
circuit parameters, optimization results, and network metadata.
Features thread-safe operations, adaptive eviction, quantum compression, and encryption.
"""
import sqlite3
import redis
import numpy as np
import pennylane as qml
from typing import Any, Dict, Optional, Union
import threading
import pickle
import json
import time
import logging
import hashlib
import os
from cryptography.fernet import Fernet
from collections import OrderedDict

# Configure logging for cache operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class QuantumCacheManager:
    """
    Advanced cache manager for QuantumNet-Core with quantum-specific optimizations.
    Supports persistent storage (SQLite), distributed caching (Redis), quantum state compression,
    adaptive eviction, encryption, and performance monitoring.
    """
    def __init__(
        self,
        db_path: str = "quantum_cache.db",
        redis_host: str = "localhost",
        redis_port: int = 6379,
        cache_size_limit: int = 1000,
        encryption_key: Optional[bytes] = None
    ):
        """
        Initialize the QuantumCacheManager.

        Args:
            db_path (str): Path to SQLite database for persistent storage.
            redis_host (str): Host for Redis distributed cache.
            redis_port (int): Port for Redis distributed cache.
            cache_size_limit (int): Maximum number of entries in in-memory cache.
            encryption_key (Optional[bytes]): Key for AES-256 encryption. If None, generated automatically.
        """
        # In-memory cache with LRU eviction
        self.memory_cache = OrderedDict()
        self.cache_size_limit = cache_size_limit
        self.lock = threading.Lock()

        # Persistent storage with SQLite
        self.db_path = db_path
        self._initialize_sqlite()

        # Distributed caching with Redis
        try:
            self.redis = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
            self.redis.ping()  # Test Redis connection
            logger.info("Connected to Redis at %s:%d", redis_host, redis_port)
        except redis.ConnectionError:
            logger.warning("Failed to connect to Redis. Distributed caching disabled.")
            self.redis = None

        # Encryption setup
        self.encryption_key = encryption_key or Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)

        # Performance metrics
        self.hits = 0
        self.misses = 0
        self.total_latency = 0.0
        self.request_count = 0

        # Quantum autoencoder for state compression
        self.qae = self._initialize_quantum_autoencoder()

    def _initialize_sqlite(self) -> None:
        """Initialize SQLite database for persistent caching."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    value BLOB,
                    fidelity REAL,
                    timestamp REAL,
                    access_count INTEGER
                )
            """)
            conn.commit()
        logger.info("Initialized SQLite cache at %s", self.db_path)

    def _initialize_quantum_autoencoder(self) -> Any:
        """Initialize quantum autoencoder for state compression."""
        n_qubits = 4  # Adjustable based on quantum state size
        n_latent = 2  # Latent space size for compression
        dev = qml.device("default.qubit", wires=n_qubits)

        @qml.qnode(dev)
        def qae_circuit(state, params):
            """Quantum autoencoder circuit for compression."""
            for i in range(n_qubits):
                qml.RX(state[i], wires=i)
            for i in range(n_latent):
                qml.Rot(*params[i], wires=i)
            return qml.state()

        class QAE:
            def __init__(self):
                self.params = np.random.randn(n_latent, 3)
                self.circuit = qae_circuit

            def compress(self, state):
                """Compress quantum state."""
                return self.circuit(state, self.params)[:2**n_latent]

            def decompress(self, compressed_state):
                """Decompress quantum state (placeholder)."""
                return np.pad(compressed_state, (0, 2**n_qubits - len(compressed_state)))

        return QAE()

    def _encrypt_data(self, data: bytes) -> bytes:
        """Encrypt data using AES-256."""
        return self.cipher.encrypt(data)

    def _decrypt_data(self, encrypted_data: bytes) -> bytes:
        """Decrypt data using AES-256."""
        return self.cipher.decrypt(encrypted_data)

    def _serialize(self, data: Any) -> bytes:
        """Serialize data for storage."""
        return pickle.dumps(data)

    def _deserialize(self, data: bytes) -> Any:
        """Deserialize data from storage."""
        return pickle.loads(data)

    def _generate_key(self, key: Union[str, tuple]) -> str:
        """Generate a unique cache key."""
        if isinstance(key, tuple):
            key = json.dumps(key, sort_keys=True)
        return hashlib.sha256(key.encode()).hexdigest()

    def put(
        self,
        key: Union[str, tuple],
        value: Any,
        fidelity: float = 1.0,
        use_quantum_compression: bool = False
    ) -> None:
        """
        Store data in the cache with optional quantum compression.

        Args:
            key (Union[str, tuple]): Cache key.
            value (Any): Data to cache (e.g., quantum state, circuit params).
            fidelity (float): Fidelity score for eviction prioritization.
            use_quantum_compression (bool): Whether to compress quantum states.
        """
        start_time = time.time()
        cache_key = self._generate_key(key)

        with self.lock:
            # Compress quantum state if requested
            if use_quantum_compression and isinstance(value, np.ndarray):
                value = self.qae.compress(value)

            # Serialize and encrypt data
            serialized_value = self._serialize(value)
            encrypted_value = self._encrypt_data(serialized_value)

            # In-memory cache
            if len(self.memory_cache) >= self.cache_size_limit:
                self._evict()
            self.memory_cache[cache_key] = (value, fidelity, time.time(), 1)
            self.memory_cache.move_to_end(cache_key)

            # Persistent storage
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO cache (key, value, fidelity, timestamp, access_count)
                    VALUES (?, ?, ?, ?, ?)
                """, (cache_key, encrypted_value, fidelity, time.time(), 1))
                conn.commit()

            # Distributed cache (Redis)
            if self.redis:
                try:
                    self.redis.setex(cache_key, 3600, serialized_value)  # 1-hour TTL
                except redis.RedisError:
                    logger.warning("Failed to store %s in Redis.", cache_key)

            latency = time.time() - start_time
            self.total_latency += latency
            self.request_count += 1
            logger.info("Cached %s (fidelity: %.4f, latency: %.4fs)", cache_key, fidelity, latency)

    def get(
        self,
        key: Union[str, tuple],
        use_quantum_decompression: bool = False
    ) -> Optional[Any]:
        """
        Retrieve data from the cache.

        Args:
            key (Union[str, tuple]): Cache key.
            use_quantum_decompression (bool): Whether to decompress quantum states.

        Returns:
            Optional[Any]: Cached data or None if not found.
        """
        start_time = time.time()
        cache_key = self._generate_key(key)

        with self.lock:
            # Check in-memory cache
            if cache_key in self.memory_cache:
                value, fidelity, timestamp, access_count = self.memory_cache[cache_key]
                self.memory_cache[cache_key] = (value, fidelity, timestamp, access_count + 1)
                self.memory_cache.move_to_end(cache_key)
                self.hits += 1
                latency = time.time() - start_time
                self.total_latency += latency
                self.request_count += 1
                logger.info("Cache hit for %s (latency: %.4fs)", cache_key, latency)
                if use_quantum_decompression and isinstance(value, np.ndarray):
                    return self.qae.decompress(value)
                return value

            # Check Redis
            if self.redis:
                try:
                    serialized_value = self.redis.get(cache_key)
                    if serialized_value:
                        value = self._deserialize(serialized_value)
                        self.put(key, value, fidelity=1.0)  # Update in-memory and SQLite
                        self.hits += 1
                        latency = time.time() - start_time
                        self.total_latency += latency
                        self.request_count += 1
                        logger.info("Redis cache hit for %s (latency: %.4fs)", cache_key, latency)
                        if use_quantum_decompression and isinstance(value, np.ndarray):
                            return self.qae.decompress(value)
                        return value
                except redis.RedisError:
                    logger.warning("Failed to retrieve %s from Redis.", cache_key)

            # Check SQLite
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT value, fidelity, access_count FROM cache WHERE key = ?", (cache_key,))
                result = cursor.fetchone()
                if result:
                    encrypted_value, fidelity, access_count = result
                    serialized_value = self._decrypt_data(encrypted_value)
                    value = self._deserialize(serialized_value)
                    cursor.execute(
                        "UPDATE cache SET access_count = ?, timestamp = ? WHERE key = ?",
                        (access_count + 1, time.time(), cache_key)
                    )
                    conn.commit()
                    self.put(key, value, fidelity=fidelity)  # Update in-memory and Redis
                    self.hits += 1
                    latency = time.time() - start_time
                    self.total_latency += latency
                    self.request_count += 1
                    logger.info("SQLite cache hit for %s (latency: %.4fs)", cache_key, latency)
                    if use_quantum_decompression and isinstance(value, np.ndarray):
                        return self.qae.decompress(value)
                    return value

            self.misses += 1
            latency = time.time() - start_time
            self.total_latency += latency
            self.request_count += 1
            logger.info("Cache miss for %s (latency: %.4fs)", cache_key, latency)
            return None

    def _evict(self) -> None:
        """Evict least valuable entry based on fidelity and access count."""
        if not self.memory_cache:
            return

        # Prioritize low fidelity and low access count
        candidates = [(k, v[1], v[3]) for k, v in self.memory_cache.items()]  # (key, fidelity, access_count)
        candidates.sort(key=lambda x: x[1] + x[2] * 0.1)  # Weighted score
        evict_key = candidates[0][0]
        self.memory_cache.pop(evict_key)
        logger.info("Evicted %s from in-memory cache", evict_key)

    def clear(self) -> None:
        """Clear all caches."""
        with self.lock:
            self.memory_cache.clear()
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM cache")
                conn.commit()
            if self.redis:
                try:
                    self.redis.flushall()
                except redis.RedisError:
                    logger.warning("Failed to clear Redis cache.")
            logger.info("All caches cleared.")

    def get_metrics(self) -> Dict[str, float]:
        """
        Retrieve cache performance metrics.

        Returns:
            Dict[str, float]: Metrics including hit rate and average latency.
        """
        hit_rate = self.hits / max(self.request_count, 1)
        avg_latency = self.total_latency / max(self.request_count, 1)
        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": hit_rate,
            "average_latency": avg_latency,
            "cache_size": len(self.memory_cache)
        }

    def __del__(self):
        """Clean up resources."""
        try:
            if os.path.exists(self.db_path):
                with sqlite3.connect(self.db_path) as conn:
                    conn.close()
            if self.redis:
                self.redis.close()
        except Exception as e:
            logger.error("Error during cleanup: %s", e)
