# main.py

import argparse
import json
import logging
from utils.logger import setup_logger
from utils.config import ConfigManager
from integration.qiskit_integration import QiskitIntegration
from integration.cirq_integration import CirqIntegration
from quantum_circuit.circuit import QuantumCircuit

def main():
    # Set up logging
    logger = setup_logger("QuantumNetCore")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="QuantumNet-Core: A Quantum Computing Framework")
    parser.add_argument('--config', type=str, help='Path to the configuration file', default='config.json')
    parser.add_argument('--backend', type=str, choices=['qiskit', 'cirq'], help='Select the backend for quantum execution', required=True)
    parser.add_argument('--num_qubits', type=int, help='Number of qubits in the quantum circuit', required=True)
    args = parser.parse_args()

    # Load configuration
    try:
        config = ConfigManager(args.config)
        logger.info("Configuration loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        return

    # Initialize the selected backend
    if args.backend == 'qiskit':
        quantum_backend = QiskitIntegration()
        logger.info("Using Qiskit as the backend.")
    elif args.backend == 'cirq':
        quantum_backend = CirqIntegration()
        logger.info("Using Cirq as the backend.")

    # Create a quantum circuit
    circuit = QuantumCircuit(args.num_qubits)
    logger.info(f"Creating a quantum circuit with {args.num_qubits} qubits.")

    # Add gates to the circuit (example: Hadamard gates)
    for i in range(args.num_qubits):
        gate = quantum_backend.create_circuit(args.num_qubits)
        circuit.add_gate(gate, [i])
        logger.info(f"Added Hadamard gate to qubit {i}.")

    # Run the circuit
    try:
        counts = quantum_backend.run_circuit(circuit)
        logger.info("Circuit executed successfully.")
    except Exception as e:
        logger.error(f"Failed to execute circuit: {e}")
        return

    # Visualize results
    logger.info("Measurement results:")
    print(json.dumps(counts, indent=4))

    # Optionally visualize the circuit (if using Qiskit)
    if args.backend == 'qiskit':
        quantum_backend.visualize_results(counts)

if __name__ == "__main__":
    main()
