import numpy as np
import pandas as pd
from test import train_and_test
from numpy import genfromtxt

if __name__ == '__main__':
    data = np.genfromtxt('DBMS\Datasets\Iris\iris.csv', delimiter=',')
    data = data[:,1:]
    X, y = data[:, 0:-1], data[:, -1]

    features = [
         'sepal length', 'sepal width', 'petal length', 'petal width'
    ]

    classes = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}

    train_and_test(X, y, classes, features)