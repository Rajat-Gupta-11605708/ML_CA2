import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# create antecedents(inputs) and consequents(outputs):
load = ctrl.Antecedent(np.arange(0, 11, 1), 'load')
waterlvl = ctrl.Antecedent(np.arange(0, 11, 1), 'waterlvl')
time = ctrl.Consequent(np.arange(0, 61, 1), 'time')

# automatically assign membership functions:
load.automf(5)
waterlvl.automf(5)
time.automf(5)

waterlvl['average'].view()
input('Press <return> to continue...')

# create rules:
rules = [
	ctrl.Rule(load['poor'] | waterlvl['poor'], time['poor']),
	ctrl.Rule(load['mediocre'] | waterlvl['mediocre'], time['mediocre']),
	ctrl.Rule(load['average'] | waterlvl['average'], time['average']),
	ctrl.Rule(load['decent'] | waterlvl['decent'], time['decent']),
	ctrl.Rule(load['good'] | waterlvl['good'], time['good']),
]

# create control system with rules:
csystem = ctrl.ControlSystem(rules)

# create simulation with this control system:
simulation = ctrl.ControlSystemSimulation(csystem)

# pass inputs to simulation
simulation.input['load'] = float(input('Enter load: '))
simulation.input['waterlvl'] = float(input('Enter water level: '))

# compute/run simulation:
simulation.compute()

# show results
print('Estimated time:', simulation.output['time'], 'minutes')
time.view(sim=simulation)
input('Press <return> to continue...')
