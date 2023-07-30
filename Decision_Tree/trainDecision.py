from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from decisionTree import DecisionTree

data = datasets.load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

clf = DecisionTree(max_depth=10)
a = clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
clf.print_tree()

def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)

acc = accuracy(y_test, predictions)
print("Accuracy")
print(acc)