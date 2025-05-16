import random  # এই লাইনটি যোগ করতে ভুলে গেছো

def single_point_crossover(parent1, parent2):
    if len(parent1) != len(parent2):
        raise ValueError("Parents must have the same length.")

    crossover_point = random.randint(1, len(parent1) - 1)

    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return offspring1, offspring2

parent1 = [1, 0, 1, 1, 0]
parent2 = [0, 1, 0, 1, 1]

offspring1, offspring2 = single_point_crossover(parent1, parent2)
print("Offspring 1:", offspring1)
print("Offspring 2:", offspring2)
