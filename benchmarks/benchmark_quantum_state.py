# benchmarks/benchmark_quantum_state.py

import time
import numpy as np
from quantum_circuit.gate_operations import apply_gate

def benchmark_quantum_state_manipulation(num_trials=1000):
    """Benchmark the application of gates to quantum states."""
    state = np.array([1, 0])  # |0⟩ state
    x_gate = np.array([[0, 1], [1, 0]])  # X gate

    start_time = time.time()
    
    for _ in range(num_trials):
        apply_gate(state, x_gate, 0)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to apply X gate to state {num_trials} times: {elapsed_time:.6f} seconds")
    print(f"Average time per gate application: {elapsed_time / num_trials:.6f} seconds")

if __name__ == "__main__":
    benchmark_quantum_state_manipulation()
