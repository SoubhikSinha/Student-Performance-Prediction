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
                "K-NN Regressor" : KNeighborsRegressor(),
                "XGBRegressor" : XGBRFRegressor(),
                "CatBoosting Regressor" : CatBoostRegressor(verbose = False),
                "AdaBoost Regressor" : AdaBoostRegressor(),
            }

            # Setting different Parameters for all the models
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "K-NN Regressor" : {
                    'n_neighbors' : [5,7,9,11],
                    # 'weights' : ['uniform','distance'],
                    # 'algorithm' : ['ball_tree' , 'kd_tree' , 'brute']
                },
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }

            model_report:dict = evaluate_models(X_train = X_train, y_train = y_train, X_test = X_test, y_test = y_test, 
                                               models = models, param=params) # evaluate_model() will be created in utils.py

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