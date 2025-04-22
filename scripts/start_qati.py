# start_qati.py

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import time
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Global variable to store telemetry data
telemetry_data = pd.DataFrame(columns=['timestamp', 'metric1', 'metric2', 'metric3'])

# Function to simulate telemetry data collection
def collect_telemetry_data():
    global telemetry_data
    while True:
        # Simulate data collection
        new_data = {
            'timestamp': pd.Timestamp.now(),
            'metric1': np.random.normal(loc=0, scale=1),
            'metric2': np.random.normal(loc=0, scale=1),
            'metric3': np.random.normal(loc=0, scale=1)
        }
        telemetry_data = telemetry_data.append(new_data, ignore_index=True)
        time.sleep(5)  # Collect data every 5 seconds

# Route to get telemetry data
@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    return jsonify(telemetry_data.to_dict(orient='records'))

# Route to detect anomalies in telemetry data
@app.route('/detect_anomalies', methods=['POST'])
def detect_anomalies():
    global telemetry_data
    if telemetry_data.empty:
        return jsonify({'status': 'No data available for anomaly detection.'}), 400

    # Prepare data for anomaly detection
    features = telemetry_data[['metric1', 'metric2', 'metric3']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Use Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.05)
    anomalies = model.fit_predict(scaled_features)

    # Mark anomalies in the telemetry data
    telemetry_data['anomaly'] = anomalies == -1
    anomaly_data = telemetry_data[telemetry_data['anomaly']]

    return jsonify(anomaly_data.to_dict(orient='records'))

# Route to respond to detected threats
@app.route('/respond_to_threats', methods=['POST'])
def respond_to_threats():
    threat_data = request.json.get('threats', [])
    responses = []

    for threat in threat_data:
        # Simulate response actions
        response = {
            'threat_id': threat['id'],
            'action': 'Mitigated',
            'timestamp': pd.Timestamp.now()
        }
        responses.append(response)

    return jsonify({'responses': responses})

# Start the telemetry data collection in a separate thread
def start_data_collection():
    collect_telemetry_data()

if __name__ == '__main__':
    # Start telemetry data collection thread
    data_collection_thread = Thread(target=start_data_collection)
    data_collection_thread.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5002, debug=True)
