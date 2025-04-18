# API Reference for QuantumNet-Core

This document provides an API reference for the QuantumNet-Core framework. It includes detailed descriptions of the classes, methods, and functionalities available in each module.

## Table of Contents

- [Entanglement Module](#entanglement-module)
  - [Entangler Class](#entangler-class)
- [Quantum State Module](#quantum-state-module)
  - [StateVector Class](#statevector-class)
  - [DensityMatrix Class](#densitymatrix-class)
- [Quantum Circuit Module](#quantum-circuit-module)
  - [Circuit Class](#circuit-class)
- [Utilities Module](#utilities-module)
  - [Logger Class](#logger-class)
  - [Config Class](#config-class)

## Entanglement Module

### Entangler Class

The `Entangler` class provides methods for creating and measuring entangled qubits.

#### Methods

- **create_entangled_pair()**
  - **Description**: Creates a pair of entangled qubits.
  - **Returns**: A tuple containing two entangled qubits.

- **measure_entanglement(qubit1, qubit2)**
  - **Description**: Measures the degree of entanglement between two qubits.
  - **Parameters**:
    - `qubit1`: The first qubit.
    - `qubit2`: The second qubit.
  - **Returns**: A numerical value representing the degree of entanglement.

## Quantum State Module

### StateVector Class

The `StateVector` class represents a quantum state using a state vector.

#### Constructor

- **StateVector(amplitudes: List[float])**
  - **Description**: Initializes a quantum state with the given amplitudes.
  - **Parameters**:
    - `amplitudes`: A list of complex numbers representing the state vector.

#### Methods

- **measure()**
  - **Description**: Measures the quantum state and collapses it to one of the basis states.
  - **Returns**: The measurement result (0 or 1).

### DensityMatrix Class

The `DensityMatrix` class represents a quantum state using a density matrix.

#### Constructor

- **DensityMatrix(matrix: List[List[complex]])**
  - **Description**: Initializes a quantum state with the given density matrix.
  - **Parameters**:
    - `matrix`: A 2D list representing the density matrix.

#### Methods

- **trace()**
  - **Description**: Computes the trace of the density matrix.
  - **Returns**: The trace value.

- **measure()**
  - **Description**: Measures the quantum state represented by the density matrix.
  - **Returns**: The measurement result (0 or 1).

## Quantum Circuit Module

### Circuit Class

The `Circuit` class allows users to build and execute quantum circuits.

#### Constructor

- **Circuit()**
  - **Description**: Initializes a new quantum circuit.

#### Methods

- **add_gate(gate_type: str, target: int, control: Optional[int] = None)**
  - **Description**: Adds a gate to the circuit.
  - **Parameters**:
    - `gate_type`: The type of gate (e.g., 'H', 'CNOT').
    - `target`: The target qubit index.
    - `control`: The control qubit index (optional, for controlled gates).

- **execute()**
  - **Description**: Executes the quantum circuit and returns the measurement results.
  - **Returns**: A list of measurement results for each qubit.

- **measure()**
  - **Description**: Measures the qubits in the circuit and returns the results.
  - **Returns**: A list of measurement results (0 or 1 for each qubit).

## Utilities Module

### Logger Class

The `Logger` class provides logging utilities for debugging and monitoring.

#### Methods

- **log(message: str)**
  - **Description**: Logs a message to the console or a log file.
  - **Parameters**:
    - `message`: The message to log.

### Config Class

The `Config` class manages configuration settings for the framework.

#### Methods

- **get_setting(key: str)**
  - **Description**: Retrieves a configuration setting by key.
  - **Parameters**:
    - `key`: The key of the setting to retrieve.
  - **Returns**: The value of the configuration setting.

- **set_setting(key: str, value: Any)**
  - **Description**: Sets a configuration setting by key.
  - **Parameters**:
    - `key`: The key of the setting to set.
    - `value`: The value to assign to the setting.

## Conclusion

This API reference provides a comprehensive overview of the classes and methods available in the QuantumNet-Core framework. Users can utilize this documentation to understand the functionalities offered by each module and effectively implement quantum computing solutions.

For further details, examples, and updates, please refer to the official [QuantumNet-Core documentation](https://github.com/KOSASIH/QuantumNet-Core).
