"""
Visualization Tools for Quantum Resource Hyper-Optimizer (QRHO).
"""
import matplotlib.pyplot as plt

def plot_resource_allocation(allocation: dict, title: str = "Resource Allocation", save_path: str = None):
    """
    Plot the resource allocation as a bar chart.

    Parameters:
    allocation (dict): Resource allocation data.
    title (str): Title of the plot.
    save_path (str): Optional path to save the plot as an image file.
    """
    resources = list(allocation.keys())
    values = list(allocation.values())

    plt.figure(figsize=(10, 6))
    plt.bar(resources, values, color='blue', alpha=0.7)
    plt.xlabel('Resources', fontsize=14)
    plt.ylabel('Allocation', fontsize=14)
    plt.title(title, fontsize=16)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Plot saved to {save_path}.")
    else:
        plt.show()

def plot_resource_efficiency(efficiency: float, title: str = "Resource Efficiency"):
    """
    Plot the resource efficiency as a single bar.

    Parameters:
    efficiency (float): Efficiency score (0 to 1).
    title (str): Title of the plot.
    """
    plt.figure(figsize=(6, 4))
    plt.barh(['Efficiency'], [efficiency], color='green' if efficiency >= 0.75 else 'orange' if efficiency >= 0.5 else 'red', alpha=0.7)
    plt.xlim(0, 1)
    plt.xlabel('Efficiency Score', fontsize=14)
    plt.title(title, fontsize=16)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

def plot_resource_comparison(allocation1: dict, allocation2: dict, title: str = "Resource Comparison"):
    """
    Compare two resource allocations side by side.

    Parameters:
    allocation1 (dict): First resource allocation data.
    allocation2 (dict): Second resource allocation data.
    title (str): Title of the plot.
    """
    resources = list(set(allocation1.keys()).union(set(allocation2.keys())))
    values1 = [allocation1.get(r, 0) for r in resources]
    values2 = [allocation2.get(r, 0) for r in resources]

    x = range(len(resources))
    width = 0.35  # Width of the bars

    plt.figure(figsize=(12, 6))
    plt.bar(x, values1, width, label='Allocation 1', color='blue', alpha=0.7)
    plt.bar([p + width for p in x], values2, width, label='Allocation 2', color='orange', alpha=0.7)

    plt.xlabel('Resources', fontsize=14)
    plt.ylabel('Allocation', fontsize=14)
    plt.title(title, fontsize=16)
    plt.xticks([p + width / 2 for p in x], resources)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Example usage:
if __name__ == "__main__":
    allocation = {'qubits': 5, 'gates': 10, 'ancillas': 3}
    plot_resource_allocation(allocation, title="Current Resource Allocation")

    efficiency = 0.85
    plot_resource_efficiency(efficiency, title="Current Resource Efficiency")

    allocation1 = {'qubits': 5, 'gates': 10, 'ancillas': 3}
    allocation2 = {'qubits': 7, 'gates': 8, 'ancillas': 2}
    plot_resource_comparison(allocation1, allocation2, title="Resource Allocation Comparison")
