import numpy as np
import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumConsensus:
    def __init__(self, num_participants, threshold=0.5):
        self.num_participants = num_participants
        self.votes = np.zeros(num_participants, dtype=int)  # Initialize votes
        self.weights = np.ones(num_participants, dtype=float)  # Default weights
        self.threshold = threshold  # Consensus threshold

    def set_weights(self, weights):
        """Set the weights for each participant."""
        if len(weights) != self.num_participants:
            raise ValueError("Weights must match the number of participants.")
        self.weights = np.array(weights, dtype=float)

    def cast_vote(self, participant_id, vote):
        """Cast a vote from a participant."""
        if participant_id < 0 or participant_id >= self.num_participants:
            raise ValueError("Invalid participant ID.")
        if vote not in [0, 1]:
            raise ValueError("Vote must be 0 or 1.")
        self.votes[participant_id] = vote
        logging.info(f"Participant {participant_id} cast vote: {vote}")

    def tally_votes(self):
        """Tally the votes and return the weighted result."""
        total_votes = np.sum(self.votes * self.weights)
        logging.info(f"Tallying votes: {total_votes} out of {np.sum(self.weights)}")
        return total_votes

    def consensus_reached(self):
        """Check if consensus is reached based on the configured threshold."""
        total_weighted_votes = self.tally_votes()
        required_votes = self.threshold * np.sum(self.weights)
        logging.info(f"Consensus check: {total_weighted_votes} >= {required_votes}")
        return total_weighted_votes >= required_votes

    def visualize_votes(self):
        """Visualize the voting results."""
        plt.bar(range(self.num_participants), self.votes, color='blue', alpha=0.7, label='Votes')
        plt.bar(range(self.num_participants), self.weights, color='orange', alpha=0.5, label='Weights')
        plt.axhline(y=self.threshold * np.sum(self.weights), color='r', linestyle='--', label='Consensus Threshold')
        plt.title('Voting Results')
        plt.xlabel('Participants')
        plt.ylabel('Votes / Weights')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    consensus = QuantumConsensus(num_participants=5, threshold=0.6)
    consensus.set_weights([1, 1, 1, 2, 1])  # Set weights for participants
    consensus.cast_vote(0, 1)
    consensus.cast_vote(1, 1)
    consensus.cast_vote(2, 0)
    consensus.cast_vote(3, 1)
    consensus.cast_vote(4, 0)

    print("Total Weighted Votes:", consensus.tally_votes())
    print("Consensus Reached:", consensus.consensus_reached())
    consensus.visualize_votes()
