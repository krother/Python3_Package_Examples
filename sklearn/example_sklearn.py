
from sklearn import svm, datasets, cross_validation

# Load one of the example datasets
# and divide it into a training and test set:
iris = datasets.load_iris()
Xtrain, Xtest, Ytrain, Ytest = \
    cross_validation.train_test_split(iris.data, iris.target, \
    test_size=0.4, random_state=True)


# Fit a Support Vector Machine model and test it:
svc = svm.SVC(kernel='linear', C=1.0).fit(Xtrain, Ytrain)
print(svc.score(Xtest, Ytest))


# Do a five-fold cross-validation:
print(cross_validation.cross_val_score(svc, Xtrain, Ytrain, cv=5))
