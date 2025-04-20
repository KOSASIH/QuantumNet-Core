import numpy as np

def random_selection(population, fitness_scores):
    """Select individuals from the population based on fitness scores."""
    total_fitness = np.sum(fitness_scores)
    probabilities = fitness_scores / total_fitness
    return np.random.choice(population, p=probabilities)

def tournament_selection(population, fitness_scores, tournament_size=3):
    """Select individuals using tournament selection."""
    selected = []
    for _ in range(len(population)):
        tournament_indices = np.random.choice(len(population), tournament_size, replace=False)
        tournament_fitness = fitness_scores[tournament_indices]
        winner_index = tournament_indices[np.argmax(tournament_fitness)]
        selected.append(population[winner_index])
    return np.array(selected)

def rank_based_selection(population, fitness_scores):
    """Select individuals based on their rank in fitness scores."""
    ranked_indices = np.argsort(fitness_scores)[::-1]  # Sort indices by fitness
    ranks = np.arange(1, len(population) + 1)
    probabilities = ranks / np.sum(ranks)  # Rank-based probabilities
    return np.random.choice(population, p=probabilities)

def normalize_fitness(fitness_scores):
    """Normalize fitness scores to a range of [0, 1]."""
    min_fitness = np.min(fitness_scores)
    max_fitness = np.max(fitness_scores)
    return (fitness_scores - min_fitness) / (max_fitness - min_fitness)

def calculate_average_fitness(fitness_scores):
    """Calculate the average fitness of a population."""
    return np.mean(fitness_scores)

def measure_diversity(population):
    """Measure the diversity of the population."""
    unique_individuals = len(set(map(tuple, population)))  # Count unique individuals
    return unique_individuals / len(population)  # Diversity ratio

def elitism(population, fitness_scores, elite_count):
    """Retain the best individuals in the population."""
    elite_indices = np.argsort(fitness_scores)[-elite_count:]  # Get indices of the best individuals
    return population[elite_indices]

# Example usage
if __name__ == "__main__":
    # Example population and fitness scores
    population = np.array([[0.1, 0.2], [0.4, 0.5], [0.3, 0.3], [0.9, 0.8]])
    fitness_scores = np.array([10, 20, 15, 25])

    selected = random_selection(population, fitness_scores)
    print("Random Selection:", selected)

    tournament_selected = tournament_selection(population, fitness_scores)
    print("Tournament Selection:", tournament_selected)

    rank_selected = rank_based_selection(population, fitness_scores)
    print("Rank-Based Selection:", rank_selected)

    normalized_fitness = normalize_fitness(fitness_scores)
    print("Normalized Fitness:", normalized_fitness)

    average_fitness = calculate_average_fitness(fitness_scores)
    print("Average Fitness:", average_fitness)

    diversity = measure_diversity(population)
    print("Population Diversity:", diversity)

    elite_individuals = elitism(population, fitness_scores, elite_count=2)
    print("Elite Individuals:", elite_individuals)
