import unittest
import numpy as np
from quantum_consensus import QuantumConsensus
from voting_protocol import EntanglementVotingProtocol
from consensus_utils import simulate_voting_with_errors

class TestQuantumConsensus(unittest.TestCase):
    
    def test_cast_vote(self):
        consensus = QuantumConsensus(num_participants=3)
        consensus.cast_vote(0, 1)
        self.assertEqual(consensus.votes[0], 1)

        with self.assertRaises(ValueError):
            consensus.cast_vote(3, 1)  # Invalid participant ID
        with self.assertRaises(ValueError):
            consensus.cast_vote(1, 2)  # Invalid vote

    def test_tally_votes(self):
        consensus = QuantumConsensus(num_participants=3)
        consensus.cast_vote(0, 1)
        consensus.cast_vote(1, 0)
        consensus.cast_vote(2, 1)
        self.assertEqual(consensus.tally_votes(), 2)

    def test_consensus_reached(self):
        consensus = QuantumConsensus(num_participants=5)
        consensus.cast_vote(0, 1)
        consensus.cast_vote(1, 1)
        consensus.cast_vote(2, 0)
        consensus.cast_vote(3, 1)
        consensus.cast_vote(4, 0)
        self.assertTrue(consensus.consensus_reached())

    def test_consensus_not_reached(self):
        consensus = QuantumConsensus(num_participants=5)
        consensus.cast_vote(0, 1)
        consensus.cast_vote(1, 0)
        consensus.cast_vote(2, 0)
        consensus.cast_vote(3, 0)
        consensus.cast_vote(4, 0)
        self.assertFalse(consensus.consensus_reached())

    def test_entanglement_voting_protocol(self):
        voting_protocol = EntanglementVotingProtocol(num_participants=3)
        voting_protocol.cast_entangled_vote(0, 1)
        voting_protocol.cast_entangled_vote(1, 1)
        voting_protocol.cast_entangled_vote(2, 0)
        self.assertEqual(voting_protocol.tally_votes(), 2)
        self.assertTrue(voting_protocol.consensus_reached())

    def test_weighted_voting(self):
        consensus = QuantumConsensus(num_participants=5)
        consensus.set_weights([1, 1, 1, 2, 1])  # Set weights for participants
        consensus.cast_vote(0, 1)
        consensus.cast_vote(1, 1)
        consensus.cast_vote(2, 0)
        consensus.cast_vote(3, 1)
        consensus.cast_vote(4, 0)
        self.assertEqual(consensus.tally_votes(), 4)  # 1 + 1 + 1 + 2 = 5
        self.assertTrue(consensus.consensus_reached())

    def test_randomized_voting(self):
        num_participants = 10
        votes = simulate_voting_with_errors(num_participants, error_rate=0.1, bias=0.6)
        consensus = QuantumConsensus(num_participants=num_participants)
        for i, vote in enumerate(votes):
            consensus.cast_vote(i, vote)
        print("Randomized Votes:", votes)
        self.assertIn(consensus.tally_votes(), range(num_participants + 1))  # Total votes should be in valid range

if __name__ == "__main__":
    unittest.main()
