# start_orchestrator.py

from flask import Flask, request, jsonify
import numpy as np
import json
import time
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Global variables to simulate quantum resources and tasks
quantum_resources = {
    'nodes': [
        {'id': 'node_1', 'status': 'available'},
        {'id': 'node_2', 'status': 'available'},
        {'id': 'node_3', 'status': 'busy'},
    ],
    'tasks': []
}

# Function to simulate task execution on a quantum node
def execute_task_on_node(node_id, task):
    print(f"Executing task {task['id']} on {node_id}...")
    time.sleep(np.random.uniform(1, 3))  # Simulate execution time
    print(f"Task {task['id']} completed on {node_id}.")
    return {'task_id': task['id'], 'result': np.random.random()}

# Route to get the status of quantum nodes
@app.route('/nodes', methods=['GET'])
def get_nodes():
    return jsonify(quantum_resources['nodes'])

# Route to submit a new quantum task
@app.route('/submit_task', methods=['POST'])
def submit_task():
    task = request.json
    task_id = len(quantum_resources['tasks']) + 1
    task['id'] = f'task_{task_id}'
    quantum_resources['tasks'].append(task)
    return jsonify({'status': 'Task submitted', 'task_id': task['id']})

# Route to execute tasks on available nodes
@app.route('/execute_tasks', methods=['POST'])
def execute_tasks():
    results = []
    for task in quantum_resources['tasks']:
        available_node = next((node for node in quantum_resources['nodes'] if node['status'] == 'available'), None)
        if available_node:
            available_node['status'] = 'busy'  # Mark node as busy
            result = execute_task_on_node(available_node['id'], task)
            results.append(result)
            available_node['status'] = 'available'  # Mark node as available again
        else:
            print("No available nodes to execute the task.")
    return jsonify({'results': results})

# Route to get the status of submitted tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(quantum_resources['tasks'])

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
