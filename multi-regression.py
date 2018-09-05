# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:14:36 2018

@author: guyia
"""

import pandas as pd

df = pd.read_excel('cars.xls')
print(df.head())

import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].as_matrix())

print (X)

est = sm.OLS(y, X).fit()

print(est.summary())

print(y.groupby(df.Doors).mean())

