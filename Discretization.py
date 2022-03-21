# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:18:30 2021

@author: Karuna Singh
"""

# importing the packages
import pandas as pd
import numpy as np

# reading the packages
iris = pd.read_csv("C:\\Users\\Karuna Singh\\Study Material\\Datasets_360\\iris.csv")

# checking the nan values : there are no nan values
iris.isna().sum()

iris.duplicated().sum() # checking duplicate records : found none

# checking data types
iris.dtypes

# checking the types of Species in Species column : 3 types of species, can be assigned 3 classes to it
iris['Species'].unique()

# calling Label Encoder : to assign classes to types of species

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

iris['Species'] = labelencoder.fit_transform(iris['Species'])

# Species column has three classes no. 0, 1 & 2

