.. target_modeling documentation master file, created by
   sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

target_modeling documentation
==============================================

This report analyzes the several machine learning models—Logistic Regression, Stochastic Gradient Descent, Decision Tree, and Random Forest—through model evaluation and the tuning of hyperparameters, which are parameters that define the model. The chosen models where used because they best handled large data sets with lots of features. The features were cleaned up and transformed in the third section of the Jupyter Notebook: Clean raw data.

In the Clean raw data section I removed mostly empty columns and converted time like columns to time stamps, which were later converted to integers for preprocessing. This last step separates the data set into testing and training sets for model validation. In the preprocessing the data is also scaled from 0 to 1, this helps the models converge.

Once the notebook has been run once, the cleaned data will be saved into a csv file. Then the notebook could be started from Section: Load cleaned data.

The initial inspection of the data demonstrates an unbalanced data set, with ~75% of data labeled 0; ~25%, 1. Wherever possible the models were tuned to fit an unbalanced data set, with class_weight ='balanced'. Given more time and familiarity with models, I would have included Validation Curves to plot validation scores and training scores as a function of model complexity.

**Summary**

Most of the models converged, however, some converged faster than others. Logistic Regression yielded the best f1-score for items labeled 1. Logistic Regression also took the longest time to train. Conversely, Random Forest yielded the best f1 score for items labels 0, and with the shortest training time.


Code on `github <https://github.com/caheredia/target_modeling/>`_



Contents:

.. toctree::
   :maxdepth: 2


   README
   modules

Analysis
====================
Jupyter notebook contents:

.. toctree::
   :maxdepth: 2

   0.1-cristian_explore_data.ipynb

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
