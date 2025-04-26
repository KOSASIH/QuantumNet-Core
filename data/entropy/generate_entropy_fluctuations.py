import numpy as np
import json
from datetime import datetime, timedelta

def generate_entropy_fluctuations(num_entries, start_time, time_interval):
    """Generate synthetic entropy fluctuation data."""
    data = []
    current_time = start_time
    for i in range(num_entries):
        # Generate a random entropy value (for example, between 0 and 2)
        entropy_value = np.random.uniform(0, 2)
        data.append({
            'id': i,
            'timestamp': current_time.isoformat(),  # ISO 8601 format
            'entropy_value': entropy_value,
            'fluctuation': np.random.normal(0, 0.1)  # Random fluctuation around the entropy value
        })
        current_time += time_interval  # Increment time by the specified interval
    return data

def save_entropy_fluctuations_to_json(data, filename):
    """Save the generated entropy fluctuation data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    num_entries = 1000  # Number of synthetic entries to generate
    start_time = datetime(2023, 10, 1)  # Starting time for the data
    time_interval = timedelta(seconds=1)  # Time interval between entries
    data = generate_entropy_fluctuations(num_entries, start_time, time_interval)
    save_entropy_fluctuations_to_json(data, 'entropy/entropy_fluctuations.json')
    print(f"Generated {num_entries} entries of synthetic entropy fluctuations and saved to 'entropy/entropy_fluctuations.json'.")

if __name__ == "__main__":
    main()
