# benchmark_qec.py

from flask import Flask, request, jsonify
import numpy as np
import time

# Initialize Flask app
app = Flask(__name__)

# Simulated database of quantum error correction codes
qec_codes_db = {
    'Shor': {
        'description': 'Shor’s error correction code.',
        'success_rate': 0.95,
        'latency': 0.1  # Simulated latency in seconds
    },
    'Steane': {
        'description': 'Steane’s error correction code.',
        'success_rate': 0.90,
        'latency': 0.15  # Simulated latency in seconds
    },
    'Surface': {
        'description': 'Surface code for error correction.',
        'success_rate': 0.85,
        'latency': 0.2  # Simulated latency in seconds
    }
}

# Route to get available QEC codes
@app.route('/qec_codes', methods=['GET'])
def get_qec_codes():
    return jsonify(qec_codes_db)

# Route to benchmark a specific QEC code
@app.route('/benchmark_qec', methods=['POST'])
def benchmark_qec():
    data = request.json
    qec_code_name = data.get('qec_code_name')

    if qec_code_name not in qec_codes_db:
        return jsonify({'status': 'QEC code not found.'}), 404

    qec_code = qec_codes_db[qec_code_name]
    
    # Simulate benchmarking process
    start_time = time.time()
    time.sleep(qec_code['latency'])  # Simulate the time taken for the QEC code to execute
    end_time = time.time()

    execution_time = end_time - start_time
    success = np.random.rand() < qec_code['success_rate']  # Simulate success based on success rate

    return jsonify({
        'qec_code_name': qec_code_name,
        'execution_time': execution_time,
        'success': success,
        'status': 'Benchmark completed'
    })

# Route to benchmark multiple QEC codes
@app.route('/benchmark_multiple_qec', methods=['POST'])
def benchmark_multiple_qec():
    data = request.json
    qec_code_names = data.get('qec_codes', [])

    results = []
    for qec_code_name in qec_code_names:
        if qec_code_name not in qec_codes_db:
            results.append({'qec_code_name': qec_code_name, 'status': 'QEC code not found.'})
            continue

        qec_code = qec_codes_db[qec_code_name]
        
        # Simulate benchmarking process
        start_time = time.time()
        time.sleep(qec_code['latency'])  # Simulate the time taken for the QEC code to execute
        end_time = time.time()

        execution_time = end_time - start_time
        success = np.random.rand() < qec_code['success_rate']  # Simulate success based on success rate

        results.append({
            'qec_code_name': qec_code_name,
            'execution_time': execution_time,
            'success': success,
            'status': 'Benchmark completed'
        })

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5013, debug=True)
