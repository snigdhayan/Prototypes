# coding: utf-8

# Gather breast cancer data


from sklearn.datasets import load_breast_cancer
breast = load_breast_cancer()
breast_data = breast.data
breast_labels = breast.target


# Prepare data as pandas dataframe


import numpy as np
labels = np.reshape(breast_labels,(569,1))
final_breast_data = np.concatenate([breast_data,labels],axis=1)

import pandas as pd
breast_dataset = pd.DataFrame(final_breast_data)
features = breast.feature_names
features_labels = np.append(features,'label')
breast_dataset.columns = features_labels

# For simplicity reduce dataset to a few relevant features only

from sklearn.preprocessing import StandardScaler

X, Y = breast_dataset.drop(columns='label'), breast_dataset['label']
X_norm = StandardScaler().fit_transform(X)

from sklearn.feature_selection import SelectPercentile, f_regression

selector = SelectPercentile(f_regression, percentile=10)
X_new = selector.fit_transform(X_norm, Y)

feature_support = selector.get_support()
selected_features = X.loc[:,feature_support].columns

breast_dataset = breast_dataset[np.append(selected_features,'label')]

# Split data for training and testing

from sklearn.model_selection import train_test_split

split = 0.3
breast_dataset_train, breast_dataset_test = train_test_split(breast_dataset, test_size=split)
X_train, Y_train = breast_dataset_train.drop(columns='label'), breast_dataset_train['label']
X_test, Y_test = breast_dataset_test.drop(columns='label'), breast_dataset_test['label']


# Train a simple decision tree model and then save it using pickle

from sklearn import tree

model = tree.DecisionTreeClassifier(criterion ="entropy", max_depth = 5).fit(X_train,Y_train)

import pickle

pickle.dump(model, open('./myModel.pkl','wb'))