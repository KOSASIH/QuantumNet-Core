# start_gravitational.py

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

# Global variable to store gravitational data
gravitational_data = pd.DataFrame(columns=['timestamp', 'gravitational_force', 'quantum_state'])

# Function to simulate gravitational data collection
def collect_gravitational_data():
    global gravitational_data
    while True:
        # Simulate data collection
        new_data = {
            'timestamp': pd.Timestamp.now(),
            'gravitational_force': np.random.normal(loc=9.81, scale=0.5),  # Simulated gravitational force in m/s^2
            'quantum_state': random.choice(['0', '1', 'superposition'])  # Simulated quantum state
        }
        gravitational_data = gravitational_data.append(new_data, ignore_index=True)
        time.sleep(5)  # Collect data every 5 seconds

# Route to get gravitational data
@app.route('/gravitational_data', methods=['GET'])
def get_gravitational_data():
    return jsonify(gravitational_data.to_dict(orient='records'))

# Route to analyze gravitational resilience
@app.route('/analyze_resilience', methods=['POST'])
def analyze_resilience():
    global gravitational_data
    if gravitational_data.empty:
        return jsonify({'status': 'No data available for analysis.'}), 400

    # Prepare data for analysis
    X = gravitational_data[['gravitational_force']]
    y = np.random.randint(0, 2, size=len(gravitational_data))  # Simulated binary resilience outcome (0 or 1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict resilience on the test set
    predictions = model.predict(X_test)
    predictions = [1 if p > 0.5 else 0 for p in predictions]  # Convert to binary

    # Calculate mean squared error for evaluation
    mse = mean_squared_error(y_test, predictions)

    return jsonify({'predictions': predictions, 'mse': mse})

# Route to generate resilience report
@app.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.json
    report_frequency = data.get('frequency', 10)  # Frequency in minutes
    current_time = pd.Timestamp.now()

    # Generate a simple resilience report
    report = []
    for i in range(1, 6):  # Generate report for the next 5 assessment sessions
        next_assessment = current_time + pd.Timedelta(minutes=i * report_frequency)
        report.append({'session': i, 'scheduled_time': next_assessment, 'status': 'Pending'})

    return jsonify({'report': report})

# Start the gravitational data collection in a separate thread
def start_data_collection():
    collect_gravitational_data()

if __name__ == '__main__':
    # Start gravitational data collection thread
    data_collection_thread = Thread(target=start_data_collection)
    data_collection_thread.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5007, debug=True)
