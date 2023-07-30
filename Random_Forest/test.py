from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from RandomForest import RandomForest



def _confusion_matrix(y_true, y_pred):
        tp, fp, fn, tn = [np.sum((y_true == 2.0) & (y_pred == 2.0)), 
                            np.sum((y_true == 2.0) & (y_pred == 4.0)), 
                            np.sum((y_true == 4.0) & (y_pred == 2.0)), 
                            np.sum((y_true == 4.0) & (y_pred == 4.0))
                        ]

        return [[tp, fp], [fn, tn]]


def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)


if __name__ == '__main__':
    data = np.genfromtxt('DBMS/DecisionTree/Data/Breast_cancer_data.csv', dtype = 'i8', delimiter=',')
    data = data[:,1:]
    data[:,[8,0]]=data[:,[0,8]]
    X, y = data[:, 0:-1], data[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    clf = RandomForest(n_trees=20)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)   

    acc = accuracy(y_test, predictions)

    print("Confusion Matrix: \n", _confusion_matrix(y_test, predictions)[0], "\n", _confusion_matrix(y_test, predictions)[1])
    # print(f'Confusion Matrix: \n[{_confusion_matrix(y_test, predictions)[0]}\n {_confusion_matrix(y_test, predictions)[1]}]')
    print(f'\nAccuracy: {acc*100:.4f}%' )
