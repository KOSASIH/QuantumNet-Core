# examples/entanglement_example.py

import numpy as np
from quantum_circuit.entanglement import create_entangled_state

def main():
    # Create a Bell state (entangled state)
    entangled_state = create_entangled_state()
    print("Entangled State (Bell State):")
    print(entangled_state)

    # Check properties of the entangled state
    norm = np.linalg.norm(entangled_state)
    print(f"Norm of the entangled state: {norm}")

if __name__ == "__main__":
    main()
