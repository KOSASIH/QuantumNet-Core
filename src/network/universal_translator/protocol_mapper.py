"""
Protocol Mapper for Quantum Universal Translator
"""
import json
import os

class ProtocolMapper:
    def __init__(self, protocol_file: str):
        """
        Initialize the protocol mapper.

        Parameters:
        protocol_file (str): Path to the JSON file containing protocol mappings.
        """
        if not os.path.exists(protocol_file):
            raise FileNotFoundError(f"Protocol file '{protocol_file}' not found.")
        self.protocols = self.load_protocols(protocol_file)

    def load_protocols(self, protocol_file: str) -> dict:
        """Load protocols from a JSON file."""
        with open(protocol_file, 'r') as file:
            try:
                protocols = json.load(file)
                if not isinstance(protocols, dict):
                    raise ValueError("Protocol file must contain a JSON object.")
                return protocols
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")

    def map_protocol(self, protocol_name: str) -> str:
        """
        Map a protocol to its universal representation.

        Parameters:
        protocol_name (str): The name of the protocol to map.

        Returns:
        str: The universal representation of the protocol.
        """
        mapped_protocol = self.protocols.get(protocol_name)
        if mapped_protocol is None:
            raise ValueError(f"Protocol '{protocol_name}' not found in the mapping.")
        return mapped_protocol

    def add_protocol(self, protocol_name: str, universal_representation: str) -> None:
        """
        Add a new protocol mapping.

        Parameters:
        protocol_name (str): The name of the protocol to add.
        universal_representation (str): The universal representation of the protocol.
        """
        if protocol_name in self.protocols:
            raise ValueError(f"Protocol '{protocol_name}' already exists.")
        self.protocols[protocol_name] = universal_representation

    def save_protocols(self, protocol_file: str) -> None:
        """
        Save the current protocols to a JSON file.

        Parameters:
        protocol_file (str): Path to the JSON file to save protocols.
        """
        with open(protocol_file, 'w') as file:
            json.dump(self.protocols, file, indent=4)

# Example usage:
if __name__ == "__main__":
    protocol_file_path = 'protocols.json'  # Path to your JSON file
    mapper = ProtocolMapper(protocol_file_path)

    # Map a protocol
    try:
        protocol_name = "example_protocol"
        universal_representation = mapper.map_protocol(protocol_name)
        print(f"Universal representation of '{protocol_name}': {universal_representation}")
    except ValueError as e:
        print(e)

    # Add a new protocol
    try:
        mapper.add_protocol("new_protocol", "universal_representation_for_new_protocol")
        mapper.save_protocols(protocol_file_path)  # Save updated protocols
        print("New protocol added successfully.")
    except ValueError as e:
        print(e)
