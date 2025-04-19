import matplotlib.pyplot as plt
import numpy as np

def visualize_surface_code(surface_code, show_stabilizers=False, save_path=None):
    """Visualize the surface code lattice with optional stabilizer display.
    
    Parameters:
    - surface_code (SurfaceCode): The surface code object containing qubit states.
    - show_stabilizers (bool): Whether to display stabilizers on the lattice.
    - save_path (str): Optional path to save the visualization as an image.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Display the qubit states
    cax = ax.imshow(surface_code.qubits, cmap='gray', interpolation='nearest')
    ax.set_title('Surface Code Lattice')
    plt.colorbar(cax, label='Qubit State (0 or 1)')
    
    # Optionally display stabilizers
    if show_stabilizers:
        stabilizers = surface_code.measure_stabilizers()
        for i, stabilizer in enumerate(stabilizers):
            if stabilizer == 1:
                # Highlight the stabilizer position
                ax.text(i // surface_code.size, i % surface_code.size, 'S', color='red', fontsize=12, ha='center', va='center')

    # Highlight errors if any
    for (x, y) in np.argwhere(surface_code.qubits == 1):
        ax.text(x, y, 'E', color='blue', fontsize=12, ha='center', va='center')

    # Save the visualization if a path is provided
    if save_path:
        plt.savefig(save_path)
        print(f"Visualization saved to {save_path}")

    plt.show()

# Example usage
if __name__ == "__main__":
    from surface_code import SurfaceCode
    surface_code = SurfaceCode(size=5)
    surface_code.apply_error(2, 2)  # Simulate an error
    visualize_surface_code(surface_code, show_stabilizers=True, save_path='surface_code_visualization.png')
