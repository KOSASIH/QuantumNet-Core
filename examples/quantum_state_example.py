# examples/quantum_state_example.py

import numpy as np
from quantum_circuit.gate_operations import apply_gate

def main():
    # Define a quantum state |0⟩
    state = np.array([1, 0])  # |0⟩ state

    # Define an X gate (NOT gate)
    x_gate = np.array([[0, 1], [1, 0]])  # X gate

    # Apply the X gate to the state
    new_state = apply_gate(state, x_gate, 0)
    print("State after applying X gate:")
    print(new_state)  # Should be |1⟩ state

if __name__ == "__main__":
    main()
