# visualization_utils.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from matplotlib.ticker import MaxNLocator

class VisualizationUtils:
    def __init__(self, data):
        """
        Initializes the VisualizationUtils with the provided data.

        :param data: DataFrame containing the data to visualize.
        """
        self.data = data

    def line_plot(self, x, y, title='Line Plot', xlabel='X-axis', ylabel='Y-axis', save_path=None):
        """
        Creates a line plot.

        :param x: Column name for the x-axis.
        :param y: Column name for the y-axis.
        :param title: Title of the plot.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param save_path: Path to save the plot image (optional).
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data[x], self.data[y], marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def scatter_plot(self, x, y, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis', save_path=None):
        """
        Creates a scatter plot.

        :param x: Column name for the x-axis.
        :param y: Column name for the y-axis.
        :param title: Title of the plot.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param save_path: Path to save the plot image (optional).
        """
        plt.figure(figsize=(12, 6))
        plt.scatter(self.data[x], self.data[y], alpha=0.7)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def histogram(self, column, title='Histogram', xlabel='Value', ylabel='Frequency', bins=30, save_path=None):
        """
        Creates a histogram.

        :param column: Column name to create the histogram for.
        :param title: Title of the plot.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param bins: Number of bins for the histogram.
        :param save_path: Path to save the plot image (optional).
        """
        plt.figure(figsize=(12, 6))
        plt.hist(self.data[column], bins=bins, alpha=0.7, color='blue', edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def heatmap(self, correlation_matrix, title='Heatmap', save_path=None):
        """
        Creates a heatmap for the correlation matrix.

        :param correlation_matrix: DataFrame containing the correlation matrix.
        :param title: Title of the heatmap.
        :param save_path: Path to save the plot image (optional).
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
        plt.title(title)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def interactive_scatter_plot(self, x, y, title='Interactive Scatter Plot', save_path=None):
        """
        Creates an interactive scatter plot using Plotly.

        :param x: Column name for the x-axis.
        :param y: Column name for the y-axis.
        :param title: Title of the plot.
        :param save_path: Path to save the plot as HTML (optional).
        """
        fig = px.scatter(self.data, x=x, y=y, title=title, labels={x: x, y: y})
        fig.update_traces(marker=dict(size=10, opacity=0.7))
        
        if save_path:
            fig.write_html(save_path)
        fig.show()

    def bar_chart(self, x, y, title='Bar Chart', xlabel='Categories', ylabel='Values', save_path=None):
        """
        Creates a bar chart.

        :param x: Column name for the x-axis (categories).
        :param y: Column name for the y-axis (values).
        :param title: Title of the chart.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param save_path: Path to save the chart image (optional).
        """
        plt.figure(figsize=(12, 6))
        plt.bar(self.data[x], self.data[y], color='skyblue', edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def box_plot(self, column, title='Box Plot', xlabel='Categories', ylabel='Values', save_path=None):
        """
        Creates a box plot.

        :param column: Column name to create the box plot for.
        :param title: Title of the plot.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param save_path: Path to save the plot image (optional).
        """
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.data, y=column)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'timestamp': pd.date_range(start='1/1/2023', periods=100, freq='H'),
        'temperature': np.random.normal(loc=20, scale=5, size=100),
        'humidity': np.random.uniform(low=30, high=90, size=100)
    }
    df = pd.DataFrame(sample_data)

    visualizer = VisualizationUtils(data=df)
    visualizer.line_plot(x='timestamp', y='temperature', title='Temperature Over Time')
    visualizer.scatter_plot(x='temperature', y='humidity', title='Temperature vs Humidity')
    visualizer.histogram(column='temperature', title='Temperature Distribution')
    visualizer.heatmap(correlation_matrix=df.corr(), title='Correlation Heatmap')
    visualizer.interactive_scatter_plot(x='temperature', y='humidity', title='Interactive Temp vs Humidity')
    visualizer.bar_chart(x='timestamp', y='temperature', title='Temperature Bar Chart')
    visualizer.box_plot(column='temperature', title='Temperature Box Plot')
