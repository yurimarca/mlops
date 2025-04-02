Almost every Python script imports third-party modules and depends on them to accomplish important functions. However, many third-party modules are updated frequently. Sometimes you need to update your modules because it will lead to better performance, and sometimes you need to avoid updating because the updates will break your code. Regardless, you need to carefully monitor the dependencies in your code to get optimal, error-free performance.

In this exercise, you'll write a script that accomplishes several dependency checks.

## Instructions - Broken Dependencies

You can start this project by writing Python code that checks for "broken dependencies." To check for broken dependencies, you need to use a command that's available as part of the `pip` program.

**Note**: Since `pip` is only accessible from the workspace command line, your solution needs to use a module that allows you to run workspace command line commands from within a Python script.

After you write the code that checks for broken dependencies, save the output of the code to a .txt file in your workspace called `broken.txt`.

## Instructions - Other Checks

There are several other dependency checks you can perform with `pip`. From within your Python solution script, perform pip commands to accomplish all of the following:

- Get a list of all installed packages. Write the output to a .txt file called `installed.txt`.
- Get all installed packages in a "requirements" format. Write the output to a file called `requirements.txt`
- Get information from pip about the scikit-learn module. Write the output to a file called `sklearninfo.txt`.


