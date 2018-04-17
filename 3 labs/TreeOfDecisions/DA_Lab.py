import pandas as pd
import numpy as np

dataset = pd.read_csv('Churn_Modelling.csv')

X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [1, 2])
X = onehotencoder.fit_transform(X).toarray()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn import tree
get = tree.DecisionTreeClassifier()
get = get.fit(X_train, y_train)
result = get.predict(X_test)

from sklearn.metrics import accuracy_score
print('Accuracy: %s%%' % (accuracy_score(y_test, result) * 100))
