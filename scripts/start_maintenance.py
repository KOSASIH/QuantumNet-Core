# start_maintenance.py

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import random
import time
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Global variable to store telemetry data
telemetry_data = pd.DataFrame(columns=['timestamp', 'temperature', 'vibration', 'usage_hours'])

# Function to simulate telemetry data collection
def collect_telemetry_data():
    global telemetry_data
    while True:
        # Simulate data collection
        new_data = {
            'timestamp': pd.Timestamp.now(),
            'temperature': np.random.normal(loc=70, scale=5),  # Simulated temperature in Fahrenheit
            'vibration': np.random.normal(loc=0.5, scale=0.1),  # Simulated vibration level
            'usage_hours': random.randint(1, 100)  # Simulated usage hours
        }
        telemetry_data = telemetry_data.append(new_data, ignore_index=True)
        time.sleep(5)  # Collect data every 5 seconds

# Route to get telemetry data
@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    return jsonify(telemetry_data.to_dict(orient='records'))

# Route to predict maintenance needs
@app.route('/predict_maintenance', methods=['POST'])
def predict_maintenance():
    global telemetry_data
    if telemetry_data.empty:
        return jsonify({'status': 'No data available for prediction.'}), 400

    # Prepare data for prediction
    X = telemetry_data[['temperature', 'vibration', 'usage_hours']]
    y = np.random.randint(0, 2, size=len(telemetry_data))  # Simulated binary maintenance need (0 or 1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict maintenance needs on the test set
    predictions = model.predict(X_test)
    predictions = [1 if p > 0.5 else 0 for p in predictions]  # Convert to binary

    # Calculate mean squared error for evaluation
    mse = mean_squared_error(y_test, predictions)

    return jsonify({'predictions': predictions, 'mse': mse})

# Route to generate maintenance schedule
@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    data = request.json
    maintenance_frequency = data.get('frequency', 10)  # Frequency in hours
    current_time = pd.Timestamp.now()

    # Generate a simple maintenance schedule
    schedule = []
    for i in range(1, 6):  # Generate schedule for the next 5 maintenance sessions
        next_maintenance = current_time + pd.Timedelta(hours=i * maintenance_frequency)
        schedule.append({'session': i, 'scheduled_time': next_maintenance})

    return jsonify({'schedule': schedule})

# Start the telemetry data collection in a separate thread
def start_data_collection():
    collect_telemetry_data()

if __name__ == '__main__':
    # Start telemetry data collection thread
    data_collection_thread = Thread(target=start_data_collection)
    data_collection_thread.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5006, debug=True)
