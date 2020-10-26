# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:06:54 2019

@author: prajw
"""

# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
y = y.reshape(10,1)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)
y = y.reshape(10,)


# Fitting the SVR to the dataset


from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X , y)


# Create your regressor here

# Predicting a new result
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.fit_transform())))
#y_pred = sc_y.inverse_transform(y_pred)

# Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (SVR Model, High precision)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
