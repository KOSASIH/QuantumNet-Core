"""
Utility functions for the Autonomous Quantum Diplomacy Engine (AQDE).
This module provides functions for data preprocessing, strategy evaluation,
sentiment analysis, and logging to enhance the functionality of the AQDE.
"""

import numpy as np
import logging
from datetime import datetime
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AQDEUtils:
    def __init__(self):
        """
        Initialize the AQDE Utilities with sentiment analysis capabilities.
        """
        self.sentiment_model = pipeline("sentiment-analysis")

    def preprocess_data(self, data: list) -> np.ndarray:
        """
        Preprocess input data for analysis.

        Args:
            data (list): The input data to preprocess.

        Returns:
            np.ndarray: The preprocessed data as a NumPy array.
        """
        # Convert to NumPy array and normalize
        data_array = np.array(data)
        normalized_data = (data_array - np.min(data_array)) / (np.max(data_array) - np.min(data_array))
        return normalized_data

    def evaluate_strategy(self, strategy: np.ndarray, opponent_moves: np.ndarray) -> float:
        """
        Evaluate the effectiveness of a given strategy against opponent moves.

        Args:
            strategy (np.ndarray): The strategy to evaluate.
            opponent_moves (np.ndarray): The moves of the opponent.

        Returns:
            float: The evaluation score of the strategy.
        """
        # Simple evaluation logic (can be enhanced)
        score = np.sum(strategy * opponent_moves)  # Dot product as a score
        return score

    def analyze_sentiment(self, message: str) -> str:
        """
        Analyze the sentiment of a given message.

        Args:
            message (str): The message to analyze.

        Returns:
            str: The sentiment analysis result.
        """
        sentiment = self.sentiment_model(message)[0]
        return f"Sentiment: {sentiment['label']}, Score: {sentiment['score']:.2f}"

    def log_interaction(self, entity_name: str, opponent_name: str, outcome: str):
        """
        Log the details of a diplomatic interaction.

        Args:
            entity_name (str): The name of the entity involved.
            opponent_name (str): The name of the opponent entity.
            outcome (str): The outcome of the interaction.
        """
        logging.info(f"Interaction logged: {entity_name} vs {opponent_name} - Outcome: {outcome}")

    def save_results(self, results: dict, filename: str):
        """
        Save the results of simulations to a file.

        Args:
            results (dict): The results to save.
            filename (str): The name of the file to save the results to.
        """
        with open(filename, 'w') as file:
            for key, value in results.items():
                file.write(f"{key}: {value}\n")
        logging.info(f"Results saved to {filename}")

# Example usage
if __name__ == "__main__":
    utils = AQDEUtils()

    # Preprocess data
    raw_data = [1, 2, 3, 4, 5]
    processed_data = utils.preprocess_data(raw_data)
    print("Processed Data:", processed_data)

    # Evaluate strategy
    strategy = np.array([0.5, 0.3, 0.2])
    opponent_moves = np.array([0.4, 0.4, 0.2])
    score = utils.evaluate_strategy(strategy, opponent_moves)
    print("Strategy Evaluation Score:", score)

    # Analyze sentiment
    message = "I am very happy with the results!"
    sentiment_result = utils.analyze_sentiment(message)
    print(sentiment_result)

    # Log interaction
    utils.log_interaction("Human", "Alien", "Mutual Cooperation")

    # Save results
    results = {"Human": "Win", "Alien": "Loss"}
    utils.save_results(results, "diplomacy_results.txt")
