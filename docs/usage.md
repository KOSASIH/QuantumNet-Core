# Usage Examples and API Documentation for QuantumNet-Core

Welcome to the usage guide for QuantumNet-Core! This document provides examples of how to use the various modules and functionalities of the framework, along with API documentation for key classes and methods.

## Table of Contents

- [Getting Started](#getting-started)
- [Entanglement Management](#entanglement-management)
  - [Creating Entangled Qubits](#creating-entangled-qubits)
  - [Visualizing Entanglement](#visualizing-entanglement)
- [Quantum State Manipulation](#quantum-state-manipulation)
  - [Creating Quantum States](#creating-quantum-states)
  - [Manipulating Quantum States](#manipulating-quantum-states)
- [Quantum Circuit Operations](#quantum-circuit-operations)
  - [Building Quantum Circuits](#building-quantum-circuits)
  - [Executing Quantum Circuits](#executing-quantum-circuits)
- [API Reference](#api-reference)

## Getting Started

To use QuantumNet-Core, ensure that you have installed the framework as per the [installation instructions](installation.md). Once installed, you can start importing the necessary modules in your Python scripts.

## Entanglement Management

### Creating Entangled Qubits

You can create entangled qubits using the `create_entangled_pair` function from the `entangler` module. Here’s an example:

```python
1 from src.entanglement.entangler import create_entangled_pair
2 
3 # Create an entangled pair of qubits
4 qubit1, qubit2 = create_entangled_pair()
5 print(f"Entangled Qubits: {qubit1}, {qubit2}")
```

### Visualizing Entanglement

To visualize the entangled state, you can use the `visualize_entanglement` function:

```python
1 from src.entanglement.entanglement_visualization import visualize_entanglement
2 
3 # Visualize the entangled state
4 visualize_entanglement(qubit1, qubit2)
```

## Quantum State Manipulation

### Creating Quantum States

You can create quantum states using the `StateVector` class from the `quantum_state` module:

```python
1 from src.quantum_state.state_vector import StateVector
2: 
3 # Create a quantum state
4 state = StateVector([1, 0])  # Represents |0⟩ state
5 print(f"Quantum State: {state}")
```

### Manipulating Quantum States

To manipulate quantum states, you can apply operations such as measurement or transformation:

```python
1 # Measure the quantum state
2 measurement_result = state.measure()
3 print(f"Measurement Result: {measurement_result}")
```

## Quantum Circuit Operations

### Building Quantum Circuits

You can build quantum circuits using the `Circuit` class from the `quantum_circuit` module:

```python
1 from src.quantum_circuit.circuit import Circuit
2 
3 # Create a new quantum circuit
4 circuit = Circuit()
5 circuit.add_gate('H', target=0)  # Apply Hadamard gate to qubit 0
6 circuit.add_gate('CNOT', control=0, target=1)  # Apply CNOT gate
7 print("Quantum Circuit Built:")
8 print(circuit)
```

### Executing Quantum Circuits

To execute the quantum circuit, use the `execute` method:

```python
1 # Execute the quantum circuit
2 result = circuit.execute()
3 print(f"Circuit Execution Result: {result}")
```

## API Reference

### Entanglement Module

- **create_entangled_pair()**: Creates a pair of entangled qubits.
  - **Returns**: A tuple containing the two entangled qubits.

### Quantum State Module

- **StateVector**: Class representing a quantum state.
  - **Constructor**: `StateVector(amplitudes: List[float])`
  - **Methods**:
    - `measure()`: Measures the quantum state and returns the result.

### Quantum Circuit Module

- **Circuit**: Class representing a quantum circuit.
  - **Constructor**: `Circuit()`
  - **Methods**:
    - `add_gate(gate_type: str, target: int, control: Optional[int] = None)`: Adds a gate to the circuit.
    - `execute()`: Executes the quantum circuit and returns the result.

---

For more detailed information on each module and its functionalities, please refer to the respective API documentation files in the `docs/` directory.

For further assistance or inquiries, please reach out to the maintainers or open an issue in the [GitHub repository](https://github.com/KOSASIH/QuantumNet-Core).
