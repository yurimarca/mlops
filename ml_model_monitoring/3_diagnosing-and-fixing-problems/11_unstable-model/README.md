Data integrity is a common problem in ML projects. In previous exercises, you detected data integrity issues. In this exercise, you'll go a step further and resolve the data integrity issues.

### Instructions: Checking for Data Integrity Problems

Start by reading the dataset called `samplefile3.csv`, which is found in the `/L4/` directory of your workspace. Store it as a variable called `thedata` in your Python session.

Next, calculate how many NA values are in **each column** of your dataset (`thedata`). You can use methods from the `pandas` module to accomplish this.

### Instructions: Resolving Data Integrity Issues

There are some data integrity issues in your data (NA values). In order to resolve these issues, you should perform imputation. To complete imputation, you'll replace NA values with the column means of each column of your dataset, as follows:

- Replace every NA value in the `col1` column with the mean of all `col1` values
- Replace every NA value in the `col2` column with the mean of all `col2` values
- Replace every NA value in the `col3` column with the mean of all `col3` values


