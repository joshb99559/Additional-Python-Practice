from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate

X, y = make_regression(n_samples=1000, random_state=0)
lr = LinearRegression()

result = cross_validate(lr, X, y) # defaults to 5-fold CV
print(result['test_score'])

result = cross_validate(lr, X, y, cv=4) # can manually pick number of k folds
print(result['test_score'])