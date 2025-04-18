# utils/file_utils.py

import json

defread_json(file_path):
    """Reads a JSON file and returns its contents.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        dict: The contents of the JSON file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json(file_path, data):
    """Writes data to a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        data (dict): The data to write to the file.
    
    Raises:
        IOError: If the file cannot be written.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
if __name__ == "__main__":
    data = {"key": "value"}
    write_json("output.json", data)
    read_data = read_json("output.json")
    print("Read data:", read_data)
