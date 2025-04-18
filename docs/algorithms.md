# Core Algorithms in QuantumNet-Core

This document provides detailed descriptions of the core algorithms implemented in QuantumNet-Core. These algorithms are fundamental to the framework's functionality, enabling users to perform various quantum computing tasks.

## Table of Contents

- [Entanglement Management Algorithms](#entanglement-management-algorithms)
  - [Entangled Pair Creation](#entangled-pair-creation)
  - [Entanglement Measurement](#entanglement-measurement)
- [Quantum State Algorithms](#quantum-state-algorithms)
  - [State Vector Representation](#state-vector-representation)
  - [Density Matrix Representation](#density-matrix-representation)
- [Quantum Circuit Algorithms](#quantum-circuit-algorithms)
  - [Gate Operations](#gate-operations)
  - [Circuit Execution](#circuit-execution)

## Entanglement Management Algorithms

### Entangled Pair Creation

**Function**: `create_entangled_pair()`

- **Description**: This algorithm generates a pair of entangled qubits using the principles of quantum mechanics. It typically utilizes the Bell state creation method, which produces maximally entangled states.
- **Usage**:
  ```python
  1 from src.entanglement.entangler import create_entangled_pair
  2 
  3 qubit1, qubit2 = create_entangled_pair()
  ```
- **Output**: Returns two qubits that are in an entangled state, allowing for quantum correlations.

### Entanglement Measurement

**Function**: `measure_entanglement(qubit1, qubit2)`

- **Description**: This algorithm measures the degree of entanglement between two qubits. It can utilize various metrics, such as concurrence or entanglement entropy, to quantify the entanglement.
- **Usage**:
  ```python
  1 from src.entanglement.entangler import measure_entanglement
  2 
  3 entanglement_degree = measure_entanglement(qubit1, qubit2)
  ```
- **Output**: Returns a numerical value representing the degree of entanglement.

## Quantum State Algorithms

### State Vector Representation

**Class**: `StateVector`

- **Description**: This class represents a quantum state using a state vector, which is a mathematical representation of the quantum state in a Hilbert space.
- **Constructor**: 
  ```python
  1 StateVector(amplitudes: List[float])
  ```
- **Methods**:
  - `measure()`: Measures the quantum state and collapses it to one of the basis states.
- **Usage**:
  ```python
  1 from src.quantum_state.state_vector import StateVector
  2 
  3 state = StateVector([1, 0])  # Represents |0⟩ state
  4 measurement_result = state.measure()
  ```

### Density Matrix Representation

**Class**: `DensityMatrix`

- **Description**: This class represents a quantum state using a density matrix, which is useful for mixed states and provides a complete description of the quantum system.
- **Constructor**: 
  ```python
  1 DensityMatrix(matrix: List[List[complex]])
  ```
- **Methods**:
  - `trace()`: Computes the trace of the density matrix.
  - `measure()`: Measures the quantum state represented by the density matrix.
- **Usage**:
  ```python
  1 from src.quantum_state.density_matrix import DensityMatrix
  2 
  3 density_matrix = DensityMatrix([[1, 0], [0, 0]])  # Represents |0⟩ state
  4 measurement_result = density_matrix.measure()
  ```

## Quantum Circuit Algorithms

### Gate Operations

**Class**: `Circuit`

- **Description**: This class allows users to build quantum circuits by adding quantum gates. It supports various gate types, including single-qubit and multi-qubit gates.
- **Methods**:
  - `add_gate(gate_type: str, target: int, control: Optional[int] = None)`: Adds a gate to the circuit.
- **Usage**:
  ```python
  1 from src.quantum_circuit.circuit import Circuit
  2 
  3 circuit = Circuit()
  4 circuit.add_gate('H', target=0)  # Apply Hadamard gate to qubit 0
  5 circuit.add_gate('CNOT', control=0, target=1)  # Apply CNOT gate
  ```

### Circuit Execution

**Method**: `execute()`

- **Description**: This method executes the quantum circuit and returns the measurement results of the qubits after applying the gates in the circuit.
- **Usage**:
  ```python
  1 result = circuit.execute()
  2 print(f"Circuit Execution Result: {result}")
  ```
- **Output**: Returns the measurement results of the qubits after executing the circuit, providing insights into the quantum state post-operation.

---

For further exploration of the algorithms and their implementations, users are encouraged to refer to the source code and additional documentation available in the `docs/` directory. This will provide a deeper understanding of the underlying principles and optimizations used in QuantumNet-Core.
