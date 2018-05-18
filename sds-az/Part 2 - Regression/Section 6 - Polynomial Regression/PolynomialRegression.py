#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu May 17 20:50:35 2018
@author     : Sourabh
"""

# %%

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

np.set_printoptions(threshold=np.nan)

# constant properties that need changes according to the actual problem
Data_File = 'Position_Salaries.csv'
Dependent_Variable_Column = 2

# import the dataset
dataset = pd.read_csv(Data_File)
# extract the feature and the dependent variable vectors
# the features X should be in the form of a matrix whereas the target y can be
# a vector, so we have to provide a column range for extracting X unlike for y
# we don't need to keep the position names as a training feature
X = dataset.iloc[:, 1:Dependent_Variable_Column].values
y = dataset.iloc[:, Dependent_Variable_Column].values

# we don't need to split the dataset into Training set and the Test set for now
# because of 2 reasons:
# 1. We don't have enough data to keep separate training and test data sets
# 2. We need as much info as possible to train our model to make it accurate
# even feature scaling is not required

# fitting simple linear regression to the data set
# this has been done to keep a reference to compare with polynomial regression
linRegressor = LinearRegression()
linRegressor.fit(X, y)

# fitting polynomial regression to the data set
# the polynomial regressor is a transformation tool than can be used to trans-
# form an input feature X into another feature with multiple degrees of
# independet variable as we provide at the time of creating the regressor.
polyRegressor = PolynomialFeatures(degree=2)
X_poly = polyRegressor.fit_transform(X)
linPolyRegressor = LinearRegression()
linPolyRegressor.fit(X_poly, y)