from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from time import time
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


# populate dict with classifiers
model_dict = {}

model_dict['Logistic Regression'] = LogisticRegression(
    class_weight='balanced', fit_intercept=False, solver='sag')


model_dict['Stochastic Gradient Descent'] = SGDClassifier(
    loss="hinge", max_iter=20, class_weight='balanced',  fit_intercept=False)


model_dict['Decision Tree'] = DecisionTreeClassifier(
    max_depth=11, class_weight='balanced')

model_dict['Random Forest'] = RandomForestClassifier(
    n_estimators=100, n_jobs=-1, class_weight='balanced')


# label data
target_names = ['0', '1']


def run_models(Xtrain, ytrain, Xtest, ytest, model_dict=model_dict):
    """Runs a list of models.

    Runs a list of models defined in model_dict.
    Tax


    Parameters
    ----------
    Xtrain : numpy.ndarray
        training data
    ytrain : numpy.ndarray
        training target data
    Xtest : numpy.ndarray
        test data
    ytrain : numpy.ndarray
        training test data
    model_dict : list (optional)
        dictionary of models to run

    """

    for name in model_dict:
        print(name)

        clf = model_dict[name]
        t0 = time()
        clf.fit(Xtrain, ytrain)
        train_time = time() - t0
        print("train time: {:0.2f}s".format(train_time))

        t0 = time()
        ypred = clf.predict(Xtest)
        test_time = time() - t0
        print('test time: {:0.2f}s'.format(test_time))
        print('Accuracy Score: {} \n'.format(accuracy_score(ytest, ypred)))
        print(classification_report(ytest, ypred, target_names=target_names))
        print('-' * 80)
