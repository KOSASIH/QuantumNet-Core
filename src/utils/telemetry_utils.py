# telemetry_utils.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import json
import os

class TelemetryDataProcessor:
    def __init__(self, data_path):
        """
        Initializes the TelemetryDataProcessor with the path to the telemetry data.

        :param data_path: Path to the telemetry data file (CSV or JSON).
        """
        self.data_path = data_path
        self.data = self.load_data()
        self.scaler = StandardScaler()

    def load_data(self):
        """
        Loads telemetry data from a specified file.

        :return: DataFrame containing the telemetry data.
        """
        if self.data_path.endswith('.csv'):
            return pd.read_csv(self.data_path)
        elif self.data_path.endswith('.json'):
            return pd.read_json(self.data_path)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV or JSON file.")

    def preprocess_data(self):
        """
        Preprocesses the telemetry data by handling missing values and scaling features.
        """
        # Fill missing values with the mean of each column
        self.data.fillna(self.data.mean(), inplace=True)

        # Scale the features
        self.data[self.data.columns] = self.scaler.fit_transform(self.data[self.data.columns])

    def detect_anomalies(self, contamination=0.05):
        """
        Detects anomalies in the telemetry data using Isolation Forest.

        :param contamination: Proportion of outliers in the data set.
        :return: DataFrame with an additional column indicating anomalies.
        """
        model = IsolationForest(contamination=contamination)
        self.data['anomaly'] = model.fit_predict(self.data)

        # Mark anomalies as True/False
        self.data['anomaly'] = self.data['anomaly'] == -1
        return self.data[self.data['anomaly']]

    def visualize_telemetry(self):
        """
        Visualizes telemetry data trends over time.
        """
        plt.figure(figsize=(12, 6))
        for column in self.data.columns:
            if column != 'timestamp' and column != 'anomaly':
                plt.plot(self.data['timestamp'], self.data[column], label=column)
        
        plt.title('Telemetry Data Trends')
        plt.xlabel('Timestamp')
        plt.ylabel('Values')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def save_processed_data(self, output_path):
        """
        Saves the processed telemetry data to a specified output path.

        :param output_path: Path to save the processed data (CSV or JSON).
        """
        if output_path.endswith('.csv'):
            self.data.to_csv(output_path, index=False)
        elif output_path.endswith('.json'):
            self.data.to_json(output_path, orient='records', lines=True)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV or JSON file.")

    def generate_summary_statistics(self):
        """
        Generates summary statistics of the telemetry data.

        :return: Dictionary containing summary statistics.
        """
        summary = {
            'mean': self.data.mean().to_dict(),
            'std_dev': self.data.std().to_dict(),
            'min': self.data.min().to_dict(),
            'max': self.data.max().to_dict(),
            'count': self.data.count().to_dict()
        }
        return summary

    def export_summary_to_json(self, output_path):
        """
        Exports summary statistics to a JSON file.

        :param output_path: Path to save the summary statistics.
        """
        summary = self.generate_summary_statistics()
        with open(output_path, 'w') as json_file:
            json.dump(summary, json_file, indent=4)

# Example usage
if __name__ == "__main__":
    telemetry_processor = TelemetryDataProcessor(data_path='data/telemetry/node_telemetry.csv')
    telemetry_processor.preprocess_data()
    anomalies = telemetry_processor.detect_anomalies()
    print("Detected Anomalies:")
    print(anomalies)

    telemetry_processor.visualize_telemetry()
    telemetry_processor.save_processed_data(output_path='data/telemetry/processed_telemetry.csv')
    telemetry_processor.export_summary_to_json(output_path='data/telemetry/summary_statistics.json')
