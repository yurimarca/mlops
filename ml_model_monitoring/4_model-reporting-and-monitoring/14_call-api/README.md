# Exercise: Calling API Endpoints

The API's you've set up in the previous exercises are capable of returning data about ML models to whoever calls them. However, every API is different and calling API's correctly is not always easy. Writing scripts that correctly call API's is especially important since many of your API users may be non-technical people who have never called an API in their lives. Writing scripts that correctly and efficiently call API's and monitor their outputs can help you and others keep your ML models and projects up-to-date and effective.

In this exercise, you'll write a script that will call API endpoints in two different ways:

- by accessing the command line of your workspace
- by using the Python module called `requests`

It will be useful to understand two different ways to call API endpoints, because in some cases, one or the other method may be impossible. For example, you might have to work in an environment in which the requests module is not available. Or, you might have to work in an environment in which the command line has restrictions on it. In either case, you'll be unable to use one of the methods for calling API's, and it will be useful to know the other one.



## Instructions - Command Line

Create a python script `call_api_endpoint.py`. You should start by writing Python commands that will access your API endpoints from the workspace command line.

To write these commands, you need to use a method in the `subprocess` module to run a `curl` command on your workspace command line.

You need to write three commands:

1. Write a command that accesses the default API endpoint ('/'), passes your name as the user query string, and stores the result in a variable called `response1`.
2. Write a command that accesses the size endpoint ('/size'), passes "testdata.csv" as the filename query string, and stores the result in a variable called `response2`.
3. Write a command that accesses the summary endpoint ('/summary'), passes "testdata.csv as the filename query string, and stores the result in a variable called `response3`.

After these commands, you should write print statements in your script to print `response1`, `response2`, and `response3` to the workspace output.



## Instructions - Requests Module

Next, write Python commands that will access your API endpoints using the `requests` module.

To write these commands, you need to use a method in the `requests` module to get the content of your API endpoint output.

You need to write same commands but store the result to a different variable:

1. Write a command that accesses the default API endpoint ('/'), passes your name as the user query string, and stores the result in a variable called `response4`.
2. Write a command that accesses the size endpoint ('/size'), passes testdata.csv as the filename query string, and stores the result in a variable called `response5`.
3. Write a command that accesses the summary endpoint ('/summary'), passes testdata.csv as the filename query string, and stores the result in a variable called `response6`.

After these commands, you should write print statements in your solution script, to print `response4`, `response5`, and `response6` to the workspace output.




