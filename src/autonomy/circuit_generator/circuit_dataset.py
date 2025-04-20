"""
Circuit Dataset Manager for Quantum Circuits
"""
import numpy as np
import json
import os
from qiskit import QuantumCircuit

class CircuitDataset:
    def __init__(self, dataset_path=None):
        """
        Initialize the Circuit Dataset Manager.

        Parameters:
        dataset_path (str): Optional path to load an existing dataset.
        """
        self.dataset = []
        if dataset_path:
            self.load_dataset(dataset_path)

    def load_dataset(self, dataset_path):
        """
        Load a dataset of quantum circuits from a JSON file.

        Parameters:
        dataset_path (str): Path to the JSON file containing the dataset.
        """
        with open(dataset_path, 'r') as file:
            self.dataset = json.load(file)
        print(f"Loaded dataset with {len(self.dataset)} circuits from {dataset_path}.")

    def save_dataset(self, dataset_path):
        """
        Save the current dataset of quantum circuits to a JSON file.

        Parameters:
        dataset_path (str): Path to save the dataset.
        """
        with open(dataset_path, 'w') as file:
            json.dump(self.dataset, file)
        print(f"Saved dataset with {len(self.dataset)} circuits to {dataset_path}.")

    def add_circuit(self, circuit: QuantumCircuit):
        """
        Add a quantum circuit to the dataset.

        Parameters:
        circuit (QuantumCircuit): The quantum circuit to add.
        """
        circuit_dict = self.circuit_to_dict(circuit)
        self.dataset.append(circuit_dict)
        print(f"Added circuit to dataset. Total circuits: {len(self.dataset)}.")

    def circuit_to_dict(self, circuit: QuantumCircuit):
        """
        Convert a QuantumCircuit to a dictionary representation.

        Parameters:
        circuit (QuantumCircuit): The quantum circuit to convert.

        Returns:
        dict: Dictionary representation of the circuit.
        """
        return {
            'num_qubits': circuit.num_qubits,
            'depth': circuit.depth(),
            'size': circuit.size(),
            'data': circuit.data  # Store gate information
        }

    def augment_dataset(self, augmentation_factor=2):
        """
        Augment the dataset by duplicating circuits with slight modifications.

        Parameters:
        augmentation_factor (int): Number of augmented copies for each circuit.
        """
        original_size = len(self.dataset)
        for _ in range(augmentation_factor):
            for circuit_dict in self.dataset:
                circuit = self.dict_to_circuit(circuit_dict)
                augmented_circuit = self.augment_circuit(circuit)
                self.add_circuit(augmented_circuit)
        print(f"Augmented dataset from {original_size} to {len(self.dataset)} circuits.")

    def dict_to_circuit(self, circuit_dict):
        """
        Convert a dictionary representation back to a QuantumCircuit.

        Parameters:
        circuit_dict (dict): The dictionary representation of the circuit.

        Returns:
        QuantumCircuit: The reconstructed quantum circuit.
        """
        circuit = QuantumCircuit(circuit_dict['num_qubits'])
        for gate in circuit_dict['data']:
            circuit.append(gate[0], gate[1])
        return circuit

    def augment_circuit(self, circuit: QuantumCircuit):
        """
        Apply random augmentations to a quantum circuit (e.g., adding noise).

        Parameters:
        circuit (QuantumCircuit): The quantum circuit to augment.

        Returns:
        QuantumCircuit: The augmented quantum circuit.
        """
        # Example augmentation: Add a random X gate to a random qubit
        import random
        qubit = random.randint(0, circuit.num_qubits - 1)
        circuit.x(qubit)  # Add an X gate to the selected qubit
        return circuit

    def split_dataset(self, train_ratio=0.8):
        """
        Split the dataset into training and testing sets.

        Parameters:
        train_ratio (float): Proportion of the dataset to include in the training set.

        Returns:
        tuple: (training_set, testing_set)
        """
        np.random.shuffle(self.dataset)  # Shuffle the dataset
        split_index = int(len(self.dataset) * train_ratio)
        training_set = self.dataset[:split_index]
        testing_set = self.dataset[split_index:]
        print(f"Split dataset into {len(training_set)} training circuits and {len(testing_set)} testing circuits.")
        return training_set, testing_set

# Example usage:
# dataset = CircuitDataset()
# circuit = QuantumCircuit(2)
# circuit.h(0)
# circuit.cx(0, 1)
# dataset.add_circuit(circuit)
# dataset.save_dataset('quantum_circuits .json')
# training_set, testing_set = dataset.split_dataset(0.8)
# dataset.augment_dataset(3)
