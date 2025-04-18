# benchmarks/benchmark_entanglement.py

import time
import numpy as np
from quantum_circuit.entanglement import create_entangled_state

def benchmark_entanglement_creation(num_trials=1000):
    """Benchmark the creation of entangled states."""
    start_time = time.time()
    
    for _ in range(num_trials):
        create_entangled_state()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to create {num_trials} entangled states: {elapsed_time:.6f} seconds")
    print(f"Average time per entangled state: {elapsed_time / num_trials:.6f} seconds")

if __name__ == "__main__":
    benchmark_entanglement_creation()
