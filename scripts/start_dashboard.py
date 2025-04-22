# start_dashboard.py

from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import os
import json
from threading import Thread
import time

# Initialize Flask app
app = Flask(__name__)

# Global variable to store telemetry data
telemetry_data = pd.DataFrame(columns=['timestamp', 'temperature', 'humidity'])

# Function to simulate telemetry data collection
def collect_telemetry_data():
    global telemetry_data
    while True:
        # Simulate data collection
        new_data = {
            'timestamp': pd.Timestamp.now(),
            'temperature': np.random.normal(loc=20, scale=2),
            'humidity': np.random.uniform(low=30, high=90)
        }
        telemetry_data = telemetry_data.append(new_data, ignore_index=True)
        time.sleep(5)  # Collect data every 5 seconds

# Route for the dashboard home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get telemetry data for visualization
@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    return jsonify(telemetry_data.to_dict(orient='records'))

# Route to generate telemetry plot
@app.route('/telemetry_plot', methods=['GET'])
def telemetry_plot():
    fig = px.line(telemetry_data, x='timestamp', y=['temperature', 'humidity'], title='Telemetry Data Over Time')
    graph_json = pio.to_json(fig)
    return graph_json

# Route to execute a quantum circuit (placeholder for actual execution)
@app.route('/execute_circuit', methods=['POST'])
def execute_circuit():
    # Placeholder for circuit execution logic
    circuit_params = request.json.get('params', [])
    # Simulate circuit execution result
    result = {
        'success': True,
        'result': np.random.random()  # Simulated result
    }
    return jsonify(result)

# Start the telemetry data collection in a separate thread
def start_data_collection():
    collect_telemetry_data()

if __name__ == '__main__':
    # Start telemetry data collection thread
    data_collection_thread = Thread(target=start_data_collection)
    data_collection_thread.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
