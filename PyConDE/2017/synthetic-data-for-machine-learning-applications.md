Synthetic Data for Machine Learning Applications
================================================

In this talk I will show how we use real and synthetic data to create
successful models for risk assessing pipeline anomalies. The main focus
is the estimation of the difference in the statistical properties of
real and generated data by machine learning methods.

Author
------

**Dr. Hendrik Niemeyer** ([@hniemeye](http://twitter.com/hniemeye))

Data Scientist working on predictive analytics with data from pipeline
inspection measurements.

Description
-----------

ROSEN provides predictive analytics for pipelines by detecting and risk
assessing anomalies from data gathered by inline inspection measurement
devices. Due to budget reasons (pipelines need to be dug up to get
acess) ground truth data for machine learning applications in this field
are usually scarce, imbalanced and not available for all existing
configurations of measurement devices. This creates the need for
synthetic data (using FEM simulations and unsupervised learning
algorithms) in order to be able to create successful models.

| But a naive mixture of real-world and synthetic samples in a model
  does not necessarily yield to an increased predictive performance
  because of differences in the statistical distributions in feature
  space. I will show how we evaluate the use of synthetic data besides
  simple visual inspection. Manifold learning (e.g. TSNE) can be used to
  gain an insight whether real and generated data are inherently
  different.
| Quantitative approaches like classifiers trained to discriminate
  between these types of data provide a non visual insight whether a
  "synthetic gap" in the feature distributions exists.

If the synthetic data is useful for model building careful
considerations have to be applied when constructing cross validation
folds and test sets to prevent biased estimates of the model
performance.

[![Synthetic Data for Machine Learning Applications](https://img.youtube.com/vi/riT9KTkBj0E/0.jpg)](https://www.youtube.com/embed/riT9KTkBj0E)
