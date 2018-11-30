# The purpose of this exercise is to apply the principles
# discussed in the first three lectures.

import numpy as np
import pandas as import pd

# read a CSV file
df = pd.read_csv('data.csv', sep=';')

# convert certain columns to category type
for cname in df.columns.values[1:]:
    df[cname] = df[cname].astype('category')


features = ['sex', 'hair_color']

# first way to create dummies: use pandas
dummies = pd.get_dummies(df, columns=features, drop_first=True)

# second way to create dummies: use scikit-learn
# from sklearn.preprocessing import OneHotEncoder
# ...

from sklearn.tree import DecisionTreeClassifier, export_graphiz

dtc_people = DecisionTreeClassifier().fit(dummies, df.index.values)
export_graphiz(dtc_people, feature_names=dummies.columns.values, class_names=df.name.values)