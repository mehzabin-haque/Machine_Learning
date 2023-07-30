from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from KNN import KNN
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
from pandas.plotting import parallel_coordinates



def _confusion_matrix(y_true, y_pred):
    
    #this confusion matrix is for 2 class breast cancer dataset
    tp, fp, fn, tn = [np.sum((y_true == 2.0) & (y_pred == 2.0)), 
                        np.sum((y_true == 2.0) & (y_pred == 4.0)), 
                        np.sum((y_true == 4.0) & (y_pred == 2.0)), 
                        np.sum((y_true == 4.0) & (y_pred == 4.0))
                    ]

    return [[tp, fp], [fn, tn]]

def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)

if __name__ == '__main__':
    data = np.genfromtxt('DBMS/Datasets/Iris/iris.csv', delimiter=',')
    X, y = data[:, 0:-1], data[:, -1]

    cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])
    # print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    plt.figure()
    plt.scatter(X[:,2],X[:,3], c=y, cmap=cmap, edgecolor='k', s=20)
    plt.show()

    clf = KNN(k=5)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)   

    acc = accuracy(y_test, predictions)

    print (confusion_matrix(y_test, predictions))

    # print("Confusion Matrix: \n", _confusion_matrix(y_test, predictions)[0], "\n", _confusion_matrix(y_test, predictions)[1])
    print(f'{acc*100:.4f}%' )