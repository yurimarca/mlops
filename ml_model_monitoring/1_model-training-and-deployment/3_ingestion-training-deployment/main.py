import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

# Read data from CSV file
sales=pd.read_csv('sales.csv')

# Features and label
X = sales['timeperiod'].values.reshape(-1, 1)
y = sales['sales'].values.reshape(-1, 1)

# Linear regression
lm = LinearRegression()

# Model training
model = lm.fit(X, y)

# Store trained model
filehandler = open('./model.pkl', 'wb') 
pickle.dump(model, filehandler)
