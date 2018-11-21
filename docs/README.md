target_modeling
==============================

Build a classification model to rank the individuals in the data set, using the FLOZVPMFT4626A column as your target variable


This report analyzes the several machine learning models—Logistic Regression, Stochastic Gradient Descent, Decision Tree, and Random Forest—through model evaluation and the tuning of hyperparameters, which are parameters that define the model. The chosen models where used because they best handled large data sets with lots of features. The features were cleaned up and transformed in the third section of the Jupyter Notebook: Clean raw data.

In the Clean raw data section I removed mostly empty columns and converted time like columns to time stamps, which were later converted to integers for preprocessing. This last step separates the data set into testing and training sets for model validation. In the preprocessing the data is also scaled from 0 to 1, this helps the models converge.

Once the notebook has been run once, the cleaned data will be saved into a CSV file. Then the notebook could be started from Section: Load cleaned data.

The initial inspection of the data demonstrates an unbalanced data set, with ~75% of data labeled 0; ~25%, 1. Wherever possible the models were tuned to fit an unbalanced data set, with class_weight ='balanced'. Given more time and familiarity with models, I would have included Validation Curves to plot validation scores and training scores as a function of model complexity.

Summary
Most of the models converged, however, some converged faster than others. Logistic Regression yielded the best f1-score for items labeled 1. Logistic Regression also took the longest time to train. Conversely, Random Forest yielded the best f1 score for items labels 0, and with the shortest training time.






Logistic Regression
train time: 682.77s
test time: 0.32s
Accuracy Score: 0.67684

              precision    recall  f1-score   support

           0       0.87      0.67      0.76     18705
           1       0.42      0.71      0.52      6295

   micro avg       0.68      0.68      0.68     25000
   macro avg       0.64      0.69      0.64     25000
weighted avg       0.76      0.68      0.70     25000

--------------------------------------------------------------------------------
Stochastic Gradient Descent
train time: 6.00s
test time: 0.04s
Accuracy Score: 0.58804

              precision    recall  f1-score   support

           0       0.82      0.58      0.68     18705
           1       0.33      0.61      0.43      6295

   micro avg       0.59      0.59      0.59     25000
   macro avg       0.57      0.60      0.55     25000
weighted avg       0.69      0.59      0.62     25000

--------------------------------------------------------------------------------
Decision Tree
train time: 30.06s
test time: 0.14s
Accuracy Score: 0.65544

              precision    recall  f1-score   support

           0       0.84      0.66      0.74     18705
           1       0.39      0.63      0.48      6295

   micro avg       0.66      0.66      0.66     25000
   macro avg       0.61      0.65      0.61     25000
weighted avg       0.73      0.66      0.68     25000

--------------------------------------------------------------------------------
Random Forest
train time: 44.60s
test time: 0.90s
Accuracy Score: 0.77708

              precision    recall  f1-score   support

           0       0.79      0.96      0.87     18705
           1       0.67      0.23      0.34      6295

   micro avg       0.78      0.78      0.78     25000
   macro avg       0.73      0.59      0.60     25000
weighted avg       0.76      0.78      0.73     25000

--------------------------------------------------------------------------------


Project Organization
------------


    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── .ipynb             <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml   <- The environment file for reproducing the analysis environment
    │
    ├── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
            │                 predictions
            ├── predict_train_model.py
           
