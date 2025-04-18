# benchmarks/benchmark_quantum_circuit.py

import time
import numpy as np
from quantum_circuit.circuit import QuantumCircuit
from quantum_circuit.gate_operations import apply_circuit

def benchmark_quantum_circuit_operations(num_qubits=2, num_trials=1000):
    """Benchmark the creation and execution of quantum circuits."""
    circuit = QuantumCircuit(num_qubits)
    x_gate = np.array([[0, 1], [1, 0]])  # X gate
    h_gate = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard gate

    # Add gates to the circuit
    circuit.add_gate(x_gate, [0])
    circuit.add_gate(h_gate, [1])

    initial_state = np.array([1, 0, 0, 0])  # |00⟩ state

    start_time = time.time()
    
    for _ in range(num_trials):
        apply_circuit(initial_state, circuit)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to apply the circuit {num_trials} times: {elapsed_time:.6f} seconds")
    print(f"Average time per circuit application: {elapsed_time / num_trials:.6f} seconds")

if __name__ == "__main__":
    benchmark_quantum_circuit_operations()
