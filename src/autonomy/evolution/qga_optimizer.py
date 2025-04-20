import numpy as np
import logging
import matplotlib.pyplot as plt

# Set up logging
logging.basicConfig(level=logging.INFO)

class QGAOptimizer:
    def __init__(self, population_size, mutation_rate, generations, solution_dim=10, fitness_function='sum'):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.solution_dim = solution_dim
        self.fitness_function = fitness_function
        self.population = self.initialize_population()
        self.fitness_history = []

    def initialize_population(self):
        """Initialize a random population."""
        return [self.random_solution() for _ in range(self.population_size)]

    def random_solution(self):
        """Generate a random solution."""
        return np.random.rand(self.solution_dim)  # Example: solution of specified dimension

    def fitness(self, solution):
        """Evaluate the fitness of a solution based on the selected fitness function."""
        if self.fitness_function == 'sum':
            return np.sum(solution)
        elif self.fitness_function == 'product':
            return np.prod(solution)
        elif self.fitness_function == 'mean':
            return np.mean(solution)
        else:
            raise ValueError("Unknown fitness function.")

    def mutate(self, solution):
        """Mutate a solution using Gaussian mutation."""
        for i in range(len(solution)):
            if np.random.rand() < self.mutation_rate:
                mutation_value = np.random.normal(0, 0.1)  # Gaussian mutation
                solution[i] += mutation_value
                solution[i] = np.clip(solution[i], 0, 1)  # Ensure values are within bounds
        return solution

    def crossover(self, parent1, parent2):
        """Perform crossover between two parents."""
        point = np.random.randint(1, len(parent1) - 1)
        return np.concatenate((parent1[:point], parent2[point:]))

    def optimize(self):
        """Run the genetic algorithm."""
        for generation in range(self.generations):
            fitness_scores = np.array([self.fitness(sol) for sol in self.population])
            self.fitness_history.append(np.mean(fitness_scores))
            logging.info(f"Generation {generation}: Average Fitness = {np.mean(fitness_scores)}")

            # Elitism: retain the best solution
            elite_count = max(1, int(0.1 * self.population_size))  # Keep top 10%
            elite_indices = np.argsort(fitness_scores)[-elite_count:]
            next_population = [self.population[i] for i in elite_indices]

            # Create new population
            while len(next_population) < self.population_size:
                parents = np.random.choice(self.population, size=2, p=fitness_scores/np.sum(fitness_scores))
                child1 = self.mutate(self.crossover(parents[0], parents[1]))
                child2 = self.mutate(self.crossover(parents[1], parents[0]))
                next_population.extend([child1, child2])

            self.population = next_population[:self.population_size]  # Ensure population size remains constant

        self.plot_fitness_history()
        return self.population

    def plot_fitness_history(self):
        """Plot the fitness history over generations."""
        plt.plot(self.fitness_history)
        plt.title('Fitness Over Generations')
        plt.xlabel('Generation')
        plt.ylabel('Average Fitness')
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    optimizer = QGAOptimizer(population_size=50, mutation_rate=0.1, generations=100, solution_dim=10, fitness_function='sum')
    final_population = optimizer.optimize()
    print("Final Population:", final_population)
