## Exercise: A Full Reporting Pipeline

In this exercise, you'll use portions of each of the skills you've learned in this lesson.

**First**, you'll configure a new API. This API will have a new app configuration file that you can call `appfinal.py`.

**Second**, you'll write a new endpoint for the API. This new endpoint will read a pickle file for a deployed model, and it will also read a dataset. It will use the deployed pickle file to make predictions for the dataset, and it will return the prediction it makes.

**Third**, you'll write a script call `apicall.py` that will call this API. You can use either method for calling API's that we learned in this lesson - the choice is yours.

### Instructions - API configuration

You should configure your new API by writing a script called `appfinal.py`.

The `appfinal.py` script should follow the same configuration instructions as our previously configured API app files:

- import the needed methods from the flask module
- construct an app with a construction method from flask
- specify an endpoint route called '/prediction', intended to provide model predictions
- use a flask method to run the app

After you've complete the basic configuration, you'll be ready to script the prediction endpoint (see next step).

### Instructions - Scripting the prediction Endpoint

Your endpoint called '/prediction' should include a function called `predict()`, that you will define. Your `predict()`function should do all of the following:

- read the pickle file called `deployedmodel.pkl` from the `/L5` directory of your workspace
- read the dataset called `predictiondata.csv` from the `/L5`directory of your workspace
- use the `deployedmodel.pkl` pickle file to make predictions for the `predictiondata.csv` dataset
- return the prediction

After you write the code for this endpoint, you'll be ready to call the endpoint and check the predicted value.

### Instructions - Calling the New Endpoint

Finally, you can write a script called `apicall.py` that calls the new prediction endpoint you've created.

You can use either of the methods we discussed in the lesson to call the new endpoint. The methods we've discussed are the following:

- Using the `subprocess` module to run commands on the workspace command line
- Using the `requests` module to access the endpoint directly from within the script

After you access the prediction endpoint, you should print out the prediction that's returned using a `print()` statement.
