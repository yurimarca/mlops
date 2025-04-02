After deploying an ML project, it's common for things to change: maybe a database gets decommissioned, or a subscription expires, or some software gets replaced. Some of these events can cause data to decay or disappear. Continuous monitoring of data integrity and stability is crucial to make sure your data remains a valid and usable input to your ML project.

In this exercise, you'll write Python scripts that can monitor two important things: data integrity and data stability.

## Instructions - Data Stability

You'll start this exercise by writing a script that can check for data stability. By "stability," we mean that the data hasn't changed much since the last time we trained our model. We'll check whether the column means of our data match historic column means to ensure stability.

### Reading past and present data

You can write your solution in a Python script called `stability_integrity.py`. The first part of your script should read a record of historic column means from previous versions of your data. You can find a record of historic column means in the file `/L4/historicmeans.txt`in your workspace. Save this record as a Python list.

**Remember**: when you read the `historicmeans.txt` file, you'll be reading a Python list that's stored in a .txt file. By default, Python will read this file as a string. You need to import and use a module that can read txt files as lists instead of strings.

After reading the list of historic means, you can read more recent data from the workspace file called `/L4/samplefile2.csv`. You should use the pandas module to read this into a DataFrame in Python.

### Comparing Past and Present Column Means

Next, you'll need to calculate the column means of the pandas DataFrame you just read into Python. You can use a pandas method that will complete these calculations in one line, and you can save the results in a list variable.

Now that you have a list of historic column means and a list of the current data's column means, you need to compare them. Write a list comprehension that finds the **percent difference** between each of the current column means and each of the historic column means.

The output of this list comprehension will be a **list with the same number of elements as the number of columns in your pandas DataFrame**. You can check this list to see how much your data has changed - in other words, how stable it is.



## Instructions - Data Integrity

After checking for data stability, you can add a little more to your script that checks for data integrity.

You can measure data integrity by checking how many NA values are in each column of your DataFrame. To do this, use a pandas method that determines whether each element of a column is NA, then use another pandas method that determines the total of NA values in each column.

Your output so far will be a list that contains a count of the number of NA values in each column of your DataFrame.

Finally, calculate the percentage of NA in each column. You can use a list comprehension to divide the count of NA values in each column by the number of rows in your DataFrame.

Your final output will be a list of the **percent of each column that consists of NA values.**




