# integration/external_api.py

import requests

class ExternalAPI:
    """Class for interacting with external APIs."""
    
    def __init__(self, base_url):
        """Initializes the ExternalAPI with a base URL.
        
        Args:
            base_url (str): The base URL for the external API.
        """
        self.base_url = base_url

    def get_data(self, endpoint):
        """Retrieves data from the specified endpoint.
        
        Args:
            endpoint (str): The API endpoint to retrieve data from.
        
        Returns:
            dict: The JSON response from the API.
        
        Raises:
            requests.RequestException: If the request fails.
        """
        response = requests.get(f"{self.base_url}/{endpoint}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def post_data(self, endpoint, data):
        """Sends data to the specified endpoint.
        
        Args:
            endpoint (str): The API endpoint to send data to.
            data (dict): The data to send in the request body.
        
        Returns:
            dict: The JSON response from the API.
        
        Raises:
            requests.RequestException: If the request fails.
        """
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

# Example usage
if __name__ == "__main__":
    api = ExternalAPI("https://api.example.com")
    try:
        data = api.get_data("data_endpoint")
        print("Retrieved data:", data)
        
        response = api.post_data("data_endpoint", {"key": "value"})
        print("Response from POST:", response)
    except requests.RequestException as e:
        print("An error occurred:", e)
