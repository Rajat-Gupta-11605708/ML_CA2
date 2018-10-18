import numpy as np

def fitness(population, x):
	return np.dot(population, x.T)

def select_mating_pool(population, x):
	f = fitness(population, x)
	pool_size = population.shape[0]//2
	pool = np.empty((pool_size, population.shape[1]))

	# calculate cumulative fitness:
	for i in range(1, len(f)):
		f[i] += f[i-1]
	
	# create pool:
	for i in range(pool_size):
		# chance of being selected is proportional to fitness
		r = np.random.random()*f[-1]
		for j in range(len(f)):
			if f[j] >= r:
				pool[i, :] = population[j, :]
				break
	return pool
	
def crossover(population, n_offspring, x):
	offsprings = np.empty((n_offspring, population.shape[1]))
	mating_pool = select_mating_pool(population, x)
	for i in range(n_offspring):
		parent_a = mating_pool[np.random.randint(0, mating_pool.shape[0])]
		parent_b = mating_pool[np.random.randint(0, mating_pool.shape[0])]
		crossover_point = np.random.randint(1, mating_pool.shape[1])
		offsprings[i, 0:crossover_point] = parent_a[0:crossover_point]
		offsprings[i, crossover_point:] = parent_b[crossover_point:]
	return offsprings

def mutate(offsprings):
	for i in range(offsprings.shape[0]):
		to_change = np.random.randint(0, offsprings.shape[1])
		m = np.random.random()*2-1
		offsprings[i, to_change] += m
		
x = np.array([1, 2, -3, 4, -5, 6])
np.random.seed(1)
nchroms = 8
ngenes = 6
n_offsprings = 4
population = np.random.uniform(-5, 5, (nchroms, ngenes))
print('Original random population:')
print(population)
print('\nOffsprings after crossover')
offsprings = crossover(population, n_offsprings, x)
print(offsprings)
print('\nOffsprings after mutation')
mutate(offsprings)
print(offsprings)

