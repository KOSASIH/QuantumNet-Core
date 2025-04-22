# benchmark_qnn.py

import pennylane as qml
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import time

# Define a quantum neural network circuit
def quantum_neural_network(weights, x):
    qml.RY(x[0], wires=0)
    qml.RY(x[1], wires=1)
    qml.RZ(weights[0], wires=0)
    qml.RZ(weights[1], wires=1)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

# Benchmarking function for QNN
def benchmark_qnn(num_samples=100, num_features=2, num_qubits=2, num_trials=10):
    # Generate synthetic dataset
    X, y = make_classification(n_samples=num_samples, n_features=num_features, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Initialize weights for the quantum neural network
    weights = np.random.uniform(low=-np.pi, high=np.pi, size=num_qubits)

    # Create a quantum device
    dev = qml.device('default.qubit', wires=num_qubits)

    # Create a QNode
    @qml.qnode(dev)
    def qnode(x):
        return quantum_neural_network(weights, x)

    # Benchmarking
    accuracies = []
    execution_times = []

    for _ in range(num_trials):
        start_time = time.time()
        predictions = []

        for x in X_test:
            prediction = qnode(x)
            predictions.append(1 if prediction > 0 else 0)

        end_time = time.time()
        execution_times.append(end_time - start_time)

        accuracy = accuracy_score(y_test, predictions)
        accuracies.append(accuracy)

    avg_accuracy = np.mean(accuracies)
    avg_execution_time = np.mean(execution_times)

    return avg_accuracy, avg_execution_time

if __name__ == '__main__':
    # Run the benchmark
    avg_accuracy, avg_execution_time = benchmark_qnn(num_samples=1000, num_features=2, num_qubits=2, num_trials=10)
    print(f"Average Accuracy: {avg_accuracy:.4f}")
    print(f"Average Execution Time: {avg_execution_time:.4f} seconds")
