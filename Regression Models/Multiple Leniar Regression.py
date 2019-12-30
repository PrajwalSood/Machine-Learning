import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('50_Startups.csv')
x = data.iloc[:,:-1].values
y = data.iloc[:,4].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_x = LabelEncoder()
x[:,3]=label_x.fit_transform(x[:,3])
ohe = OneHotEncoder(categorical_features=[3])
x = ohe.fit_transform(x).toarray()

x = x[:, 1:]

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x ,y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xtrain,ytrain)

ypred = regressor.predict(xtest)


#Optional Backward Elimination

import statsmodels.api as sm
x = np.append(arr = np.ones((50,1)).astype(int), values = x, axis = 1)
x_opt = x[:, [0, 1, 2, 3,4 ,5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:, [0, 1, 3,4 ,5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:, [0,3,4 ,5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:, [0,3,5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:, [0,3]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

xtrainopt, xtestopt, ytrain, ytest = train_test_split(x_opt ,y, test_size = 0.2, random_state = 0)
regressor.fit(xtrainopt,ytrain)

ypredbackelem = regressor.predict(xtestopt)