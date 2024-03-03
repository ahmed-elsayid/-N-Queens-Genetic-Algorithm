import random
import time
import numpy as np

def create_population(size):
    """Create a population of random strings of given length."""
    return np.random.randint(8, size=(size, 8))

def calculate_fitness(population):
    """Calculate the fitness of each individual in the population based on the N-Queens problem."""
    fitness = []
    for i in population:
        penalty = 0
        for j in range(len(i)):
            row = i[j]
            for k in range(len(i)):
                if k == j:
                    continue
                distance = abs(j - k)
                if i[k] in [row, row + distance, row - distance]:
                    penalty += 1

        fitness.append(penalty)
    fitness = [round(1 / (i + 1) * 100) for i in fitness]
    return np.array(fitness)

def select_parents(population, fitness):
    """Select two parents from the population based on their fitness."""
    p1, p2 = random.choices(population, weights=fitness, k=2)
    return p1, p2

def crossover(parent1, parent2):
    """Perform crossover between two parents to create a child."""
    center = random.randint(1, len(parent1) - 1)
    return np.concatenate((parent1[:center], parent2[center:]))

def make_mutation(child, mutation_rate):
    """Introduce mutations in the child with a specified mutation rate."""
    mutation_options = ['mutate', 'no_mutate', 'no_mutate']
    if random.choices(mutation_options, weights=[mutation_rate, (1 - mutation_rate) / 2, (1 - mutation_rate) / 2], k=1)[0] == 'mutate':
        n = random.randint(0, len(child) - 1)
        child[n] = random.randint(0, 7)
    return child

def create_next_generation(population, mutation_rate):
    """Create a new generation by selecting parents, performing crossover, and introducing mutations."""
    fitness = calculate_fitness(population)
    new_generation = []

    for _ in range(len(population)):
        parent1, parent2 = select_parents(population, fitness)
        child = crossover(parent1, parent2)
        mutated_child = make_mutation(child, mutation_rate)
        new_generation.append(mutated_child)

    return new_generation

def check_goal_achieved(fitness):
    """Check if any individual in the generation has reached the target fitness."""
    return any(i == 100 for i in fitness)

def main(population_size, mutation_rate):
    """Evolve a population towards a solution for the N-Queens problem."""
    population = create_population(population_size)
    generation_count = 0
    start_time = time.time()

    while True:
        fitness = calculate_fitness(population)
        if check_goal_achieved(fitness):
            break
        population = create_next_generation(population, mutation_rate)
        generation_count += 1

    end_time = time.time()
    print(f"Number of generations: {generation_count} | Time taken: {round(end_time - start_time, 3)} seconds")

# Example usage with a population size of 100 and a mutation rate of 0.4
main(100, 0.4)
