import ast
import pandas as pd

# === 1. Load Historic Column Means ===
with open('historicmeans.txt', 'r') as file:
    # Converts string list into actual Python list
    historic_means = ast.literal_eval(file.read())

# === 2. Load New Data ===
df = pd.read_csv('samplefile2.csv')

# === 3. Calculate Current Column Means ===
current_means = df.mean().tolist()

# === 4. Compare Means for Stability ===
percent_diffs = [
    abs(curr - hist) / hist * 100 if hist != 0 else 0
    for curr, hist in zip(current_means, historic_means)
]

print("=== Data Stability Check ===")
print(f"Historic means: {historic_means}")
print(f"Current means: {current_means}")

print("Percent difference in column means:")
print(percent_diffs)

# === 5. Check for Missing Values (Data Integrity) ===
na_counts = df.isna().sum().tolist()
na_percentages = [count / len(df) for count in na_counts]

print("\n=== Data Integrity Check ===")
print("Percent of NA values per column:")
print(na_percentages)


