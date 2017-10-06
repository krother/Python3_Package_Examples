
# Load one of the example datasets and divide it into a training and test set:

from sklearn import svm, datasets, cross_validation

iris = datasets.load_iris()
X_train, X_test, Y_train, Y_test = \
    cross_validation.train_test_split(iris.data, iris.target, \
    test_size=0.4, random_state=True)


# Fit a Support Vector Machine model and test it:

svc = svm.SVC(kernel='linear', C=1.0, probability=True).fit(X_train, Y_train)
print(svc.score(X_test, Y_test))


# Do a five-fold cross-validation:

print(accuracy = cross_validation.cross_val_score(svc, X, Y, cv=5, scoring='accuracy'))
