import numpy as np
import json

def generate_civilization_models(num_models):
    """Generate synthetic civilization model data."""
    data = []
    for i in range(num_models):
        population = np.random.randint(1000, 100000)  # Random population between 1,000 and 100,000
        technology_level = np.random.uniform(0, 1)  # Technology level between 0 (primitive) and 1 (advanced)
        resources = {
            'food': np.random.randint(1000, 10000),  # Random food resources
            'water': np.random.randint(1000, 10000),  # Random water resources
            'energy': np.random.randint(1000, 10000)  # Random energy resources
        }
        data.append({
            'id': i,
            'population': population,
            'technology_level': technology_level,
            'resources': resources,
            'happiness_index': np.random.uniform(0, 1),  # Happiness index between 0 and 1
            'civilization_name': f"Civilization {i}"  # Optional name for the civilization
        })
    return data

def save_civilization_models_to_json(data, filename):
    """Save the generated civilization model data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    num_models = 100  # Number of synthetic civilization models to generate
    data = generate_civilization_models(num_models)
    save_civilization_models_to_json(data, 'civilization/civilization_models.json')
    print(f"Generated {num_models} synthetic civilization models and saved to 'civilization/civilization_models.json'.")

if __name__ == "__main__":
    main()
