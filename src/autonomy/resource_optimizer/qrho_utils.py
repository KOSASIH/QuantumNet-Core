"""
Utility Functions for Quantum Resource Hyper-Optimizer (QRHO).
"""
import numpy as np

def normalize_resource_allocation(allocation: dict) -> dict:
    """
    Normalize resource allocation to ensure it fits within limits.

    Parameters:
    allocation (dict): Resource allocation to normalize.

    Returns:
    dict: Normalized resource allocation.
    """
    total = sum(allocation.values())
    if total == 0:
        return {k: 0 for k in allocation}  # Return zero allocation if total is zero
    return {k: v / total for k, v in allocation.items()}

def calculate_resource_efficiency(allocation: dict, demand: dict) -> float:
    """
    Calculate the efficiency of resource allocation.

    Parameters:
    allocation (dict): Current resource allocation.
    demand (dict): Demand for resources.

    Returns:
    float: Efficiency score (0 to 1).
    """
    total_allocated = sum(allocation.values())
    total_demanded = sum(demand.values())
    return total_allocated / total_demanded if total_demanded > 0 else 0

def calculate_resource_shortfall(allocation: dict, demand: dict) -> dict:
    """
    Calculate the shortfall of resources based on demand.

    Parameters:
    allocation (dict): Current resource allocation.
    demand (dict): Demand for resources.

    Returns:
    dict: Shortfall of resources.
    """
    return {k: max(0, demand.get(k, 0) - allocation.get(k, 0)) for k in demand}

def calculate_resource_surplus(allocation: dict, demand: dict) -> dict:
    """
    Calculate the surplus of resources based on demand.

    Parameters:
    allocation (dict): Current resource allocation.
    demand (dict): Demand for resources.

    Returns:
    dict: Surplus of resources.
    """
    return {k: max(0, allocation.get(k, 0) - demand.get(k, 0)) for k in allocation}

def aggregate_resource_allocations(allocations: list) -> dict:
    """
    Aggregate multiple resource allocations into a single allocation.

    Parameters:
    allocations (list): List of resource allocation dictionaries.

    Returns:
    dict: Aggregated resource allocation.
    """
    aggregated = {}
    for allocation in allocations:
        for k, v in allocation.items():
            if k in aggregated:
                aggregated[k] += v
            else:
                aggregated[k] = v
    return aggregated

# Example usage:
if __name__ == "__main__":
    allocation = {'qubits': 5, 'gates': 10}
    demand = {'qubits': 8, 'gates': 7}

    # Normalize allocation
    normalized_allocation = normalize_resource_allocation(allocation)
    print("Normalized Allocation:", normalized_allocation)

    # Calculate efficiency
    efficiency = calculate_resource_efficiency(allocation, demand)
    print("Resource Efficiency:", efficiency)

    # Calculate shortfall
    shortfall = calculate_resource_shortfall(allocation, demand)
    print("Resource Shortfall:", shortfall)

    # Calculate surplus
    surplus = calculate_resource_surplus(allocation, demand)
    print("Resource Surplus:", surplus)

    # Aggregate allocations
    allocations = [{'qubits': 3, 'gates': 5}, {'qubits': 2, 'gates': 4}]
    aggregated_allocation = aggregate_resource_allocations(allocations)
    print("Aggregated Allocation:", aggregated_allocation)
