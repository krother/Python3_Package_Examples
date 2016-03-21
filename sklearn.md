
# scikit-learn

### What it is good for?

Machine Learning.

The `scikit-learn` library contains regression and classification methods ranging from simple linear regression over logistic regression, Support Vector Machines and multiple clustering methods to sophisticated things like Random Forests. In addition, rich functions for validating predictions exist.

### Installed with Python by default

no

### Installed with Anaconda

yes

### How to install it?

    pip install scikit-learn

### Example

Load one of the example datasets and divide it into a training and test set:

    >>> from sklearn import svm, datasets, cross_validation

    >>> iris = datasets.load_iris()
    >>> X_train, X_test, Y_train, Y_test = \
    ...      cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=True)

Fit a Support Vector Machine model and test it:

    >>> svc = svm.SVC(kernel='linear', C=1.0, probability=True).fit(X_train, Y_train)
    >>> print(svc.score(X_test, Y_test))
    0.983333333333

Do a five-fold cross-validation:

    >>> print(accuracy = cross_validation.cross_val_score(svc, X, Y, cv=5, scoring='accuracy'))
    [ 0.96666667  1.          0.96666667  0.96666667  1.        ]

### Where to learn more?

[http://scipy.org/](http://scipy.org/)
