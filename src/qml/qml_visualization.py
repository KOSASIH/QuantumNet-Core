import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_bloch_sphere(state_vector):
    """
    Visualize a quantum state on the Bloch sphere.
    
    Parameters:
    - state_vector (np.ndarray): The quantum state vector (should be normalized).
    """
    if len(state_vector) != 2:
        raise ValueError("State vector must be a 2-dimensional vector.")
    
    # Calculate the angles for the Bloch sphere representation
    theta = 2 * np.arccos(np.abs(state_vector[0]))
    phi = np.angle(state_vector[1])
    
    # Convert spherical coordinates to Cartesian coordinates
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    
    # Plotting the Bloch sphere
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, x, y, z, color='r', arrow_length_ratio=0.1)
    
    # Set the limits and labels
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Bloch Sphere Representation')
    
    plt.show()

def plot_training_results(epochs, accuracy, loss):
    """
    Generate plots for training results including accuracy and loss over epochs.
    
    Parameters:
    - epochs (list): List of epoch numbers.
    - accuracy (list): List of accuracy values over epochs.
    - loss (list): List of loss values over epochs.
    """
    fig, ax1 = plt.subplots()

    # Plot accuracy
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Accuracy', color='tab:blue')
    ax1.plot(epochs, accuracy, color='tab:blue', label='Accuracy')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Create a second y-axis for loss
    ax2 = ax1.twinx()
    ax2.set_ylabel('Loss', color='tab:red')
    ax2.plot(epochs, loss, color='tab:red', label='Loss')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title('Training Results')
    fig.tight_layout()
    plt.show()

def plot_histogram(data, title='Data Distribution', xlabel='Value', ylabel='Frequency'):
    """
    Generate a histogram for the given data.
    
    Parameters:
    - data (list or np.ndarray): The data to be visualized in a histogram.
    - title (str): Title of the histogram.
    - xlabel (str): Label for the x-axis.
    - ylabel (str): Label for the y-axis.
    """
    plt.hist(data, bins=30, alpha=0.7, color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example quantum state
    example_state = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # |+> state
    plot_bloch_sphere(example_state)

    # Example training results
    epochs = list(range(1, 11))
    accuracy = [0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 1.0]
    loss = [1.0, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.01]
    plot_training_results(epochs, accuracy, loss)

    # Example histogram
    data = np.random.normal(0, 1, 1000)
    plot_histogram(data)
