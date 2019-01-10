Active Learning - Building Semi-supervised Classifiers when Labeled Data is not Available
=========================================================================================

In situations where unlabeled data is abundant but labeled data cannot
be obtained easily active learning can be utilized to build classifiers
by intelligently querying users for labels. This talks shows the core
concepts and algorithms of active learning based on a real-world
project.

Author
------

**Dr. Hendrik Niemeyer** ([@hniemeye](http://twitter.com/hniemeye))

I am a Data Scientist working on applying machine learning solutions to
sensor data from non-destructive testing of pipelines in order to detect
and size internal damage.

Description
-----------

In many situations large datasets are available but unfortunately
labeling is expensive and time consuming. Active Learning is a concept
for building classifiers by letting the algorithm choose the training
data it uses. This achieves greater accuracy than just labeling a random
subset of the available dataset.

The active learning algorithm selects some unlabeled data instances
which are then labeled by a human annotator. Given this information a
classifier is trained and new instances for the human annotator to label
are selected. This iterative process tries to label as few instances as
possible while achieving high classification accuracy.

In this talk I will give a general overview of the core concepts and
techniques of active learning like algorithms for selecting the queries
and convergence criteria.

[![Active Learning - Building Semi-supervised Classifiers when Labeled Data is not Available](https://img.youtube.com/vi/0efyjq5rWS4/0.jpg)](https://www.youtube.com/watch?v=0efyjq5rWS4)
