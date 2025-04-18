# examples/integration_example.py

from integration.qiskit_integration import QiskitIntegration
from integration.cirq_integration import CirqIntegration

def main():
    # Qiskit integration example
    print("Qiskit Integration Example:")
    qiskit_backend = QiskitIntegration()
    qiskit_circuit = qiskit_backend.create_circuit(2)
    qiskit_counts = qiskit_backend.run_circuit(qiskit_circuit)
    print("Qiskit Measurement Results:")
    print(qiskit_counts)

    # Cirq integration example
    print("\nCirq Integration Example:")
    cirq_backend = CirqIntegration()
    cirq_circuit = cirq_backend.create_circuit(2)
    cirq_result = cirq_backend.run_circuit(cirq_circuit)
    print("Cirq Measurement Results:")
    print(cirq_result)

if __name__ == "__main__":
    main()
