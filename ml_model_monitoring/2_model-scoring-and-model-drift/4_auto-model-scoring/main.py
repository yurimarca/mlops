import pandas as pd
import pickle
from sklearn import metrics
from sklearn.metrics import f1_score

# load model
with open('samplemodel.pkl', 'rb') as file:
    model = pickle.load(file)

# read test data
testdata=pd.read_csv('testdata.csv')

X = testdata[['col1','col2']].values.reshape(-1,2)
y = testdata['col3'].values.reshape(-1,1)

# use model to predict new data
predicted=model.predict(X)

print(f"predicted result: {predicted}")

# Calculate metric
f1score=metrics.f1_score(predicted,y)

print(f"F1-score: {f1score}")
