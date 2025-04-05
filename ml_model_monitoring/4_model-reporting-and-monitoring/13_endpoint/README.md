Configuring an API is only the first step to having a useful API. After configuration, you need to write scripts for endpoints that can provide useful information to you and other users of the API.

In this exercise, you'll write scripts for API endpoints so they can provide useful information about data.

## Environment and Starter

You can use the workspace below to create and run your solution.

We've provided a starter file called `appe2.py` in the `/L5/` directory. You can add your endpoints to that file, which is already configured to run on your workspace.

## Instructions: Function for Reading Data

The first thing you need to add to your `appe2.py` script is a function for reading data.

You can call your function `readpandas()`. It should take a filename string as its input. It should use a pandas method to read a CSV whose filename is given by the function input. It should return the DataFrame that it read.

## Instructions: Size Endpoint

Next, you can write a "size" endpoint that enables users to check the size of a dataset.

Your "size" endpoint needs to start with a line that specifies the app route (the route should be called '/size').

Your endpoint needs a function, that you can call `size()`. This function should read a query string from the API user called "filename". Then, your function should call the `readpandas()` function you created previously, passing the filename as the argument to this function. This will enable you to get the Dataframe specified by the filename.

Finally, you need to add a return statement to your `size()` function. It should return the **number of rows** of the pandas DataFrame the function read.

## Instructions - Summary Endpoint

Next, you can write a "summary" endpoint that enables users to check the summary statistics - in this case the mean of each column of a dataset.

Your "summary" endpoint needs to start with a line that specifies the app route (the route should be called '/summary').

Your endpoint needs a function, that you can call `summary()`. This function should read a query string from the API user called "filename". Then, your function should call the `readpandas()` function you created previously, passing the filename as the argument to this function. This will enable you to get the Dataframe specified by the filename.

You need to add a return statement to your `summary()` function. It should return the **mean of the column** of the pandas DataFrame the function read.

Finally, you should test your `summary()` function. There's a dataset in the `/L5` directory of your workspace called `testdata.csv`. You can pass the name 'testdata.csv' to your `summary()` function, and check the column means of the file. . You can also test your `size()` function by passing the `testdata.csv` filename to it, and checking that it's working correctly, and returning the correct size.
