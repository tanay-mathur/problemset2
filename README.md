ProblemSet2
==============================

Predict the median house price in a block (smallest census group in US) given other demographic and geographic information. 

Project Organization
------------

    ├── LICENSE
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
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

Tools used
--------
- Template from cookie cutter
- DVC pipelines
- CI pipelines from CML
- This has been deployed to an AWS EC2 instance

Details:
--------
- Cookie cutter
    - Template used from https://drivendata.github.io/cookiecutter-data-science/
- Data Version Control (DVC)
    - The data is stored in an s3 bucket and linked to DVC. Thus, it doesn't need to be uploaded to GitHub for tracking and can be fetched using `dvc pull`
    - Implemented a DVC pipeline to:
        - Read the raw data from data/housing.csv, process it, split it into train and test and place the processed data in data/processed. This data is then read from data/processed and used to train a linear regression model. A pickled version of this model is saved
        - Read the pickled model and test data, use it to make predictions and evaluate the mean squared error of the prediction on test data.
        The results of this evaluation are saved in evaluation/test.json.
- Continuous Machine Learning (CML) for DVC through GitHub actions
    - Whenever a push is made to the repository, there is a GitHub action based on CML and DVC that is triggered. It runs on a custom CML docker container.
    - At each push, the metrics (MSE) of the latest version are calculated. This is then compared with the previous version and the results of the comparison are sent by email once the action completes.
    - When a new pull request is opened, the error metrics of the two branches are compared by the action. This comparison is automatically added as a comment to the pull request. Example: https://github.com/tanay-mathur/problemset2/pull/2
- AWS EC2
    - This model has been deployed to an EC2 instance

--------
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
