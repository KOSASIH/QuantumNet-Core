# utils/config.py

import json
import os

class ConfigManager:
    """Class for managing configuration settings."""
    
    def __init__(self, config_file):
        """Initializes the ConfigManager with a configuration file.
        
        Args:
            config_file (str): Path to the configuration file.
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Loads the configuration from the specified file.
        
        Returns:
            dict: Configuration settings.
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def get(self, key, default=None):
        """Gets a configuration value by key.
        
        Args:
            key (str): The key of the configuration setting.
            default: The default value to return if the key is not found.
        
        Returns:
            The configuration value or default if not found.
        """
        return self.config.get(key, default)

# Example usage
if __name__ == "__main__":
    config = ConfigManager("config.json")
    print(config.get("some_setting", "default_value"))
