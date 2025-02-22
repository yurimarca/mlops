import pandas as pd
import pickle
from sklearn import metrics
from sklearn.metrics import f1_score
import ast
import numpy as np

# Load trained model
with open('l3final.pkl', 'rb') as file:
    model = pickle.load(file)

# Read test data
testdata = pd.read_csv('testdatafinal.csv')

X = testdata['timeperiod'].values.reshape(-1,1)
y = testdata['sales'].values.reshape(-1,1)

# Model inference on test data
predicted = model.predict(X)
print(predicted)

# Compute metric
mse=metrics.mean_squared_error(predicted,y)
print(mse)

# Read previous model scores
with open('l3finalscores.txt', 'r') as f:
    mselist = ast.literal_eval(f.read())

# Compute IQR
iqr = np.quantile(mselist,0.75)-np.quantile(mselist,0.25)
print(iqr)

# Check non-parametric model drift test
drifttest = mse>(np.quantile(mselist,0.75)+iqr*1.5)
print(drifttest)
