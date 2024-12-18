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

## Data Slicing Introduction

Data slicing is when we compute the metrics of our model holding a certain feature fixed.

For example, imagine an image classification model trained to recognize different animals. In general, we want to know the model's overall performance, but we may also want to know specifically how well it does on each class. For instance, if the model performs really well on dogs, wolves, and coyotes but performs poorly on cats, lions and tigers then that would indicate a problem. Furthermore, if our data was oversampled towards canines then we might not even notice the underperformance for felines if we were to look at the overall metrics.

Typical model validation such as validation sets and K-Fold Cross-Validation can be thought of as looking at horizontal slices of the data, i.e. an overall view of the data and performance. Data slicing can be thought of as looking at vertical slices of the data. This is by no means a rigorous distinction but is helpful to keep in mind.

### Use Cases

Data slicing should be used in the model validation process before deploying a model. Just as you would verify overall performance, you should verify performance on all relevant slices. What counts as "relevant" is highly dependent on the type of model/data, and the domain. For example, slicing on the specialty of medical providers in a disease predictor, or race and gender in a recidivism (repeated criminal offenses) predictor.

The same slices that you monitor pre-deployment should also be monitored post-deployment. Of course in post-deployment, you will not have labels to compute exact metrics, but given enough examples, one can compute the output values on a given slice like classification probability and see if it is statistically similar to the same classification probability on the training data.

While it's beyond the scope of this course, there is a growing field of "slice-based learning" (linked in the further reading). Understanding how your model performs on a more granular level can potentially open opportunities for further model developments.





