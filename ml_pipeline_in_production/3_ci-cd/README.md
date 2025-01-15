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




