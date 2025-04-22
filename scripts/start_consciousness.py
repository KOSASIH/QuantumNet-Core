# start_consciousness.py

from flask import Flask, request, jsonify
import numpy as np
import random
import time
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Global variable to store experiences
experiences = []

# Function to simulate cognitive processing
def cognitive_processing():
    global experiences
    while True:
        # Simulate a new experience
        new_experience = {
            'timestamp': time.time(),
            'decision': random.choice(['action_a', 'action_b']),
            'outcome': random.choice(['success', 'failure'])
        }
        experiences.append(new_experience)
        time.sleep(5)  # Process new experiences every 5 seconds

# Route to get current experiences
@app.route('/experiences', methods=['GET'])
def get_experiences():
    return jsonify(experiences)

# Route to simulate decision-making based on experiences
@app.route('/make_decision', methods=['POST'])
def make_decision():
    global experiences
    if not experiences:
        return jsonify({'status': 'No experiences available for decision-making.'}), 400

    # Analyze past experiences to make a decision
    success_count = sum(1 for exp in experiences if exp['outcome'] == 'success')
    failure_count = len(experiences) - success_count

    # Simple decision-making logic
    if success_count > failure_count:
        decision = 'action_a'  # Favor action_a if more successes
    else:
        decision = 'action_b'  # Favor action_b otherwise

    return jsonify({'decision': decision})

# Route to simulate learning from experiences
@app.route('/learn', methods=['POST'])
def learn():
    global experiences
    if not experiences:
        return jsonify({'status': 'No experiences available for learning.'}), 400

    # Simulate learning process
    learning_rate = 0.1
    success_rate = sum(1 for exp in experiences if exp['outcome'] == 'success') / len(experiences)
    adjusted_success_rate = success_rate * (1 + learning_rate)

    return jsonify({'adjusted_success_rate': adjusted_success_rate})

# Start the cognitive processing in a separate thread
def start_cognitive_processing():
    cognitive_processing()

if __name__ == '__main__':
    # Start cognitive processing thread
    cognitive_thread = Thread(target=start_cognitive_processing)
    cognitive_thread.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5011, debug=True)
