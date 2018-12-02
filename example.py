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

# random_state is needed to achieve deterministic behavior.
dtc_people = DecisionTreeClassifier(random_state=42).fit(dummies, df.index.values)

# visualize tree
export_graphiz(dtc_people, feature_names=dummies.columns.values, class_names=df.name.values)

# Looking at the tree you will notice that the root represents a decision criteria by which the data is
# split into two subset: one for which the condition is true and one for which it is false.
# In this example the first node splits the data into a group for which sex_m is female and another for which
# the data is not female, i.e. male.
# Each subset is then further sub-divided into smaller groups using different features as decision criteria.
# In the current configuration this process continues until no more features are left to be evaluated or we
# arrive at a node where we are left with only one instance, i.e. where the data cannot be further subdivided into smaller
# groups.

# Note: catboost allows building decision tree based classifiers using boosting.
# The library supports categorical features without the need of prior encoding.
# This may be something to explore in later chapters. 