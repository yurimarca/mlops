# Software Engineering Principles

There are nearly as many "principles" of software engineering as grains of sand on a beach. Many principles focus on the process of writing code (such as the Single Responsibility Principle that states that every module/class/function should serve a single purpose), but for our purposes here we will focus on principles that pertain to model deployment.

Specifically we will focus on automation, testing, and versioning. None of these are unique to deploying a model, but each one plays an important role as we will see in the following lectures.

These principles leads us into Continuous Integration and Continuous Delivery (CI/CD). To put CI/CD into practice we will leverage GitHub Actions and Heroku, respectively.

- Software Engineering Principle: Automation
- Software Engineering Principle: Testing
- Software Engineering Principle: Versioning
- Continuous Integration with GitHub Actions
- Continuous Deployment with Heroku

## Software Engineering Principle -- Automation
Automation is the principle where we set up processes to do rote tasks for us routinely, such as on a schedule or when another action happens.

Automation can take many forms. For instance:

- Code formatters such as Black which remove the need to fiddle with exact placement of spaces, parenthesis, etc. in code.
- Editor features which vary depending on the text editor or IDE you use. For example, I have Vim set to remove EOL whitespace when saving a file since that clutters Git diffs and can break things like line continuation characters in shell scripts.
- Pre-Commit hooks allow us to run code, like formatters, before we commit a change. Since we're going to commit our code, this saves us from having to run a formatter separately.

Collectively, using automation helps you save time and reduces the risk of errors.

A related principle to automation is Don't Repeat Yourself (DRY). While not automation per se, it's a close cousin. We write functions instead of copy and pasting or rewriting code, and with automation, we set up processes instead of needing to retype or copy commands into the development environment.

## Software Engineering Principle -- Testing

When writing code we expect it to function as we planned, but often there can be unforeseen situations or edge cases. Testing is the principle we leverage to ensure our code functions as intended and is reproducible. A robust testing suite allows us to harden our code and make us more confident that, e.g., a function that does X actually does X instead of Y.

If we design our tests well, it can also help us catch edge cases that otherwise would have slipped through. Furthermore, if we tweak our code it ensures that we don't alter behavior unexpectedly.

**Tests build trust**. This trust is both for yourself but also for anyone you collaborate with. A robust testing suite should be developed alongside your code such that nearly every piece of functionality has a corresponding unit test.

As covered in a previous course, do not forget that machine learning models are inherently stochastic and built on data. The approach to testing these may be different and rely on tools such as Great Expectations.

Tests are like seat belts and safety bags. Their presence is not a guarantee that harm will not befall your code, but it is a best practice that mitigates harm in case something goes awry.

### Readings

1. [https://www.jeremyjordan.me/testing-ml/](https://www.jeremyjordan.me/testing-ml/)
1. [https://krokotsch.eu/posts/deep-learning-unit-tests/](https://krokotsch.eu/posts/deep-learning-unit-tests/)


## Software Engineering Principle -- Versioning

Software projects are by their nature complex with many dependencies and constant evolution. We manage this using versioning. Versioning is how we track our finished projects (e.g. version 1.0 of our code base may have 5 features, but a subsequent version 2.0 may have 10 features).

A popular approach to manage this is Semantic Versioning. Using this scheme a version number contains three parts, X.Y.Z:

- X is the major version, increment this when you have introduced API breaking changes.
- Y is the minor version, increment this when you make backward-compatible changes.
- Z is the patch version, increment this when you squash bugs or make smaller features.

For example, NumPy 1.20.0 released on January 30, 2021, before that was version 1.19.2. Going from 1.19.1 to 1.19.2 there were a handful of bug fixes. The jump to 1.20.0 included entirely new functions, type annotations throughout the code base, and deprecation of some old functions. By time you read this there might even be a NumPy 1.20.1 or beyond!

While semantic versioning is typically used to specify software, it can also be used for the model itself. Sometimes you make small adjustments to preprocessing and then retrain a model, other times you may entirely change the training data or underlying model. These changes would represent a change in the patch version and major version, respectively.

## Benefits of Software Engineering Principles

- What are the benefits of automation, testing, and versioning for solo development and how do these vary, if at all, for collaborative work?

Automation saves you time, and time paid in the present can often pay dividends in the future. Likewise, testing reduces headaches by helping to ensure that changes made to the code base integrate in without breaking anything else. Versioning is most helpful if you are releasing a product since it sets clear expectations to your users.

All of the benefits from solo development hold for collaborative work as well. However, versioning can become even more important because it communicates to your teammates which version should currently be used and is also used to coordinate development efforts (such as working on a new release or bug fixing an old one).

- What are some examples from your work where you could have leveraged automation, testing, or versioning?

At one company I was at we had a major product that was quickly thrown together with shifting business requirements. This product could have benefited from all three principles. The entire pipeline had to be manually run with a fairly tedious config file which could have been automated, there was no testing which resulted in fragile ad-hoc changes, and there wasn't clear versioning of the ML model which wasn't apparent until we created a second version and it took a while to incorporate the changes safely.

If automation and testing were embraced then we could have much more rapidly iterated on our product and brought it to a more sustainable state sooner, and versioning would have enhanced clarity around upgrading models.


# Continuous Integration/Continuous Delivery (CI/CD)

Continuous Integration and Continuous Delivery (or Deployment) (CI/CD) is a core driver of putting software engineering principles into practice.

Continuous integration is the practice of ensuring changes to the code fit into the overall code base. This is done by running our unit test suite and attempting to build the code on any platforms we choose to target. If this succeeds then the code is integrated. A robust testing suite is the backbone of a reliable continuous integration procedure.

If continous integration is the practice of making sure code is always deployable, then continuous delivery is the practice of keeping code actually deployed. CD allows you to make changes to the code, have it be verified by your CI process, and then immediately get served to your users without downtime.

## Continuous Integration with GitHub Actions

GitHub Actions is CI/CD built right into GitHub and comes with a plethora of pre-built workflows such as running your test suite or checking in if your code has any flake8 errors.

Setting up a GitHub Action is as straightforward as specifying when the action occurs, such as on push, what sort of VM it runs on, what programs and packages it installs, and then ultimately what commands get run. Here is a portion of the template workflow for Python that GitHub provides:

```python
name: Python package # Name of the Action.

on: [push] # When this action runs.

jobs:
  build:

    runs-on: ubuntu-latest # Which OS this runs on, you can also build on Windows or MacOS.
    strategy:
      matrix:
        python-version: [3.6, 3.7, 3.8] # You can build against multiple Python versions.

    steps:
    - uses: actions/checkout@v2 # Calling a pre-built GitHub Action which allows your Action to access your repository.
    - name: Set up Python ${{ matrix.python-version }} # Name of an action that sets up Python.
      uses: actions/setup-python@v2 # A pre-built GitHub Action that sets up a Python environment.
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies # The first step that isn't just calling another action.
      run: |
        python -m pip install --upgrade pip # Upgrade pip to the latest version.
        pip install pytest # Install pytest.
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi # If we have a requirements.txt, then install it.
    - name: Test with pytest # Final action which runs pytest. If any test fails, then this Action fails.
      run: |
        pytest
```

See the inline comments for details on the steps in this workflow.

Beyond CI/CD GitHub Actions can also automate actions such as greeting users when they submit their first pull request to your repository.

Other popular platforms for CI/CD include CircleCI, TravisCI, and Jenkins.

### Further Reading:
- GitHub's [overview](https://docs.github.com/en/actions) on Actions.
- GitHub's [docs](https://github.com/features/actions) on Actions.
- A [repository](https://github.com/actions/starter-workflows) of GitHub's starter workflows.

## Setting up GitHub Actions

The first action is the Python Application Action. This Action installs Python and the requirements for your application (if there are any). Lastly it runs flake8 and pytest -- the build fails if either a test fails or certain flake8 errors are hit.

In principle, one should run flake8 and pytest before you commit your code since that can be faster than waiting on the automated build process but this piece of automation ensures any contributors to the code also pass flake8 and pytest and they get checked in case you don't run them yourself. It also ensures that both of these pass when the code is built in a clean environment.

python-app.yaml
```yaml
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
```

The second Action is a scheduled job that uses a Unix time-based job scheduler called cron. This Action simply marks issues and pull requests as stale if they have no activity. If you go to stale.yaml's repo then you will see that there are many more options than shown in the default YAML file.

This Action is particularly useful for large projects, e.g. open-source projects, since it helps with the maintenance of issues and pull requests. It makes it easier to track what is current or not, and what may need attention without manually combing through the issues and pull requests.

**stale.yaml**
```yaml
name: Mark stale issues and pull requests

on:
  schedule:
  - cron: "30 1  *** "

jobs:
  stale:

    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write

    steps:
    - uses: actions/stale@v3
      with:
        repo-token: ${{ secrets.GITHUB_TOKEN }}
        stale-issue-message: 'Stale issue message'
        stale-pr-message: 'Stale pull request message'
        stale-issue-label: 'no-issue-activity'
        stale-pr-label: 'no-pr-activity'
```

## Introduction to Heroku

Heroku is a cloud Platform-as-a-Service (PaaS) that supports various languages and allows users to deploy apps. For our purposes, we will use Heroku to run a Python application that consists of an API for machine learning inference.

Heroku is built around lightweight containers called dynos that are easily scalable and adaptable to various tasks. For our work, we will be using one web dyno to run our API.

The instructions for launching an app are contained in a Procfile that resides in the highest level of your project directory. This file declares the dyno type and the associated command on each line, e.g.:

```
web: uvicorn main:app
```

This Procfile specifies a web dyno that runs the command uvicorn which is then running a web app cleverly called app that resides in main.py.

#### Further Reading
- Heroku's [https://devcenter.heroku.com/articles/getting-started-with-python](documentation )on getting started with Python.
- Heroku's [https://devcenter.heroku.com/articles/dynos](documentation) on dynos.

### Continuous Deployment with Heroku

Heroku makes it easy to do CD. It provides** **multiple different deployment options with the two most common being Git and Docker based deployments. We will leverage the GitHub connection.

You can connect an existing repository to Heroku either using the web GUI or the CLI and from there you can enable continuous delivery so that all changes to your code automatically get deployed to your Heroku app. Furthermore, you can specify that the CD only occurs when your continuous integration (e.g. your unit tests) succeeds. Doing this tightly couples our CI and CD processes which will help us avoid deploying a broken app.

When creating apps on Heroku, it's important to think of your slug and its limitations. The slug is your app and all of its dependencies, and it has a size limit of 500 MB. For light use cases all of your code, model, and even data could fit within that limit. However large models or frameworks (such as TensorFlow 2) can easily exceed the limit. Where possible, trim what is included in your slug using a .slugignore file, and in our case, we can leverage our remote DVC storage to contain our model and data and access them in our app when we need them.

## Deployment to Render Cloud Platform

[https://render.com/](Render) is a unified cloud platform to build and run apps and websites. Render provides all services in one place, including web services, static sites, background workers, cron jobs, Dockerfiles, private services, PostgreSQL, and Redis.

> Render is an alternative tp Heroku that provides free-tier services for small projects and hobbyists.

Here's how to deploy a Flask app and Postgres database on Render Console:

1. Create a Render account
1. Set up a Database Service with Postgres
1. Deploy a Flask app with Render's Web Service

We'll go through each step in detail.

Before you get started, make sure to download or clone the Flask app example for the exercise below from the [https://github.com/udacity/render-cloud-example](Udacity | Render Cloud Example repo).

> ⚠️ After you complete this exercise, please suspend or delete the services to avoid any charges.

#### Step 1: Create a Render Account

From the Render.com landing page, click the "Get Started" button to open the sign-up page. You can create an account by linking your GitHub, GitLab, or Google account or provide your email and password.

![2-create-new-account.jpeg](figs/2-create-new-account.jpeg)

#### Step 2: Set up a Database Service with Postgres

Once you are logged in, you will be redirected to the Render Dashboard. Click the New PostgreSQL button to set up a Postgres cloud database.

![3-setup-postgres.png](figs/3-setup-postgres.png)

On the **New Postgres** page:

1. Enter a name for the new database service: postgres-deployment-example
1. Select an instance type: Free
1. Click Create Database button

![32-create-database.png](figs/32-create-database.png)

#### Step 3: Deploy Apps with Render's Web Service

Once the database is set up, we can return to Render Dashboard and create a new Web Service.

![44-create-web-service.png](figs/4-create-web-service.png)

![5-connect-to-gh-repo.png](figs/5-connect-to-gh-repo.png)

On the **New Web Service** page:
1. Provide a name for the new database service: render-deployment-example
1. Select an instance type: Free
1. Enter the build command: `pip install -r requirements.txt`

**Note:** Render will install the dependencies from the requirements.txt in the GitHub repo.

![6-name-the-web-service.png](figs/6-name-the-web-service.png)

#### Connect the Database Service and Web Service
Before you click Create Web Service, you must connect the Postgres service so your Flask app can read and write data to the Postgres database. To connect the services, you can copy the Postgres database URL and paste it into the environment variables within the web service

#### Copy Postgres Database URL
From the Postgres service (name: "postgres-deployment-example"), click the "Info" side navigation and copy the Internal Database URL from the Connections page.


![8a-copy-db-url.png](figs/8a-copy-db-url.png)

#### Paste the Database URL in the Web Service Environment Variable
From the web service (name: render-deployment-example), create an environment variable with the key: DATABASE_URL and value: the Database URL value copied from the Postgres service..

![8b-paste-env-var.png](figs/8b-paste-env-var.png)


_Note: The Flask app will use the second environment variable ("EXCITED: true"). You can store any other credentials for your apps by adding the environment variables._

After the Web Service is ready, you can open your Flask app on the browser by clicking the app URL under the title on the Web Service page.

![9-create-web-service.png](figs/9-create-web-service.png)

Check that your app is running! It should show the message

```
Hello!!!!! You are doing great in this Udacity project.
```

![101-root.png](figs/101-root.png)

Now navigate to the coolkids page. You should see this message:

```
Be cool, man, be coooool! You're almost a FSND grad!
```

![102-coolkids.png](figs/102-coolkids.png)

Congratulations! You have deployed the sample app on the Render Cloud platform.

> ⚠️ After you complete this exercise, please suspend or delete the services to avoid any charges.



