"""
Utility Functions for Intergalactic Protocol Adaptation (IPA)
"""
import numpy as np
import json
from typing import List, Dict, Any

def load_protocols(file_path: str) -> List[Dict[str, Any]]:
    """
    Load protocols from a JSON file.

    Parameters:
    file_path (str): Path to the JSON file containing protocol definitions.

    Returns:
    List[Dict[str, Any]]: A list of protocol definitions.
    """
    with open(file_path, 'r') as file:
        protocols = json.load(file)
    return protocols

def adapt_protocol(protocol: Dict[str, Any], adaptation_rules: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adapt a given protocol based on specified adaptation rules.

    Parameters:
    protocol (Dict[str, Any]): The original protocol to adapt.
    adaptation_rules (Dict[str, Any]): Rules defining how to adapt the protocol.

    Returns:
    Dict[str, Any]: The adapted protocol.
    """
    adapted_protocol = protocol.copy()
    for key, value in adaptation_rules.items():
        if key in adapted_protocol:
            adapted_protocol[key] = value
    return adapted_protocol

def calculate_performance_metrics(results: Dict[str, int]) -> Dict[str, float]:
    """
    Calculate performance metrics from simulation results.

    Parameters:
    results (Dict[str, int]): The measurement results.

    Returns:
    Dict[str, float]: A dictionary containing performance metrics.
    """
    total_shots = sum(results.values())
    metrics = {
        'success_rate': results.get('success', 0) / total_shots if total_shots > 0 else 0,
        'failure_rate': results.get('failure', 0) / total_shots if total_shots > 0 else 0,
        'total_shots': total_shots
    }
    return metrics

def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Process raw data for analysis.

    Parameters:
    data (List[Dict[str, Any]]): Raw data to process.

    Returns:
    List[Dict[str, Any]]: Processed data ready for analysis.
    """
    processed_data = []
    for entry in data:
        processed_entry = {
            'protocol_id': entry['id'],
            'adapted': adapt_protocol(entry['protocol'], entry.get('adaptation_rules', {})),
            'metrics': calculate_performance_metrics(entry['results'])
        }
        processed_data.append(processed_entry)
    return processed_data

def save_results(results: List[Dict[str, Any]], file_path: str):
    """
    Save results to a JSON file.

    Parameters:
    results (List[Dict[str, Any]]): Results to save.
    file_path (str): Path to the output JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)

# Example usage:
if __name__ == "__main__":
    protocols = load_protocols('protocols.json')
    adaptation_rules = {'timeout': 300, 'max_retries': 5}
    
    adapted_protocols = [adapt_protocol(protocol, adaptation_rules) for protocol in protocols]
    results = [{'id': protocol['id'], 'results': {'success': 80, 'failure': 20}} for protocol in adapted_protocols]
    
    processed_results = process_data(results)
    save_results(processed_results, 'adapted_results.json')
