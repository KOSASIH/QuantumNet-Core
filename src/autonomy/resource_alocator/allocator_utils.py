import random
import logging
import numpy as np

# Set up logging
logging.basicConfig(level=logging.INFO)

def generate_random_resources(num_resources, resource_types=None, distribution='uniform'):
    """Generate a random list of resources.

    :param num_resources: Number of resources to generate.
    :param resource_types: Optional list of resource types (e.g., ['CPU', 'Memory']).
    :param distribution: Distribution type ('uniform' or 'normal').
    :return: Dictionary of resources with random values.
    """
    if resource_types is None:
        resource_types = ['CPU', 'Memory', 'Bandwidth']

    resources = {}
    for resource in resource_types:
        if distribution == 'uniform':
            resources[resource] = random.randint(1, 100)
        elif distribution == 'normal':
            resources[resource] = max(1, int(np.random.normal(50, 15)))  # Mean 50, stddev 15
        else:
            logging.error("Invalid distribution type. Use 'uniform' or 'normal'.")
            raise ValueError("Invalid distribution type. Use 'uniform' or 'normal'.")

    logging.info(f"Generated resources: {resources}")
    return resources

def calculate_utilization(resources):
    """Calculate the utilization of resources.

    :param resources: Dictionary of resource usage.
    :return: Dictionary of utilization metrics (total, average, max, min).
    """
    if not resources:
        logging.warning("No resources provided for utilization calculation.")
        return {'total': 0, 'average': 0, 'max': 0, 'min': 0}

    total = sum(resources.values())
    average = total / len(resources)
    max_utilization = max(resources.values())
    min_utilization = min(resources.values())

    utilization_metrics = {
        'total': total,
        'average': average,
        'max': max_utilization,
        'min': min_utilization
    }

    logging.info(f"Calculated utilization metrics: {utilization_metrics}")
    return utilization_metrics

def round_robin_allocation(resources, num_allocations):
    """Allocate resources using a round-robin strategy.

    :param resources: Dictionary of available resources.
    :param num_allocations: Number of allocations to perform.
    :return: List of allocations.
    """
    allocations = []
    resource_keys = list(resources.keys())
    for i in range(num_allocations):
        resource_key = resource_keys[i % len(resource_keys)]
        allocations.append((resource_key, resources[resource_key]))
    
    logging.info(f"Round-robin allocations: {allocations}")
    return allocations

def weighted_allocation(resources, weights):
    """Allocate resources based on provided weights.

    :param resources: Dictionary of available resources.
    :param weights: Dictionary of weights corresponding to each resource.
    :return: List of weighted allocations.
    """
    total_weight = sum(weights.values())
    allocations = []
    
    for resource in resources:
        allocation = (resource, resources[resource] * (weights[resource] / total_weight))
        allocations.append(allocation)

    logging.info(f"Weighted allocations: {allocations}")
    return allocations

# Example usage
if __name__ == "__main__":
    # Generate random resources
    resources = generate_random_resources(5, resource_types=['CPU', 'Memory', 'Bandwidth'], distribution='normal')
    
    # Calculate utilization
    utilization_metrics = calculate_utilization(resources)
    print(utilization_metrics)
    
    # Perform round-robin allocation
    round_robin_allocations = round_robin_allocation(resources, 10)
    print(round_robin_allocations)
    
    # Perform weighted allocation
    weights = {'CPU': 0.5, 'Memory': 0.3, 'Bandwidth': 0.2}
    weighted_allocations = weighted_allocation(resources, weights)
    print(weighted_allocations)
