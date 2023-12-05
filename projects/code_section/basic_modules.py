"""
To perform the analysis and predict the house price,
we can use Python and it's data analysis libraries such as
pandas, numpy, matplotlib, seaborn and sklearn
"""
# Importing necessary libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder, StandardScaler 
from sklearn import metrics 
from sklearn.svm import SVC 
from xgboost import XGBRegressor 
from sklearn.linear_model import LinearRegression, Lasso, Ridge 
from sklearn.ensemble import RandomForestRegressor 

# Suppressing warnings to improve code readability
import warnings 
warnings.filterwarnings('ignore')

# Load the data into a pandas dataframe
df = pd.read_csv('data_zillow.csv')

# Display the first few rows
# print(df.head())

# To print the shape
# print(df.shape)
