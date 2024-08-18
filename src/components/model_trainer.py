# 3. MODEL TRAINING

'''
There is no "Best" Algorithm !
You should try every single algorithm to see
which one performs the best !!!
'''

# Importing necessary libraries
import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRFRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig: # This Config class is important in every (.py) file which is a component of project - to save a file to the desired file path
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig() # Getting the path where model.pkl file will be stored

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting Training and Testing Input Data") # Input will be coming from data_transformation.py file
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1], # Omitting the last attribute (as being the target feature - considering all rows)
                train_array[:,-1], # Taking only last attribute (as being the target feature - considering all rows)
                test_array[:,:-1], # Omitting the last attribute (as being the target feature - considering all rows)
                test_array[:,-1] # Taking only last attribute (as being the target feature - considering all rows)
            )

            models = { # Dictionary of model
                "Random Forest" : RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Linear Regression" : LinearRegression(),
                "K-Nearest Neighbours" : KNeighborsRegressor(),
                "XGBRegressor" : XGBRFRegressor(),
                "CatBoosting Regressor" : CatBoostRegressor(verbose = False),
                "Adaboost Regressor" : AdaBoostRegressor(),
            }

            model_report:dict = evaluate_models(X_train = X_train, y_train = y_train, X_test = X_test, y_test = y_test, 
                                               models = models) # evaluate_model() will be created in utils.py

            # Getting the best model score from the dict - Max. score of R2-Score ▶️ BEST MODEL
            best_model_score = max(sorted(model_report.values()))

            # Getting the best model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            # Getting the "best" model object from the dictionary
            best_model = models[best_model_name]

            # Minimum Threshold for "Best Model Score" - here, 60%
            if best_model_score < 0.6:
                raise CustomException("No Best Model Found !!!")
            
            logging.info(f"BEST MODEL FOUND on both Training and Testing Dataset")

            # Saving the best model - save_model() function is taken from utils.py
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model            
            )

            # Printing the predicted output on the test data
            predicted = best_model.predict(X_test)

            # R2-Score on the predicted output
            return r2_score(y_test, predicted)

        except Exception as e:
            raise CustomException(e, sys)
            
