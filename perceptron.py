import numpy as np
import random

class Perceptron:
	def __init__(self, learn_speed, num_weights):
		self.speed = learn_speed
		self.weights = []
		
		# assign random weights between -1 and 1:
		for x in range(0, num_weights):
			self.weights.append(random.random()*2-1)
		# random.random() returns a random between 0 and 1
	def activate(self, num):
		# turn a sum over 0 into 1, and below 0 into -1
		if num >= 0:
			return 1
		return -1
    
	def feed_forward(self, inputs):
		sum = 0
		# multiply inputs by weights and sum them
		sum = np.dot(inputs, self.weights)
		return self.activate(sum)

	def adjust_weights(self, inputs, desired_output):
		guess = self.feed_forward(inputs)
		error = desired_output - guess

		for x in range(0, len(self.weights)):
			self.weights[x] += error*inputs[x]*self.speed

class Trainer:
	def __init__(self, iters = 1000):
		self.perceptron = Perceptron(0.01, 3)
		self.iters = iters
	
	def f(self, x):
		return x # line: f(x) = 0.5x + 10
	
	def train(self):
		for x in range(0, self.iters):
			x_coord = random.random()*500 - 250
			y_coord = random.random()*500 - 250
			line_y = self.f(x_coord)

			if y_coord > line_y:	# above line
				answer = 1
				self.perceptron.adjust_weights([x_coord, y_coord, 1], answer)
			else:					# below line
				answer = -1
				self.perceptron.adjust_weights([x_coord, y_coord, 1], answer)
		return self.perceptron		# return trained perceptron


trainer = Trainer(int(input()))
p = trainer.train()

print("(-7, 9):",p.feed_forward([-7, 9, 1]))
print("(3, 3):",p.feed_forward([3, 3, 1]))
