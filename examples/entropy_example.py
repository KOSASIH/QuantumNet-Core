import numpy as np
import json
import matplotlib.pyplot as plt

def generate_entropy_fluctuations(num_entries):
    """Generate synthetic entropy fluctuation data."""
    data = []
    for i in range(num_entries):
        entropy_value = np.random.uniform(0, 2)  # Random entropy value between 0 and 2
        fluctuation = np.random.normal(0, 0.1)  # Random fluctuation around the entropy value
        data.append({
            'id': i,
            'entropy_value': entropy_value,
            'fluctuation': fluctuation
        })
    return data

def save_entropy_fluctuations_to_json(data, filename):
    """Save the generated entropy fluctuation data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_entropy_fluctuations_from_json(filename):
    """Load entropy fluctuation data from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def analyze_entropy_data(data):
    """Analyze the entropy data and return statistical properties."""
    entropy_values = [entry['entropy_value'] for entry in data]
    mean_entropy = np.mean(entropy_values)
    std_entropy = np.std(entropy_values)
    return mean_entropy, std_entropy

def plot_entropy_fluctuations(data):
    """Plot the entropy fluctuations."""
    ids = [entry['id'] for entry in data]
    entropy_values = [entry['entropy_value'] for entry in data]
    fluctuations = [entry['fluctuation'] for entry in data]

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(ids, entropy_values, label='Entropy Values', color='blue')
    plt.title('Entropy Values Over Time')
    plt.xlabel('Entry ID')
    plt.ylabel('Entropy Value')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(ids, fluctuations, label='Fluctuations', color='red')
    plt.title('Entropy Fluctuations Over Time')
    plt.xlabel('Entry ID')
    plt.ylabel('Fluctuation')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    num_entries = 1000  # Number of synthetic entries to generate
    filename = 'entropy_fluctuations.json'

    # Generate and save synthetic entropy fluctuations
    data = generate_entropy_fluctuations(num_entries)
    save_entropy_fluctuations_to_json(data, filename)
    print(f"Generated {num_entries} synthetic entropy fluctuations and saved to '{filename}'.")

    # Load the data from JSON
    loaded_data = load_entropy_fluctuations_from_json(filename)

    # Analyze the loaded data
    mean_entropy, std_entropy = analyze_entropy_data(loaded_data)
    print(f"Mean Entropy: {mean_entropy:.4f}, Standard Deviation: {std_entropy:.4f}")

    # Plot the entropy fluctuations
    plot_entropy_fluctuations(loaded_data)

if __name__ == "__main__":
    main()
