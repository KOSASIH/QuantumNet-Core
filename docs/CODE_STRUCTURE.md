QuantumNet-Core/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── requirements.txt
│
├── docs/
│   ├── index.md
│   ├── installation.md
│   ├── usage.md
│   ├── algorithms.md
│   ├── architecture.md
│   ├── tutorials/
│   │   ├── entanglement_tutorial.md
│   │   ├── quantum_state_tutorial.md
│   │   ├── circuit_tutorial.md
│   │   ├── qml_tutorial.md         # Tutorial QML
│   │   ├── protocol_tutorial.md    # Tutorial protokol quantum
│   │   └── dashboard_tutorial.md   # Tutorial dashboard
│   └── api_reference.md
│
├── src/
│   ├── entanglement/
│   │   ├── __init__.py
│   │   ├── entangler.py
│   │   ├── entanglement_utils.py
│   │   ├── entanglement_tests.py
│   │   └── entanglement_visualization.py
│   ├── quantum_state/
│   │   ├── __init__.py
│   │   ├── state_vector.py
│   │   ├── density_matrix.py
│   │   ├── state_tests.py
│   │   └── state_visualization.py
│   ├── quantum_circuit/
│   │   ├── __init__.py
│   │   ├── circuit.py
│   │   ├── gate_operations.py
│   │   ├── circuit_tests.py
│   │   └── circuit_visualization.py
│   ├── qml/                       # NEW: Quantum Machine Learning
│   │   ├── __init__.py
│   │   ├── entanglement_optimizer.py
│   │   ├── qml_utils.py
│   │   ├── qml_visualization.py
│   │   └── qml_tests.py
│   ├── qnn/                       # NEW: Quantum Neural Network
│   │   ├── __init__.py
│   │   ├── state_predictor.py
│   │   ├── qnn_utils.py
│   │   ├── qnn_visualization.py
│   │   └── qnn_tests.py
│   ├── network/                   # NEW: Network protocols
│   │   ├── __init__.py
│   │   ├── protocols/
│   │   │   ├── __init__.py
│   │   │   ├── qkd_bb84.py
│   │   │   ├── teleportation.py
│   │   │   ├── entanglement_routing.py
│   │   │   ├── protocol_utils.py
│   │   │   └── protocol_tests.py
│   │   ├── p2p_protocol.py
│   │   └── repeater.py
│   ├── error_correction/          # NEW: Quantum Error Correction
│   │   ├── __init__.py
│   │   ├── surface_code.py
│   │   ├── concatenated_code.py
│   │   ├── qec_utils.py
│   │   ├── qec_visualization.py
│   │   └── qec_tests.py
│   ├── consensus/                 # NEW: Quantum Consensus
│   │   ├── __init__.py
│   │   ├── quantum_consensus.py
│   │   ├── voting_protocol.py
│   │   ├── consensus_utils.py
│   │   └── consensus_tests.py
│   ├── dashboard/                 # NEW: Web-based Dashboard
│   │   ├── __init__.py
│   │   ├── backend/
│   │   │   ├── api.py
│   │   │   ├── server.py
│   │   │   └── data_collector.py
│   │   ├── frontend/
│   │   │   ├── static/
│   │   │   ├── templates/
│   │   │   └── app.js
│   │   └── dashboard_tests.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── config.py
│   │   ├── math_utils.py
│   │   ├── file_utils.py
│   │   └── performance_monitor.py
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── qiskit_integration.py
│   │   ├── cirq_integration.py
│   │   └── external_api.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   ├── test_entanglement.py
│   ├── test_quantum_state.py
│   ├── test_quantum_circuit.py
│   ├── test_qml.py                # NEW: Tes untuk QML
│   ├── test_qnn.py                # NEW: Tes untuk QNN
│   ├── test_network.py            # NEW: Tes untuk protokol jaringan
│   ├── test_error_correction.py   # NEW: Tes untuk QEC
│   ├── test_consensus.py          # NEW: Tes untuk konsensus
│   ├── test_dashboard.py          # NEW: Tes untuk dashboard
│   ├── test_utils.py
│   └── test_integration.py
│
├── examples/
│   ├── entanglement_example.py
│   ├── quantum_state_example.py
│   ├── circuit_example.py
│   ├── qml_example.py             # NEW: Contoh penggunaan QML
│   ├── qnn_example.py             # NEW: Contoh penggunaan QNN
│   ├── protocol_example.py        # NEW: Contoh penggunaan protokol
│   ├── qec_example.py             # NEW: Contoh penggunaan QEC
│   ├── consensus_example.py       # NEW: Contoh penggunaan konsensus
│   ├── dashboard_example.py       # NEW: Contoh penggunaan dashboard
│   └── integration_example.py
│
├── benchmarks/
│   ├── benchmark_entanglement.py
│   ├── benchmark_quantum_state.py
│   ├── benchmark_quantum_circuit.py
│   ├── benchmark_qml.py           # NEW: Benchmark QML
│   ├── benchmark_qnn.py           # NEW: Benchmark QNN
│   ├── benchmark_protocols.py     # NEW: Benchmark protokol
│   └── benchmark_qec.py           # NEW: Benchmark QEC
│
├── scripts/
│   ├── setup_environment.py
│   ├── run_tests.py
│   ├── generate_docs.py
│   └── start_dashboard.py         # NEW: Script untuk menjalankan dashboard
│
└── .github/                      # NEW: GitHub configurations
    ├── ISSUE_TEMPLATE.md
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
        ├── test.yml              # CI/CD untuk testing
        └── docs.yml              # CI/CD untuk dokumentasi
