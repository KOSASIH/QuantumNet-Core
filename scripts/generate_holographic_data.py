import numpy as np
import json

def generate_holographic_memory(num_entries, vector_size):
    """Generate synthetic holographic memory data."""
    data = []
    for i in range(num_entries):
        # Generate a random holographic representation as a vector
        holographic_representation = np.random.rand(vector_size).tolist()  # Random values between 0 and 1
        data.append({
            'id': i,
            'holographic_representation': holographic_representation,
            'timestamp': f"2023-10-01T00:00:0{i}:00Z",  # Example timestamp
            'metadata': {
                'description': f"Holographic memory entry {i}",
                'category': np.random.choice(['image', 'audio', 'text', 'video']),  # Random category
                'quality': np.random.uniform(0, 1)  # Quality measure between 0 and 1
            }
        })
    return data

def save_holographic_memory_to_json(data, filename):
    """Save the generated holographic memory data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    num_entries = 1000  # Number of synthetic holographic memory entries to generate
    vector_size = 64  # Size of the holographic representation vector
    data = generate_holographic_memory(num_entries, vector_size)
    save_holographic_memory_to_json(data, 'memory/holographic_data.json')
    print(f"Generated {num_entries} synthetic holographic memory entries and saved to 'memory/holographic_data.json'.")

if __name__ == "__main__":
    main()
