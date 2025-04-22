# start_resource_optimizer.py

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import time
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Global variable to store resource usage data
resource_usage_data = pd.DataFrame(columns=['timestamp', 'resource_id', 'usage', 'performance'])

# Function to simulate resource usage data collection
def collect_resource_usage_data():
    global resource_usage_data
    resource_ids = ['Qubit_1', 'Qubit_2', 'Qubit_3', 'Qubit_4']
    while True:
        # Simulate data collection
        for resource_id in resource_ids:
            new_data = {
                'timestamp': pd.Timestamp.now(),
                'resource_id': resource_id,
                'usage': np.random.uniform(0, 100),  # Simulated usage percentage
                'performance': np.random.uniform(0, 1)  # Simulated performance metric
            }
            resource_usage_data = resource_usage_data.append(new_data, ignore_index=True)
        time.sleep(5)  # Collect data every 5 seconds

# Route to get resource usage data
@app.route('/resource_usage', methods=['GET'])
def get_resource_usage():
    return jsonify(resource_usage_data.to_dict(orient='records'))

# Route to optimize resource allocation
@app.route('/optimize_resources', methods=['POST'])
def optimize_resources():
    global resource_usage_data
    if resource_usage_data.empty:
        return jsonify({'status': 'No data available for optimization.'}), 400

    # Prepare data for optimization
    X = resource_usage_data[['usage', 'performance']]
    y = np.random.randint(0, 2, size=len(resource_usage_data))  # Simulated binary allocation outcome (0 or 1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict allocation on the test set
    predictions = model.predict(X_test)
    predictions = [1 if p > 0.5 else 0 for p in predictions]  # Convert to binary

    # Calculate mean squared error for evaluation
    mse = mean_squared_error(y_test, predictions)

    # Simulate optimized resource allocation
    optimized_allocation = {
        'allocated_resources': predictions,
        'mse': mse
    }

    return jsonify({'status': 'Resource optimization completed', 'allocation': optimized_allocation})

# Start the resource usage data collection in a separate thread
def start_data_collection():
    collect_resource_usage_data()

if __name__ == '__main__':
    # Start resource usage data collection thread
    data_collection_thread = Thread(target=start_data_collection)
    data_collection_thread.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5010, debug=True)
