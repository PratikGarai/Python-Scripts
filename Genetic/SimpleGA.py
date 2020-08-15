import numpy as np


class Individual():

    def __init__(self, n_genes, choices):
        self.fitness = 0
        self.genes = np.random.choice(choices,n_genes)

    def calc_fitness(self):
        self.fitness = sum(self.genes)
        return self.fitness
    
    def set_weights(self, weights):
        self.genes = np.array(weights)
        

class Population():

    def __init__(self, n_population, n_genes, choices):
        self.population = n_population
        self.genes = n_genes
        self.choices = choices
        self.individuals = [ Individual(self.genes, self.choices) for _ in range(n_population) ]

    def get_fittest_n(self, n):
        all_individuals = sorted([ (i,i.calc_fitness()) for i in self.individuals ], key = lambda x : -x[1])
        return all_individuals[:n]

    def crossover(self):
        crossover_point = np.random.randint(0,self.genes)
        fit1 , fit2 = self.get_fittest_n(2)
        fit1 = list(fit1[0].genes)
        fit2 = list(fit2[0].genes)
        child1 = fit1[:crossover_point]+fit2[crossover_point:]
        child2 = fit2[:crossover_point]+fit1[crossover_point:]
        self.mutate(child1)
        self.mutate(child2)

    def mutate(self, child):
        to_mutate = np.random.choice([True,False,False])
        if to_mutate:
            n_mutate = np.random.choice(range(1,self.genes))
            indexes = np.random.choice(range(0,self.genes),n_mutate)
            for i in indexes:
                if child[i]==1:
                    child[i]=0
                    continue
                child[i]=1
        child_object = Individual(self.genes, self.choices)
        child_object.set_weights(child) 
        self.individuals.append( child_object )
        self.population += 1


if __name__ == '__main__':
    n_population = 5
    n_genes = 8
    n_generations  = 1

    a = Population(n_population, n_genes , [0,0,1] )
    highest_fitness = a.get_fittest_n(1)[0][1]
    
    print("Target : ",n_genes)
    while(highest_fitness<n_genes):
        print('Generation',n_generations,':',highest_fitness,'\t\tPopulation : ',a.population)
        a.crossover()
        highest_fitness = a.get_fittest_n(1)[0][1]
        n_generations += 1

    print('Generation',n_generations,':',highest_fitness)
    print('Successful')
