import pennylane as qml
import numpy as np
import logging
import pickle

class QRLAgent:
    def __init__(self, n_qubits, n_layers, learning_rate=0.1, gamma=0.99):
        self.dev = qml.device("default.qubit", wires=n_qubits)
        self.n_layers = n_layers
        self.params = np.random.randn(n_layers, n_qubits, 3)
        self.learning_rate = learning_rate
        self.gamma = gamma  # Discount factor for future rewards
        self.opt = qml.AdamOptimizer(stepsize=self.learning_rate)
        self.experience_replay = []  # Store experiences for replay
        self.max_experience_size = 1000  # Max size of experience replay
        self.target_params = np.copy(self.params)  # Target network parameters
        self.update_target_frequency = 10  # Frequency to update target network
        self.training_step = 0  # Track training steps

        # Set up logging
        logging.basicConfig(level=logging.INFO)

    @qml.qnode
    def circuit(self, state):
        for l in range(self.n_layers):
            for i in range(len(state)):
                qml.Rot(*self.params[l, i], wires=i)
        return [qml.expval(qml.PauliZ(i)) for i in range(len(state))]

    def optimize(self, network_state, reward_function):
        """Optimize the network policy using QRL."""
        action_probs = self.circuit(network_state)
        reward = reward_function(action_probs, network_state)

        # Store experience for replay
        self.store_experience(network_state, action_probs, reward)

        # Update parameters using experience replay
        if len(self.experience_replay) > 0:
            state, action_probs, reward = self.sample_experience()
            self.params = self.opt.step(lambda p: -reward, self.params)

        # Update target network periodically
        if self.training_step % self.update_target_frequency == 0:
            self.target_params = np.copy(self.params)

        self.training_step += 1
        return action_probs

    def store_experience(self, state, action_probs, reward):
        """Store experience in the replay buffer."""
        if len(self.experience_replay) >= self.max_experience_size:
            self.experience_replay.pop(0)  # Remove oldest experience
        self.experience_replay.append((state, action_probs, reward))

    def sample_experience(self):
        """Sample a random experience from the replay buffer."""
        return self.experience_replay[np.random.randint(len(self.experience_replay))]

    def save_model(self, filename):
        """Save the model parameters to a file."""
        with open(filename, 'wb') as f:
            pickle.dump(self.params, f)
        logging.info(f"Model parameters saved to {filename}")

    def load_model(self, filename):
        """Load the model parameters from a file."""
        with open(filename, 'rb') as f:
            self.params = pickle.load(f)
        logging.info(f"Model parameters loaded from {filename}")

    def set_learning_rate(self, new_learning_rate):
        """Set a new learning rate."""
        self.learning_rate = new_learning_rate
        self.opt = qml.AdamOptimizer(stepsize=self.learning_rate)
        logging.info(f"Learning rate updated to {new_learning_rate}")

    def set_discount_factor(self, new_gamma):
        """Set a new discount factor."""
        self.gamma = new_gamma
        logging.info(f"Discount factor updated to {new_gamma}")
