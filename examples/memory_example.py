import numpy as np
import json
import matplotlib.pyplot as plt

def generate_holographic_memory(num_entries, vector_size):
    """Generate synthetic holographic memory data."""
    data = []
    for i in range(num_entries):
        holographic_representation = np.random.rand(vector_size).tolist()  # Random values between 0 and 1
        timestamp = f"2023-10-01T00:00:{i:02d}Z"  # Example timestamp
        metadata = {
            'description': f"Holographic memory entry {i}",
            'category': np.random.choice(['image', 'audio', 'text', 'video']),  # Random category
            'quality': np.random.uniform(0, 1)  # Quality measure between 0 and 1
        }
        data.append({
            'id': i,
            'holographic_representation': holographic_representation,
            'timestamp': timestamp,
            'metadata': metadata
        })
    return data

def save_holographic_memory_to_json(data, filename):
    """Save the generated holographic memory data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_holographic_memory_from_json(filename):
    """Load holographic memory data from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def analyze_holographic_data(data):
    """Analyze the holographic data and return statistical properties."""
    qualities = [entry['metadata']['quality'] for entry in data]
    mean_quality = np.mean(qualities)
    return mean_quality

def plot_holographic_memory(data):
    """Plot the holographic memory data."""
    ids = [entry['id'] for entry in data]
    qualities = [entry['metadata']['quality'] for entry in data]

    plt.figure(figsize=(10, 5))
    plt.bar(ids, qualities, color='purple')
    plt.title('Quality of Holographic Memory Entries')
    plt.xlabel('Entry ID')
    plt.ylabel('Quality')
    plt.xticks(ids, rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    num_entries = 100  # Number of synthetic holographic memory entries to generate
    vector_size = 64   # Size of the holographic representation vector
    filename = 'holographic_data.json'

    # Generate and save synthetic holographic memory data
    data = generate_holographic_memory(num_entries, vector_size)
    save_holographic_memory_to_json(data, filename)
    print(f"Generated {num_entries} synthetic holographic memory entries and saved to '{filename}'.")

    # Load the data from JSON
    loaded_data = load_holographic_memory_from_json(filename)

    # Analyze the loaded data
    mean_quality = analyze_holographic_data(loaded_data)
    print(f"Mean Quality of Holographic Memory Entries: {mean_quality:.4f}")

    # Plot the holographic memory data
    plot_holographic_memory(loaded_data)

if __name__ == "__main__":
    main()
