from dvclive import Live
import pickle
import numpy as np
from pathlib import Path
import os
from sklearn.metrics import mean_squared_error

def main():
    with open('model.pkl', "rb") as fd:
        lin_reg = pickle.load(fd)

    X_test = np.loadtxt(os.path.join(project_dir, 'data', 'processed','X_test.csv'), delimiter=',')
    hml_test_labels = np.loadtxt(os.path.join(project_dir, 'data', 'processed','Y_test.csv'), delimiter=',')
    y_test_predict = lin_reg.predict(X_test)
    print(mean_squared_error(hml_test_labels,y_test_predict,squared=False))

    eval_path = os.path.join("evaluation", "test")
    live = Live(eval_path)
    live.log("mse", mean_squared_error(hml_test_labels,y_test_predict,squared=False))

if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[2]
    main()