import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint



iris_X, iris_y = datasets.load_iris(return_X_y=True)

# Split iris data into train and test data via a random permutation
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

param_distributions = {'n_neighbors': randint(3, 12),
                       }

search = RandomizedSearchCV(estimator=KNeighborsClassifier(),
                            n_iter=5,
                            param_distributions=param_distributions,
                            random_state=0)

search.fit(iris_X_train, iris_y_train)
print(search.best_params_)
print(search.score(iris_X_test, iris_y_test))