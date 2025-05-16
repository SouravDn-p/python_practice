import random

# ----- Create Initial Population -----
def generate_population(pop_size, chromosome_length):
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(pop_size)]

# ----- Fitness Function -----
def fitness(chromosome):
    # Example: maximize number of 1s (simple problem)
    return sum(chromosome)

# ----- Selection: Roulette Wheel Selection -----
def select_parent(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fit in zip(population, fitnesses):
        current += fit
        if current >= pick:
            return individual
    return population[-1]

# ----- Single Point Crossover -----
def single_point_crossover(parent1, parent2):
    if len(parent1) != len(parent2):
        raise ValueError("Parents must have the same length.")
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

# ----- Mutation -----
def mutate(offspring, mutation_rate=0.01):
    mutated_offspring = []
    for individual in offspring:
        mutated = individual.copy()
        for i in range(len(mutated)):
            if random.random() < mutation_rate:
                mutated[i] = 1 - mutated[i]  # Flip bit
        mutated_offspring.append(mutated)
    return mutated_offspring

# ----- Genetic Algorithm Main Function -----
def genetic_algorithm(pop_size=10, chromosome_length=8, generations=50, mutation_rate=0.01):
    population = generate_population(pop_size, chromosome_length)
    best_solution = None

    for gen in range(generations):
        print(f"\n--- Generation {gen + 1} ---")
        fitnesses = [fitness(ind) for ind in population]
        max_fit = max(fitnesses)
        best_solution = population[fitnesses.index(max_fit)]
        print(f"Best Fitness: {max_fit}, Chromosome: {best_solution}")

        new_population = []
        while len(new_population) < pop_size:
            # Selection
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)

            # Crossover
            child1, child2 = single_point_crossover(parent1, parent2)

            # Mutation
            children = mutate([child1, child2], mutation_rate)

            new_population.extend(children)

        population = new_population[:pop_size]

    print(f"\n✅ Final Best Solution: {best_solution}, Fitness: {fitness(best_solution)}")

# Run the algorithm
genetic_algorithm()
