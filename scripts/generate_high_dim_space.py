import numpy as np
import json

def generate_high_dimensional_data(num_points, num_dimensions):
    """Generate synthetic higher-dimensional space data."""
    data = []
    for i in range(num_points):
        # Generate random coordinates in the specified number of dimensions
        coordinates = np.random.rand(num_dimensions).tolist()  # Random values between 0 and 1
        data.append({
            'id': i,
            'coordinates': coordinates,
            'magnitude': np.linalg.norm(coordinates),  # Calculate the magnitude of the point
            'label': f"Point {i}"  # Optional label for the point
        })
    return data

def save_high_dimensional_data_to_json(data, filename):
    """Save the generated high-dimensional data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    num_points = 1000  # Number of synthetic points to generate
    num_dimensions = 10  # Number of dimensions for each point
    data = generate_high_dimensional_data(num_points, num_dimensions)
    save_high_dimensional_data_to_json(data, 'dimensional/high_dim_spaces.json')
    print(f"Generated {num_points} points in {num_dimensions}-dimensional space and saved to 'dimensional/high_dim_spaces.json'.")

if __name__ == "__main__":
    main()
