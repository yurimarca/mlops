In this lesson, we will cover performance testing and preparing a model for production.

You have put an immense amount of work creating a model by writing clean code with a robust reproducible work flow. Now we want to put the cherry on top and check our performance a few additional ways with **slices**, check for **bias**, and lastly deliver the final model with a **model card** that explains its origin, purpose, and any caveats.

- Review Validation Sets and K-Fold Cross-Validation
- Data Slicing
- Data Slicing Use Cases and Testing
- Model Bias
- The Aequitas Package
- Model Cards

# Review of Validation Set and K-Fold Cross-Validation

Validation set and K-Fold Cross-Validation (CV) are methods for evaluating overall model performance.

## Validation Set
In this approach, we split the training data into a train and validation set. The validation set is used to make decisions on what model to use before finally applying it to a final test set. Commonly, the validation set is between 10-30% of your overall data, but often it can be much less depending on data needs.

Conceptually this approach is simple and relatively fast. However, it means that your model does not get to see all the data when you train, and thus potentially leaves value on the table.

## K-Fold Cross-Validation
In this method, we split the data into K sets. The model is trained on K-1 then validated on the last. This process occurs K times, each time changing which fold is held out. The final validation score is the average of the metric on each fold. This leads to a more reliable measure of the performance metric since it minimizes the chance of an unlucky validation set that may not fully represent the data.

This approach allows your model to see all of the data since the set that is being held out changes on every iteration. However, this is computationally expensive since you must now train your model K times (albeit on a smaller data set size). Due to the cost, typically, K-Fold CV is not used for training neural networks, and instead, a validation set is used.

# Data Slicing Introduction

Data slicing is when we compute the metrics of our model holding a certain feature fixed.

For example, imagine an image classification model trained to recognize different animals. In general, we want to know the model's overall performance, but we may also want to know specifically how well it does on each class. For instance, if the model performs really well on dogs, wolves, and coyotes but performs poorly on cats, lions and tigers then that would indicate a problem. Furthermore, if our data was oversampled towards canines then we might not even notice the underperformance for felines if we were to look at the overall metrics.

Typical model validation such as validation sets and K-Fold Cross-Validation can be thought of as looking at horizontal slices of the data, i.e. an overall view of the data and performance. Data slicing can be thought of as looking at vertical slices of the data. This is by no means a rigorous distinction but is helpful to keep in mind.

## Use Cases

Data slicing should be used in the model validation process before deploying a model. Just as you would verify overall performance, you should verify performance on all relevant slices. What counts as "relevant" is highly dependent on the type of model/data, and the domain. For example, slicing on the specialty of medical providers in a disease predictor, or race and gender in a recidivism (repeated criminal offenses) predictor.

The same slices that you monitor pre-deployment should also be monitored post-deployment. Of course in post-deployment, you will not have labels to compute exact metrics, but given enough examples, one can compute the output values on a given slice like classification probability and see if it is statistically similar to the same classification probability on the training data.

While it's beyond the scope of this course, there is a growing field of "slice-based learning" (linked in the further reading). Understanding how your model performs on a more granular level can potentially open opportunities for further model developments.


## Demo Code

**foo.py**
```py
def foo():
    return "Hello world!"
```

**test_foo.py**
```py
from .foo import foo

def test_foo():
    foo_result = foo()

    expected_foo_result = "Hello world!"
    assert foo_result == expected_foo_result
```

**test_slice.py**
```py
import pandas as pd
import pytest


@pytest.fixture
def data():
    """ Simple function to generate some fake Pandas data."""
    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "numeric_feat": [3.14, 2.72, 1.62],
            "categorical_feat": ["dog", "dog", "cat"],
        }
    )
    return df


def test_data_shape(data):
    """ If your data is assumed to have no null values then this is a valid test. """
    assert data.shape == data.dropna().shape, "Dropping null changes shape."


def test_slice_averages(data):
    """ Test to see if our mean per categorical slice is in the range 1.5 to 2.5."""
    for cat_feat in data["categorical_feat"].unique():
        avg_value = data[data["categorical_feat"] == cat_feat]["numeric_feat"].mean()
        assert (
            2.5 > avg_value > 1.5
        ), f"For {cat_feat}, average of {avg_value} not between 2.5 and 3.5."

```


> Exercise 1 - Data Slicing


# Investigating Model Bias: Overview

Commonly, a model may perform well overall but underperform on some slices. Or, insidiously, a model may perform well by every metric you throw at it but still underperform in application. There are many reasons this could happen, but one culprit that has been gaining increased awareness is data bias. This is not to be confused with the bias in "bias-variance trade-off" which is part of the model under or overfitting and model generalization.

Data bias can come from a multitude of sources such as human error. A few examples are

- sampling error - when there is a mismatch between the sample and the intended population, one cause can be too small of a sample or using a biased method of collection.
- exclusion bias - exclusion of a group from a survey, it could arise from survey methods (such as only using in-person surveys) or perhaps only collecting data from a platform that certain age-groups frequent when instead an all-age sample is desired.
- recall bias - the human error that occurs when people are asked to recall events from the past. Data could be unreliable or clouded by external perspective.

Data bias can also be more systemic and stem from society-level errors such as unjust and unfair systems or stereotypes.

**Data bias can arise during data collection, data annotation, and/or data preprocessing.**

## Investigating Model Bias: The Aequitas Package

Data bias can take many forms and have many ramifications. There are a growing number of tools to classify, understand, and mitigate data bias such as What-If Tool, FairLearn, FairML, and Aequitas. Here, we will focus on Aequitas. Note, these tools are typically separate from model explainability tools such as SHAP and LIME.

Aequitas is a powerful Python library designed to assess and mitigate bias and fairness in machine learning models. It provides a range of tools to help data scientists and researchers understand and address potential biases in their models, particularly in the context of predictive analytics and decision-making systems.


Key Features of Aequitas:

1. Bias Assessment: Aequitas offers various metrics to assess bias across different groups in the dataset, such as race, gender, age, or any other protected attribute. It helps identify whether the model predictions exhibit disparities across these groups.

1. Fairness Evaluation: The library provides methods for evaluating fairness based on different criteria and definitions. These criteria include disparate impact, equal opportunity, and statistical parity.

1. Group-Based Analysis: Aequitas allows users to perform group-based analyses to compare model performance and outcomes across different demographic groups. This helps identify whether the model's predictions systematically disadvantage or advantage certain groups.

1. Visualizations: The package offers visualization tools to help interpret bias assessment results. Visualizations such as group-level fairness metrics, disparity metrics, and ROC curves can provide insights into the model's fairness.

1. Bias Mitigation Strategies: Aequitas also includes utilities for mitigating bias in machine learning models. These may involve adjusting the model's predictions or retraining it with fairness constraints to ensure equitable outcomes across different groups.

How to Use Aequitas for Model Explainability and Investigating Model Bias:

1. Data Preparation: Start by preparing your dataset and identifying any sensitive attributes (e.g., race, gender) you want to assess for bias. Ensure that your dataset is appropriately labeled and you have a target variable for prediction.

1. Model Training: Train your machine learning model using standard techniques. It could be a classification, regression, or other predictive model.

1. Model Evaluation: Evaluate your model's performance using standard metrics such as accuracy, precision, recall, and F1-score. Additionally, the model's fairness and bias will be assessed using Aequitas.

1. Bias Assessment: Use Aequitas to assess bias across different demographic groups in your dataset. Calculate metrics such as disparate impact, false positive rate parity, false negative rate parity, and others to identify any disparities in model predictions.

1. Fairness Evaluation: Using Aequitas, evaluate your model's fairness based on various fairness criteria. Compare the model's outcomes across different groups to ensure equitable treatment.

1. Visualizations: Use the visualization tools provided by Aequitas to visualize bias assessment results and fairness metrics. This can help interpret and communicate the findings effectively.

1. Bias Mitigation: If bias is detected, consider employing bias mitigation strategies. These may involve adjusting the model's predictions or retraining the model with fairness constraints to mitigate bias and ensure fair outcomes.

By following these steps and leveraging the capabilities of Aequitas, you can gain insights into your model's bias and fairness, ultimately leading to more transparent and equitable predictive analytics systems.

> Exercise - Running Aequitas

# Model Cards

Model cards are a succinct approach for documenting the creation, use, and shortcomings of a model. They should be written such that a non-expert can understand the model card's contents.

There is no one way to write a model card! Suggested sections include:

1. Model Details such as who made it, type of model, training/hyperparameter details, and links to any additional documentation like a paper reference.
1. Intended use for the model and the intended users.
1. Metrics of how the model performs. Include overall performance and also key slices. A figure or two can convey a lot.
1. Data including the training and validation data. How it was acquired and processed.
1. Bias inherent either in data or model. This could also be included in the metrics or data section.
1. Caveats, if there are any.


Google's [general documentation](https://modelcards.withgoogle.com/about) on model cards.

## Model Card exercise

- Example from previous Execise 2:

### Model Details
Justin C Smith created the model. It is logistic regression using the default hyperparameters in scikit-learn 0.24.2.

### Intended Use
This model should be used to predict the acceptability of a car based off a handful of attributes. The users are prospective car buyers.

### Metrics
The model was evaluated using F1 score. The value is 0.8960.

### Data
The data was obtained from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Car+Evaluation(opens in a new tab)). The target class was modified from four categories down to two: "unacc" and "acc", where "good" and "vgood" were mapped to "acc".

The original data set has 1728 rows, and a 75-25 split was used to break this into a train and test set. No stratification was done. To use the data for training a One Hot Encoder was used on the features and a label binarizer was used on the labels.

### Bias
According to Aequitas bias is present at the unsupervised and supervised level. This implies an unfairness in the underlying data and also unfairness in the model. From Aequitas summary plot we see bias is present in only some of the features and is not consistent across metrics.

