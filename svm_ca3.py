import numpy as np
from sklearn.model_selection import train_test_split
# ^for older versions of sklearn, replace model_selection with cross_validation
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# initialize data:
X = np.array([[1,1,1],
			 [1,1,0],
			 [1,0,0],
			 [1,0,1],
			 [0,0,1],
			 [0,0,0],
			 [0,1,0],
			 [0,1,1]])

y = np.array([1,1,1,1,-1,-1,-1,1])

# split data into training and testing sets:
X_train, X_test, y_train, y_test = train_test_split(X, y, 
								   test_size = 0.2, random_state = 1234)
# ^test_size is the fraction of data to be reserved for testing,
# ^random_state is used to make predictions repeatable

# initialize and train SVM:
svm = SVC(kernel = 'linear', C=1, random_state = 0)
svm.fit(X_train, y_train) # training on the training data

# make and show predictions on the test data:
y_pred = svm.predict(X_test)
print('Input for testing:')
print(X_test)
print('Predicted values:')
print(y_pred)

# show error and accuracy:
print('Misclassified samples: %d'%(y_test!=y_pred).sum())
print('Accuracy:%.2f'%accuracy_score(y_test, y_pred))
