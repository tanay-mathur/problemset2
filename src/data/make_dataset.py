# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
# from dotenv import find_dotenv, load_dotenv
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle


# @click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def processData():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    project_dir = Path(__file__).resolve().parents[2]
    df = pd.read_csv(os.path.join(project_dir, 'data', 'raw','housing.csv'))
    df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
    hml = df_train.drop("median_house_value", axis=1)
    hml_labels = df_train["median_house_value"].copy() 
    col_names = ["total_rooms","total_bedrooms","population","households"]
    hml_num = hml.drop("ocean_proximity", axis=1)
    num_pipeline = Pipeline([
                         ('imputer',SimpleImputer(strategy="median")),
                         ('scaler',StandardScaler())
                         ])

    cat_pipeline = Pipeline([
                            ('encoder',OneHotEncoder())
                            ])

    num_cols = list(hml_num) # Alternatively: hml_num.columns.values.tolist()
    cat_cols = ["ocean_proximity"]

    full_pipeline = ColumnTransformer([
                                    ('num',num_pipeline,num_cols),
                                    ('cat',cat_pipeline,cat_cols)
                                    ])

    hml_prepared = full_pipeline.fit_transform(hml)
    hml_test = df_test.drop("median_house_value", axis=1) # drop labels for training set
    hml_test_labels = df_test["median_house_value"].copy() 
    X_test = full_pipeline.transform(hml_test)
    with open('full_pipeline.pkl', "wb") as fd:
        pickle.dump(full_pipeline, fd)
    # np.savetxt("foo.csv", a, delimiter=",")
    np.savetxt(os.path.join(project_dir, 'data', 'processed','X_train.csv'), hml_prepared, delimiter=",")
    # pd.DataFrame(hml_prepared).to_csv(os.path.join(project_dir, 'data', 'processed','X_train.csv'),header=None, index=None)
    np.savetxt(os.path.join(project_dir, 'data', 'processed','Y_train.csv'), hml_labels, delimiter=",")
    # pd.DataFrame(hml_labels).to_csv(os.path.join(project_dir, 'data', 'processed','Y_train.csv'), header=None, index=None)
    np.savetxt(os.path.join(project_dir, 'data', 'processed','X_test.csv'), X_test, delimiter=",")
    # pd.DataFrame(X_test).to_csv(os.path.join(project_dir, 'data', 'processed','X_test.csv'), header=None, index=None)
    np.savetxt(os.path.join(project_dir, 'data', 'processed','Y_test.csv'), hml_test_labels, delimiter=",")
    # pd.DataFrame(hml_test_labels).to_csv(os.path.join(project_dir, 'data', 'processed','Y_test.csv'), header=None, index=None)


# if __name__ == '__main__':
#     log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#     logging.basicConfig(level=logging.INFO, format=log_fmt)

#     # not used in this stub but often useful for finding various files
#     project_dir = Path(__file__).resolve().parents[2]

#     # find .env automagically by walking up directories until it's found, then
#     # load up the .env entries as environment variables
#     # load_dotenv(find_dotenv())

    # processData()
