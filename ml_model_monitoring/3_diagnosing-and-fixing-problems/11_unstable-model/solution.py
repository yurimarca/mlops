import pandas as pd

# Step 1: Read the dataset
thedata = pd.read_csv('samplefile3.csv')

# Step 2: Count NA values per column
na_counts = thedata.isna().sum()
print("NA counts per column:\n", na_counts)

# Step 3: Replace NA values with column means
for column in ['col1', 'col2', 'col3']:
    mean_value = thedata[column].mean()
    print(f"{column}: {mean_value}")
    thedata[column].fillna(mean_value, inplace=True)
