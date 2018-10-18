import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# create antecedents(inputs) and consequents(outputs):
mte = ctrl.Antecedent(np.arange(0, 31, 1), 'mte')
ete = ctrl.Antecedent(np.arange(0, 71, 1), 'ete')
cgpa = ctrl.Consequent(np.arange(0, 11, 1), 'cgpa')

# automatically assign membership functions:
mte.automf(5)
ete.automf(5)
cgpa.automf(5)

ete['average'].view()
input('Press <return> to continue...')

# create rules:
rules = [
	ctrl.Rule(mte['poor'] | ete['poor'], cgpa['poor']),
	ctrl.Rule(mte['mediocre'] | ete['mediocre'], cgpa['mediocre']),
	ctrl.Rule(mte['average'] | ete['average'], cgpa['average']),
	ctrl.Rule(mte['decent'] | ete['decent'], cgpa['decent']),
	ctrl.Rule(mte['good'] | ete['good'], cgpa['good']),
]

# create control system with rules:
csystem = ctrl.ControlSystem(rules)

# create simulation with this control system:
simulation = ctrl.ControlSystemSimulation(csystem)

# pass inputs to simulation
simulation.input['mte'] = float(input('Enter mte: '))
simulation.input['ete'] = float(input('Enter ete: '))

# compute/run simulation:
simulation.compute()

# show results
print('Estimated CGPA:', simulation.output['cgpa'])
cgpa.view(sim=simulation)
input('Press <return> to continue...')
