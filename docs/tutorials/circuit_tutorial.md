# Quantum Circuit Tutorial for QuantumNet-Core

Welcome to the Quantum Circuit Tutorial! In this guide, you will learn how to create, manipulate, and execute quantum circuits using the QuantumNet-Core framework. This tutorial will walk you through the process step-by-step, providing code examples and explanations along the way.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Creating a Quantum Circuit](#creating-a-quantum-circuit)
- [Adding Gates to the Circuit](#adding-gates-to-the-circuit)
- [Executing the Circuit](#executing-the-circuit)
- [Measuring the Results](#measuring-the-results)
- [Conclusion](#conclusion)

## Prerequisites

Before you begin, ensure that you have completed the following:

1. **Install QuantumNet-Core**: Follow the [installation instructions](../installation.md) to set up the framework on your local machine.
2. **Basic Python Knowledge**: Familiarity with Python programming will help you understand the examples provided in this tutorial.

## Creating a Quantum Circuit

In this section, you will learn how to create a quantum circuit using the `Circuit` class.

### Step 1: Import the Required Module

Start by importing the `Circuit` class from the quantum circuit module:

```python
1 from src.quantum_circuit.circuit import Circuit
```

### Step 2: Create a New Quantum Circuit

Now, you can create a new quantum circuit:

```python
1 # Create a new quantum circuit
2 circuit = Circuit()
3 print("Quantum Circuit Created:")
4 print(circuit)
```

## Adding Gates to the Circuit

In this section, you will learn how to add quantum gates to your circuit.

### Step 1: Add a Hadamard Gate

The Hadamard gate creates superposition. You can add it to your circuit as follows:

```python
1 # Add a Hadamard gate to qubit 0
2 circuit.add_gate('H', target=0)
3 print("Hadamard Gate Added to Qubit 0:")
4 print(circuit)
```

### Step 2: Add a CNOT Gate

The CNOT (Controlled-NOT) gate is used to create entanglement between qubits. Here’s how to add it:

```python
1 # Add a CNOT gate with control on qubit 0 and target on qubit 1
2 circuit.add_gate('CNOT', control=0, target=1)
3 print("CNOT Gate Added (Control: Qubit 0, Target: Qubit 1):")
4 print(circuit)
```

## Executing the Circuit

Now that you have built your quantum circuit, you can execute it to obtain results.

### Step 1: Execute the Circuit

To execute the quantum circuit, use the `execute` method:

```python
1 # Execute the quantum circuit
2 result = circuit.execute()
3 print(f"Circuit Execution Result: {result}")
```

### Explanation

The `execute` method runs the circuit and returns the measurement results of the qubits after applying the gates in the circuit.

## Measuring the Results

After executing the circuit, you can measure the results to obtain classical outcomes.

### Step 1: Measure the Qubits

You can measure the qubits to see their final states:

```python
1 # Measure the results of the qubits
2 measurement_results = circuit.measure()
3 print(f"Measurement Results: {measurement_results}")
```

### Explanation

The `measure` method collapses the quantum states of the qubits to classical bits, providing the final measurement outcomes.

## Conclusion

In this tutorial, you have learned how to create, manipulate, and execute quantum circuits using the QuantumNet-Core framework. Understanding quantum circuits is essential for exploring more advanced quantum algorithms and applications.

For further exploration, consider experimenting with different gate combinations or integrating these concepts into larger quantum systems.

If you have any questions or need assistance, feel free to reach out to the community or refer to the documentation.

---

For more tutorials and information, visit the [QuantumNet-Core GitHub repository](https://github.com/KOSASIH/QuantumNet-Core).
