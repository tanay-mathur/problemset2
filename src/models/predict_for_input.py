from dvclive import Live
import pickle
import numpy as np
from pathlib import Path
import os
from sklearn.metrics import mean_squared_error
import pandas as pd

def main():
    with open('model.pkl', "rb") as fd:
        lin_reg = pickle.load(fd)
    with open('full_pipeline.pkl', "rb") as fd:
        full_pipeline = pickle.load(fd)
    longitude = float(input("Enter longitude: "))
    latitude = float(input("Enter latitude: "))
    housing_median_age = int(input("Enter housing median age: "))
    total_rooms = int(input("Enter total rooms: "))
    total_bedrooms = int(input("Enter total bedrooms: "))
    population = int(input("Enter population: "))
    households = int(input("Enter households: "))
    median_income = float(input("Enter median income: "))
    ocean_proximity = input("Enter ocean proximity: ")

    input_transformed = full_pipeline.transform(pd.DataFrame({"longitude":[longitude], "latitude":[latitude], "housing_median_age": [housing_median_age], "total_rooms": [total_rooms], "total_bedrooms": [total_bedrooms], "population": [population], "households": [households], "median_income": [median_income], "ocean_proximity": [ocean_proximity]}))
    y_predict = lin_reg.predict(input_transformed)
    print("Predicted house value: ", y_predict)

if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[2]
    main()