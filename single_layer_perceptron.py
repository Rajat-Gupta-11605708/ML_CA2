from numpy import *

class Perceptron(object):

    def __init__(self, eta=0.051, n_iter=10):
        self.eta = eta              #learning rate between 0.0 to 1.0
        self.n_iter = n_iter        #Passes over the training dataset

    def fit(self, x, y):            #training for x, y with current data set
        self.w_ = zeros(1+x.shape[1])

        for _ in range(self.n_iter):
            for xi, target in zip(x,y):     #takes iteration value and returns Iterator
                error = target-self.predict(xi)
                if error!=0:
                    update = self.eta * (self.predict(xi))
                    self.w_[1:] += update*xi
                    self.w_[0] += update
        return self

    def net_input(self, x):
        """Calculate net steps"""
        # Calculate net input
        return dot(x, self.w_[1:]+self.w_[0])

    def predict(self, x):
        """Return Class label after unit step"""
        return where(self.net_input(x) >= 0.0, 1, -1)       #ternary operator

x = array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
print("Inputs : ",x)

y = array([-1,-1,-1,-1,1,1,1,1])

ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(x,y)
print('Outputs : ',ppn.predict(x))
print('Output for [1,1,1] is : ', ppn.predict([1,1,1]))
print('Output for [0,0,0] is : ', ppn.predict([0,0,0]))