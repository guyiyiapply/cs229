# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:58:38 2018

@author: guyia
"""

import numpy as np
import pandas as pd
from sklearn import tree

input_file = "C:/Users/guyia/Desktop/python class/DataScience/DataScience-Python3/PastHires.csv"
df = pd.read_csv(input_file, header = 0)

print(df.head())

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
print(df.head())

features = list(df.columns[1:7])
print(features)
#print(df.head(8))

y = df["Hired"]
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

from sklearn.ensemble import RandomForestClassifier

calf = RandomForestClassifier(n_estimators=10)
calf = clf.fit(X, y)

#Predict employment of an employed 10-year veteran
print (calf.predict([[10, 1, 4, 0, 0, 0]]))
#...and an unemployed 10-year veteran
print (calf.predict([[10, 0, 4, 0, 0, 0]]))

from IPython.display import Image  
from sklearn.externals.six import StringIO  
import pydotplus



dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=features)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())

