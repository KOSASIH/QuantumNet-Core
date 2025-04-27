import numpy as np
import json
import matplotlib.pyplot as plt

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
        happiness_index = np.random.uniform(0, 1)  # Happiness index between 0 and 1
        data.append({
            'id': i,
            'population': population,
            'technology_level': technology_level,
            'resources': resources,
            'happiness_index': happiness_index,
            'civilization_name': f"Civilization {i}"  # Optional name for the civilization
        })
    return data

def save_civilization_models_to_json(data, filename):
    """Save the generated civilization model data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_civilization_models_from_json(filename):
    """Load civilization model data from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def analyze_civilization_data(data):
    """Analyze the civilization data and return statistical properties."""
    populations = [entry['population'] for entry in data]
    tech_levels = [entry['technology_level'] for entry in data]
    happiness_indices = [entry['happiness_index'] for entry in data]

    mean_population = np.mean(populations)
    mean_tech_level = np.mean(tech_levels)
    mean_happiness = np.mean(happiness_indices)

    return mean_population, mean_tech_level, mean_happiness

def plot_civilization_data(data):
    """Plot the civilization data."""
    ids = [entry['id'] for entry in data]
    populations = [entry['population'] for entry in data]
    tech_levels = [entry['technology_level'] for entry in data]
    happiness_indices = [entry['happiness_index'] for entry in data]

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.bar(ids, populations, color='blue')
    plt.title('Population of Civilizations')
    plt.xlabel('Civilization ID')
    plt.ylabel('Population')

    plt.subplot(3, 1, 2)
    plt.bar(ids, tech_levels, color='green')
    plt.title('Technology Levels of Civilizations')
    plt.xlabel('Civilization ID')
    plt.ylabel('Technology Level')

    plt.subplot(3, 1, 3)
    plt.bar(ids, happiness_indices, color='orange')
    plt.title('Happiness Indices of Civilizations')
    plt.xlabel('Civilization ID')
    plt.ylabel('Happiness Index')

    plt.tight_layout()
    plt.show()

def main():
    num_models = 100  # Number of synthetic civilization models to generate
    filename = 'civilization_models.json'

    # Generate and save synthetic civilization models
    data = generate_civilization_models(num_models)
    save_civilization_models_to_json(data, filename)
    print(f"Generated {num_models} synthetic civilization models and saved to '{filename}'.")

    # Load the data from JSON
    loaded_data = load_civilization_models_from_json(filename)

    # Analyze the loaded data
    mean_population, mean_tech_level, mean_happiness = analyze_civilization_data(loaded_data)
    print(f"Mean Population: {mean_population:.2f}, Mean Technology Level: {mean_tech_level:.2f}, Mean Happiness Index: {mean_happiness:.2f}")

    # Plot the civilization data
    plot_civilization_data(loaded_data)

if __name__ == "__main__":
    main()
