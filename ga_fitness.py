import numpy as np

def fitness(population, x):
	return np.dot(population, x.T)

x = np.array([-2, 2, 1, 3])
ngenes = 4	# no. of genes in each chromosom
npop = 8	# no. chromosomes in population

# set random seed for reproducible results
np.random.seed(0)

# generate random population:
population = np.random.uniform(-5, 5, (npop, ngenes))
print('Random Population:')

# following line prints out the whole population matrix:
[[print('%.3f'%(i), end='\t') for i in j] and print() for j in population]

# calculate fitess:
f = fitness(population, x)
print('\nFitnesses:')
[print('%.3f'%(i), end='\t') for i in f]
print()
