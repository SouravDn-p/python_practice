import random

def random_chromosome(size):
    return [random.randint(1, size)for _ in range(size)] 

def fitness(chromosome):
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2 
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n

    for i in range(n):
        left_diagonal [i+chromosome[i]-1]+=1
        right_diagonal[len(chromosome) -i + chromosome
        [i] -2 ] +=1


if __name__ == "__main__": 
    nq = int(input("Enter The Number of Queen: ")) 
    maxFitness = (nq*(nq-1))/2
    population = [random_chromosome(nq) for _ in range(nq)]

    generation = 1  

    while not maxFitness in [fitness(chrom) for chrom in population]
    print("===  Generation {} ===".format(generation))

    print("=== you input : {} ===".format(population))