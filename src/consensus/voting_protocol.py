import numpy as np
from quantum_consensus import QuantumConsensus
import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EntanglementVotingProtocol:
    def __init__(self, num_participants, threshold=0.5):
        self.consensus = QuantumConsensus(num_participants, threshold)
        self.entangled_states = np.zeros(num_participants, dtype=int)  # Initialize entangled states

    def entangle_participants(self):
        """Simulate entanglement between participants."""
        # For simplicity, we randomly assign entangled states (0 or 1)
        self.entangled_states = np.random.choice([0, 1], size=self.consensus.num_participants)
        logging.info(f"Participants are entangled with states: {self.entangled_states}")

    def cast_entangled_vote(self, participant_id, vote):
        """Cast a vote using entanglement."""
        self.entangle_participants()
        # Modify the vote based on the entangled state
        if self.entangled_states[participant_id] == 1:
            vote = 1  # If entangled state is 1, force vote to 1
        self.consensus.cast_vote(participant_id, vote)
        logging.info(f"Participant {participant_id} cast entangled vote: {vote}")

    def tally_votes(self):
        """Tally the votes from the consensus mechanism."""
        return self.consensus.tally_votes()

    def consensus_reached(self):
        """Check if consensus is reached."""
        return self.consensus.consensus_reached()

    def visualize_votes(self):
        """Visualize the voting results."""
        plt.bar(range(self.consensus.num_participants), self.consensus.votes, color='blue', alpha=0.7, label='Votes')
        plt.axhline(y=self.consensus.threshold * np.sum(self.consensus.weights), color='r', linestyle='--', label='Consensus Threshold')
        plt.title('Voting Results with Entanglement')
        plt.xlabel('Participants')
        plt.ylabel('Votes')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    voting_protocol = EntanglementVotingProtocol(num_participants=5, threshold=0.6)
    voting_protocol.consensus.set_weights([1, 1, 1, 2, 1])  # Set weights for participants
    voting_protocol.cast_entangled_vote(0, 1)
    voting_protocol.cast_entangled_vote(1, 1)
    voting_protocol.cast_entangled_vote(2, 0)
    voting_protocol.cast_entangled_vote(3, 1)
    voting_protocol.cast_entangled_vote(4, 0)

    print("Total Weighted Votes:", voting_protocol.tally_votes())
    print("Consensus Reached:", voting_protocol.consensus_reached())
    voting_protocol.visualize_votes()
