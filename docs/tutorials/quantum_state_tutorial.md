# Quantum State Tutorial for QuantumNet-Core

Welcome to the Quantum State Tutorial! In this guide, you will learn how to create, manipulate, and measure quantum states using the QuantumNet-Core framework. This tutorial will walk you through the process step-by-step, providing code examples and explanations along the way.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Creating Quantum States](#creating-quantum-states)
  - [State Vector Representation](#state-vector-representation)
  - [Density Matrix Representation](#density-matrix-representation)
- [Manipulating Quantum States](#manipulating-quantum-states)
  - [Applying Operations](#applying-operations)
- [Measuring Quantum States](#measuring-quantum-states)
- [Conclusion](#conclusion)

## Prerequisites

Before you begin, ensure that you have completed the following:

1. **Install QuantumNet-Core**: Follow the [installation instructions](../installation.md) to set up the framework on your local machine.
2. **Basic Python Knowledge**: Familiarity with Python programming will help you understand the examples provided in this tutorial.

## Creating Quantum States

In this section, you will learn how to create quantum states using both state vector and density matrix representations.

### State Vector Representation

#### Step 1: Import the Required Module

Start by importing the `StateVector` class from the quantum state module:

```python
1 from src.quantum_state.state_vector import StateVector
```

#### Step 2: Create a Quantum State

Now, you can create a quantum state using the state vector representation:

```python
1 # Create a quantum state representing |0⟩
2 state_0 = StateVector([1, 0])  # Amplitudes for |0⟩ state
3 print(f"Quantum State |0⟩: {state_0}")
4 
5 # Create a quantum state representing |1⟩
6 state_1 = StateVector([0, 1])  # Amplitudes for |1⟩ state
7 print(f"Quantum State |1⟩: {state_1}")
```

### Density Matrix Representation

#### Step 1: Import the Required Module

Import the `DensityMatrix` class:

```python
1 from src.quantum_state.density_matrix import DensityMatrix
```

#### Step 2: Create a Density Matrix

You can create a density matrix representing a quantum state:

```python
1 # Create a density matrix for the |0⟩ state
2 density_matrix_0 = DensityMatrix([[1, 0], [0, 0]])  # Represents |0⟩ state
3 print(f"Density Matrix for |0⟩:\n{density_matrix_0}")
4 
5 # Create a density matrix for the |1⟩ state
6 density_matrix_1 = DensityMatrix([[0, 0], [0, 1]])  # Represents |1⟩ state
7 print(f"Density Matrix for |1⟩:\n{density_matrix_1}")
```

## Manipulating Quantum States

In this section, you will learn how to apply operations to quantum states.

### Applying Operations

#### Step 1: Import the Required Operations

You can apply operations such as measurement or transformations to the quantum states. For this example, we will measure the states.

```python
1 # Measure the quantum state represented by the state vector
2 measurement_result_0 = state_0.measure()
3 print(f"Measurement Result for |0⟩: {measurement_result_0}")
4 
5 # Measure the quantum state represented by the density matrix
6 measurement_result_1 = density_matrix_1.measure()
7 print(f"Measurement Result for |1⟩: {measurement_result_1}")
```

### Explanation

The `measure()` method collapses the quantum state to one of the basis states and returns the measurement result.

## Measuring Quantum States

You can measure the quantum states to obtain classical outcomes.

### Step 1: Measure the State Vector

```python
1 # Measure the |0⟩ state
2 measurement_result_0 = state_0.measure()
3 print(f"Measurement Result for |0⟩: {measurement_result_0}")
```

### Step 2: Measure the Density Matrix

```python
1 # Measure the density matrix for |1⟩ state
2 measurement_result_1 = density_matrix_1.measure()
3 print(f"Measurement Result for |1⟩: {measurement_result_1}")
```

## Conclusion

In this tutorial, you have learned how to create, manipulate, and measure quantum states using the QuantumNet-Core framework. Understanding quantum states is fundamental for exploring more advanced quantum algorithms and applications.

For further exploration, consider experimenting with different quantum operations or integrating these concepts into larger quantum systems.

If you have any questions or need assistance, feel free to reach out to the community or refer to the documentation.

---

For more tutorials and information, visit the [QuantumNet-Core GitHub repository](https://github.com/KOSASIH/QuantumNet-Core).
