import numpy as np
import matplotlib.pyplot as plt

def generate_random_votes(num_participants, bias=None):
    """Generate random votes for participants.
    
    Parameters:
    - num_participants (int): Number of participants.
    - bias (float): Probability of voting '1' (between 0 and 1). If None, votes are uniformly random.
    
    Returns:
    - np.ndarray: Array of votes (0 or 1).
    """
    if bias is not None:
        if not (0 <= bias <= 1):
            raise ValueError("Bias must be between 0 and 1.")
        return np.random.choice([0, 1], size=num_participants, p=[1 - bias, bias])
    return np.random.choice([0, 1], size=num_participants)

def simulate_voting(num_participants, bias=None):
    """Simulate a voting process.
    
    Parameters:
    - num_participants (int): Number of participants.
    - bias (float): Probability of voting '1' (between 0 and 1).
    
    Returns:
    - np.ndarray: Array of simulated votes.
    """
    votes = generate_random_votes(num_participants, bias)
    return votes

def simulate_voting_with_errors(num_participants, error_rate, bias=None):
    """Simulate a voting process with potential errors.
    
    Parameters:
    - num_participants (int): Number of participants.
    - error_rate (float): Probability of an error occurring (flipping a vote).
    - bias (float): Probability of voting '1' (between 0 and 1).
    
    Returns:
    - np.ndarray: Array of votes after applying errors.
    """
    votes = simulate_voting(num_participants, bias)
    errors = np.random.rand(num_participants) < error_rate
    votes[errors] = 1 - votes[errors]  # Flip the votes where errors occur
    return votes

def visualize_vote_distribution(votes):
    """Visualize the distribution of votes.
    
    Parameters:
    - votes (np.ndarray): Array of votes (0 or 1).
    """
    unique, counts = np.unique(votes, return_counts=True)
    plt.bar(unique, counts, color=['blue', 'orange'], alpha=0.7)
    plt.xticks(unique, ['Vote 0', 'Vote 1'])
    plt.title('Vote Distribution')
    plt.xlabel('Vote')
    plt.ylabel('Count')
    plt.show()

# Example usage
if __name__ == "__main__":
    num_participants = 10
    bias = 0.6  # 60% chance of voting '1'
    error_rate = 0.1  # 10% chance of error

    votes = simulate_voting_with_errors(num_participants, error_rate, bias)
    print("Simulated Votes with Errors:", votes)
    visualize_vote_distribution(votes)
