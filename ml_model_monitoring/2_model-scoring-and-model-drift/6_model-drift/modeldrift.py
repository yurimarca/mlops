import ast
import numpy as np

newr2=0.3625

# Open previous scores file
with open('previousscores.txt', 'r') as f:
    r2list = ast.literal_eval(f.read())
print(f"Previous scores: {r2list}")

# Raw Comparison test
firsttest = newr2<np.min(r2list)
print(f"Raw comparison test: {firsttest}")

# Parametric test
secondtest = newr2<np.mean(r2list)-2*np.std(r2list)
print(f"Mean: {np.mean(r2list)}")
print(f"Standard deviation: {np.std(r2list)}")
print(f"Parametric test: {secondtest}")

# Non-parametric test
iqr = np.quantile(r2list,0.75)-np.quantile(r2list,0.25)
thirdtest = newr2<np.quantile(r2list,0.25)-iqr*1.5
print(f"IQR: {iqr}")
print(f"Non-parametric test: {thirdtest}")


