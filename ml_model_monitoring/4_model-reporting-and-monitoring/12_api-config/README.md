As a data scientist or ML engineer, you should have mastery over your own code, and a clear sense of the accuracy of your models. However, you may work with colleagues and stakeholders who aren't as familiar with your models as you are. Building ML monitoring and reporting API's can enable a broader audience to access crucial information about your deployed models.

In this exercise, you'll accomplish the basics of API configuration. This will prepare you to create a full-scale API that can provide monitoring and reporting about your data and models to a broad audience.

## Instructions - Setting up app.py

The first important step is to create a Python script called `app.py`. This will be the script that contains the "back end" of your API. Let's start by creating the first two lines and the last line of app.py before we fill in the middle.

The first line of your `app.py` script should import two methods from the flask module. You need to import a method for app construction, and also a method for getting user inputs.

The second line of `app.py` should create a variable called `app`. This variable needs to be an instance of the app construction method you imported.

The last line of your `app.py` script should contain a command to run your app. You can use the host `0.0.0.0`, and the port `8000`, to run your app.



## Instructions - A Simple Endpoint

Next, you need to specify an endpoint that API users can access. You'll start by specifying an app route. Start with the default app route: `'/'`.

Finally, you need to define a function that will return something to anyone who accesses your API. You can create a function called `index()`. Your `index()`function needs to get the query string provided by the user, and store it in a variable called `user`. Then, it should return a string that contains the word "Hello" and also the query string provided by the user.

(This endpoint isn't super impressive - all it does it take the user's name and say hello to them. But in a future exercise, we'll create more advanced endpoints that can return more detailed information about your models and data.)
