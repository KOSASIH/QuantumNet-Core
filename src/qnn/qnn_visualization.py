# src/qnn/qnn_visualization.py

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

def visualize_predictions(predictions, plot_type='bar', save_as=None, title='Predicted Quantum State Probabilities', color='blue'):
    """Visualize the predictions of the QNN.
    
    Args:
        predictions (dict): Dictionary of predictions with states as keys and probabilities as values.
        plot_type (str): Type of plot ('bar', 'pie', 'line').
        save_as (str): Filename to save the plot (e.g., 'plot.png'). If None, the plot will not be saved.
        title (str): Title of the plot.
        color (str): Color of the plot elements.
    """
    if not isinstance(predictions, dict) or not predictions:
        raise ValueError("Predictions must be a non-empty dictionary.")

    states = list(predictions.keys())
    probabilities = list(predictions.values())

    if plot_type == 'bar':
        plt.bar(states, probabilities, color=color)
        plt.xlabel('Quantum States')
        plt.ylabel('Probabilities')
        plt.title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save_as:
            plt.savefig(save_as)
        plt.show()

    elif plot_type == 'pie':
        plt.pie(probabilities, labels=states, autopct='%1.1f%%', startangle=90)
        plt.title(title)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        if save_as:
            plt.savefig(save_as)
        plt.show()

    elif plot_type == 'line':
        plt.plot(states, probabilities, marker='o', color=color)
        plt.xlabel('Quantum States')
        plt.ylabel('Probabilities')
        plt.title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save_as:
            plt.savefig(save_as)
        plt.show()

    else:
        raise ValueError("Unsupported plot type. Use 'bar', 'pie', or 'line'.")

def interactive_visualization(predictions):
    """Create an interactive visualization of the predictions using Plotly.
    
    Args:
        predictions (dict): Dictionary of predictions with states as keys and probabilities as values.
    """
    if not isinstance(predictions, dict) or not predictions:
        raise ValueError("Predictions must be a non-empty dictionary.")

    states = list(predictions.keys())
    probabilities = list(predictions.values())

    fig = go.Figure(data=[go.Bar(x=states, y=probabilities, marker_color='blue')])
    fig.update_layout(title='Predicted Quantum State Probabilities',
                      xaxis_title='Quantum States',
                      yaxis_title='Probabilities',
                      template='plotly_white')
    fig.show()

def compare_predictions(predictions_list, labels):
    """Compare multiple sets of predictions side by side.
    
    Args:
        predictions_list (list): List of dictionaries of predictions.
        labels (list): List of labels for each set of predictions.
    """
    if not isinstance(predictions_list, list) or not predictions_list or len(predictions_list) != len(labels):
        raise ValueError("predictions_list must be a list of non-empty dictionaries with corresponding labels.")

    num_predictions = len(predictions_list)
    states = list(predictions_list[0].keys())
    bar_width = 0.15
    x = np.arange(len(states))

    for i, predictions in enumerate(predictions_list):
        probabilities = list(predictions.values())
        plt.bar(x + i * bar_width, probabilities, width=bar_width, label=labels[i])

    plt.xlabel('Quantum States')
    plt.ylabel('Probabilities')
    plt.title('Comparison of Predicted Quantum State Probabilities')
    plt.xticks(x + bar_width / 2, states)
    plt.legend()
    plt.tight_layout()
    plt.show()
