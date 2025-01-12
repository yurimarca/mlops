# Exercise: Aequitas

In this exercise, you will use Aequitas to investigate the potential bias in a model/data set.

- We'll use the Car Evaluation Data Set from the UCI Machine Learning Repository(opens in a new tab), a notebook that trains a logistic regression model to determine the car's acceptability is provided.

- Using Aequitas, determine if the model contains bias. For simplicity, from Aequitas' Fairness class obtain the results of the get_overall_fairness method which returns a dictionary with Yes/No result for "Unsupervised Fairness", "Supervised Fairness" and "Overall Fairness".

- Lastly, use the aequitas.plotting.Plot module and compute the summary on fpr, fnr, and for with a 1.25 fairness_threshold.

- You can draw inspiration from examples present here: https://github.com/dssg/aequitas/blob/master/docs/source/examples/compas_demo.ipynb