'''
Contains utility functions and helper methods that are used across different 
parts of a project to promote code reuse and organization.
'''

# Here, the common functions that will be used throughout the project
# OR will be called from any file - will be called from here


# Importing necessary libraries
import os
import sys
import numpy as np
import pandas as pd
import dill

from sklearn.metrics import r2_score

from src.exception import CustomException

# Function for saving an object to the given file path
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path) # Taking File Path
        os.makedirs(dir_path, exist_ok = True) # Creating Directory

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj) # Dump the object to the directory created above

    except Exception as e:
        raise CustomException(e, sys)
    

# Function for model(s) evaluation on Training and Testing data - over a dictionary of model(s)
def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i] # Taking the model

            model.fit(X_train, y_train) # Model Training

            y_train_pred = model.predict(X_train) # Model Prediction on X_train

            y_test_pred = model.predict(X_test) # Model Prediction on X_test

            train_model_score = r2_score(y_train, y_train_pred) # Model R2-score over y_train and y_train_pred

            test_model_score = r2_score(y_test, y_test_pred) # Model R2-score over y_test and y_test_pred
            
            report[list(models.keys())[i]] = test_model_score # Storing the model test report on y_test and y_test_pred in the "report" dictionary
        
        return report

    except Exception as e:
        raise CustomException(e, sys)