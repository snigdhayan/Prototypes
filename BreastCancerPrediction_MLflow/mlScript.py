# coding: utf-8

# Gather breast cancer data

from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
breast_cancer_data = breast_cancer.data
breast_cancer_labels = breast_cancer.target


# Prepare data as pandas dataframe


import numpy as np
labels = np.reshape(breast_cancer_labels,(569,1))
final_breast_cancer_data = np.concatenate([breast_cancer_data,labels],axis=1)

import pandas as pd
breast_cancer_dataset = pd.DataFrame(final_breast_cancer_data)
features = breast_cancer.feature_names
features_labels = np.append(features,'label')
breast_cancer_dataset.columns = features_labels

"""
Replace 0,1 label by medical terminology (Benign = cancer false, Malignant = cancer true)

breast_cancer_dataset['label'].replace(0, 'Benign',inplace=True)
breast_cancer_dataset['label'].replace(1, 'Malignant',inplace=True)
"""

# For simplicity reduce dataset to a few relevant features only

from sklearn.preprocessing import StandardScaler

X, Y = breast_cancer_dataset.drop(columns='label'), breast_cancer_dataset['label']
X_norm = StandardScaler().fit_transform(X)

from sklearn.feature_selection import SelectPercentile, f_regression

selector = SelectPercentile(f_regression, percentile=10)
X_new = selector.fit_transform(X_norm, Y)

feature_support = selector.get_support()
selected_features = X.loc[:,feature_support].columns

breast_cancer_dataset = breast_cancer_dataset[np.append(selected_features,'label')]

# Split data for training and testing

from sklearn.model_selection import train_test_split

split = 0.3
breast_cancer_dataset_train, breast_cancer_dataset_test = train_test_split(breast_cancer_dataset, test_size=split)
X_train, Y_train = breast_cancer_dataset_train.drop(columns='label'), breast_cancer_dataset_train['label']
X_test, Y_test = breast_cancer_dataset_test.drop(columns='label'), breast_cancer_dataset_test['label']


# Train a simple decision tree model and then save it using pickle

from sklearn import tree

model = tree.DecisionTreeClassifier(criterion ="entropy", max_depth = 5).fit(X_train,Y_train)

import mlflow
import mlflow.sklearn

score = model.score(X_test, Y_test)
print("Score: %s" % score)
mlflow.log_metric("score", score)
mlflow.sklearn.log_model(model, "model")
print("Model saved in run %s" % mlflow.active_run().info.run_uuid)

import pickle

pickle.dump(model, open('./myModel.pkl','wb'))
