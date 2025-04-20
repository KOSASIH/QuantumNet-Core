import unittest
import numpy as np
from qga_optimizer import QGAOptimizer
from circuit_evolver import CircuitEvolver
from protocol_evolver import ProtocolEvolver

class TestEvolutionComponents(unittest.TestCase):
    
    def test_qga_optimizer(self):
        optimizer = QGAOptimizer(population_size=10, mutation_rate=0.1, generations=5)
        final_population = optimizer.optimize()
        
        # Check that the final population size is correct
        self.assertEqual(len(final_population), 10)
        
        # Check that the fitness scores are improving
        initial_fitness = optimizer.fitness(optimizer.population[0])
        final_fitness = optimizer.fitness(final_population[0])
        self.assertGreaterEqual(final_fitness, initial_fitness)

    def test_circuit_evolver(self):
        initial_circuit = ['H', 'CNOT']
        circuit_evolver = CircuitEvolver(initial_circuit)
        circuit_evolver.evolve(generations=5)
        
        # Check that the current circuit is not None and has evolved
        self.assertIsNotNone(circuit_evolver.current_circuit)
        self.assertNotEqual(circuit_evolver.current_circuit, initial_circuit)

        # Check that the performance score is greater than zero
        performance_score = circuit_evolver.evaluate_circuit()
        self.assertGreater(performance_score, 0)

    def test_protocol_evolver(self):
        initial_protocol = {
            'states': ['State_0', 'State_1'],
            'transitions': ['Transition_0', 'Transition_1']
        }
        protocol_evolver = ProtocolEvolver(initial_protocol)
        protocol_evolver.evolve(generations=5)
        
        # Check that the current protocol is not None and has evolved
        self.assertIsNotNone(protocol_evolver.current_protocol)
        self.assertNotEqual(protocol_evolver.current_protocol, initial_protocol)

        # Check that the performance score is greater than zero
        performance_score = protocol_evolver.evaluate_protocol()
        self.assertGreater(performance_score, 0)

    def test_empty_population_qga(self):
        optimizer = QGAOptimizer(population_size=0, mutation_rate=0.1, generations=5)
        with self.assertRaises(ValueError):
            optimizer.optimize()

    def test_empty_initial_circuit(self):
        circuit_evolver = CircuitEvolver(initial_circuit=[])
        circuit_evolver.evolve(generations=5)
        self.assertEqual(circuit_evolver.current_circuit, [])

    def test_empty_initial_protocol(self):
        initial_protocol = {
            'states': [],
            'transitions': []
        }
        protocol_evolver = ProtocolEvolver(initial_protocol)
        protocol_evolver.evolve(generations=5)
        self.assertEqual(protocol_evolver.current_protocol['states'], [])
        self.assertEqual(protocol_evolver.current_protocol['transitions'], [])

if __name__ == "__main__":
    unittest.main()
