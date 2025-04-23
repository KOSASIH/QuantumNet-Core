# qml_example.py

import numpy as np
from qiskit import Aer, QuantumCircuit, transpile, assemble, execute
from qiskit.circuit import Parameter
from qiskit.utils import QuantumInstance
from qiskit_machine_learning.algorithms import QSVC
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Function to create a quantum circuit for QSVM
def create_qsvm_circuit(num_qubits):
    # Define parameters for the circuit
    theta = Parameter('θ')
    circuit = QuantumCircuit(num_qubits)

    # Apply Hadamard gates to create superposition
    for qubit in range(num_qubits):
        circuit.h(qubit)

    # Apply rotation gates
    for qubit in range(num_qubits):
        circuit.ry(theta, qubit)

    # Measure the qubits
    circuit.measure_all()
    return circuit

# Function to visualize the decision boundary
def plot_decision_boundary(model, X, y):
    # Create a grid of points
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    
    # Predict the class for each point in the grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the decision boundary
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
    plt.title("QSVM Decision Boundary")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

# Main function to execute the QML example
def main():
    # Generate synthetic data
    X, y = make_moons(n_samples=100, noise=0.1, random_state=42)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a quantum instance
    backend = Aer.get_backend('qasm_simulator')
    quantum_instance = QuantumInstance(backend, shots=1024)

    # Create a QSVM model
    num_qubits = 2  # Number of qubits for the QSVM
    circuit = create_qsvm_circuit(num_qubits)
    qsvm = QSVC(quantum_instance=quantum_instance, quantum_circuit=circuit)

    # Train the QSVM model
    qsvm.fit(X_train, y_train)

    # Make predictions
    y_pred = qsvm.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of QSVM: {accuracy:.2f}")

    # Visualize the decision boundary
    plot_decision_boundary(qsvm, X, y)

if __name__ == "__main__":
    main()
