# benchmark_protocols.py

from flask import Flask, request, jsonify
import numpy as np
import time
from typing import List, Dict

# Initialize Flask app
app = Flask(__name__)

# Simulated database of quantum protocols
protocols_db = {
    'BB84': {
        'description': 'Quantum key distribution protocol.',
        'success_rate': 0.95,
        'latency': 0.1  # Simulated latency in seconds
    },
    'E91': {
        'description': 'Entanglement-based quantum key distribution.',
        'success_rate': 0.90,
        'latency': 0.15  # Simulated latency in seconds
    },
    'QDS': {
        'description': 'Quantum digital signatures protocol.',
        'success_rate': 0.85,
        'latency': 0.2  # Simulated latency in seconds
    }
}

# Route to get available protocols
@app.route('/protocols', methods=['GET'])
def get_protocols():
    return jsonify(protocols_db)

# Route to benchmark a specific protocol
@app.route('/benchmark_protocol', methods=['POST'])
def benchmark_protocol():
    data = request.json
    protocol_name = data.get('protocol_name')

    if protocol_name not in protocols_db:
        return jsonify({'status': 'Protocol not found.'}), 404

    protocol = protocols_db[protocol_name]
    
    # Simulate benchmarking process
    start_time = time.time()
    time.sleep(protocol['latency'])  # Simulate the time taken for the protocol to execute
    end_time = time.time()

    execution_time = end_time - start_time
    success = np.random.rand() < protocol['success_rate']  # Simulate success based on success rate

    return jsonify({
        'protocol_name': protocol_name,
        'execution_time': execution_time,
        'success': success,
        'status': 'Benchmark completed'
    })

# Route to benchmark multiple protocols
@app.route('/benchmark_multiple', methods=['POST'])
def benchmark_multiple():
    data = request.json
    protocol_names = data.get('protocols', [])

    results = []
    for protocol_name in protocol_names:
        if protocol_name not in protocols_db:
            results.append({'protocol_name': protocol_name, 'status': 'Protocol not found.'})
            continue

        protocol = protocols_db[protocol_name]
        
        # Simulate benchmarking process
        start_time = time.time()
        time.sleep(protocol['latency'])  # Simulate the time taken for the protocol to execute
        end_time = time.time()

        execution_time = end_time - start_time
        success = np.random.rand() < protocol['success_rate']  # Simulate success based on success rate

        results.append({
            'protocol_name': protocol_name,
            'execution_time': execution_time,
            'success': success,
            'status': 'Benchmark completed'
        })

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)
