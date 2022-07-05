from copyreg import pickle
from pathlib import Path
from sklearn.linear_model import LinearRegression
import pandas as pd
import os
from sklearn.metrics import mean_squared_error
from data import make_dataset
import numpy as np
import pickle
import sys

# sys.path.append('../data')

def main():
    make_dataset.processData()
    hml_prepared = np.loadtxt(os.path.join(project_dir, 'data', 'processed','X_train.csv'), delimiter=',')
    # hml_prepared = pd.read_csv(os.path.join(project_dir, 'data', 'processed','X_train.csv'))
    hml_labels = np.loadtxt(os.path.join(project_dir, 'data', 'processed','Y_train.csv'), delimiter=',')
    # hml_labels = pd.read_csv(os.path.join(project_dir, 'data', 'processed','Y_train.csv'))
    X_test = np.loadtxt(os.path.join(project_dir, 'data', 'processed','X_test.csv'), delimiter=',')
    # X_test = pd.read_csv(os.path.join(project_dir, 'data', 'processed','X_test.csv'))
    hml_test_labels = np.loadtxt(os.path.join(project_dir, 'data', 'processed','Y_test.csv'), delimiter=',')
    # hml_test_labels = pd.read_csv(os.path.join(project_dir, 'data', 'processed','Y_test.csv'))
    lin_reg = LinearRegression()
    lin_reg.fit(hml_prepared,hml_labels)
    with open('model.pkl', "wb") as fd:
        pickle.dump(lin_reg, fd)
    # pickle.dump(lin_reg, 'model.pkl')
    # y_test_predict = lin_reg.predict(X_test)
    # print(mean_squared_error(hml_test_labels,y_test_predict,squared=False))

if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[2]
    main()