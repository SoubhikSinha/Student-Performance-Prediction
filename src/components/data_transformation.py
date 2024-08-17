# 2. DATA TRANSFORMATION

# Importing necessary libraries
import sys
from dataclasses import dataclass
import os

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer 
# The above will altogether put data transformation functions in action (on-by-one) by itself !
# Basically, we will create a pipeline

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object # Function from "src/util.py" to save object in the given file path

@dataclass
class DataTransformationConfig: # This will enable to get the input for data pre-processing / transformation
    preprocessor_ob_file_path = os.path.join('artifacts', "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transormation_config = DataTransformationConfig() # Constructor variable for stroing path of pre-processor

    def get_data_transformer_object(self):
        '''
        This function is reponsible for Data Transformation 
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipeline = Pipeline( # This pipeline will work on "Training Dataset" --> Numerical Features
                steps = [
                    ("imputer", SimpleImputer(strategy = "median")), # Handling mising values - replacing them with "feature median" value
                    ("scaler", StandardScaler()) # Standard Scaling
                ]
            )

            cat_pipeline = Pipeline( # This pipeline will work on "Training Dataset" --> Categorical Features
                steps = [
                    ("imputer", SimpleImputer (strategy = "most_frequent")), # Handling mising values - replacing them with "feature mode" value
                    ("one_hot_encoder", OneHotEncoder()), # One Hot Encoding for converting categorical values to numerical values
                    ("scaler", StandardScaler(with_mean=False)) # Standard Scaling --> "with_mean=False" ▶️ valid for sparse matrices
                ] 
            )

            # logging.info("Numerical columns scaling completed") # Logger --> Numerical Features
            
            # logging.info("Categorical columns encoding completed") # Logger --> Categorical Features

            logging.info(f"Categorical columns : {categorical_columns}") # Logger --> Categorical Features
            logging.info(f"Numerical columns : {numerical_columns}") # Logger --> Numerical Features

            preprocessor = ColumnTransformer( # Combining both the pipelines, to work one after the other, by themselves
                [
                    ("num_pipeline", num_pipeline, numerical_columns), # Numerical Pipline for Numerical Columns
                    ("cat_pipeline", cat_pipeline, categorical_columns) # Categorical Pipline for Categorical Columns
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)


    # Function to initiate Data Transformation
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object() # Note : The "preprocessing_obj" should be converted to a pickle file 

            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns = [target_column_name], axis = 1) # Of-course we don't want the target feature to become pre-processed
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns = [target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Applying Preprocessing Object on Training DataFrame and Testing DataFrame."
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df) # "fit_transform" only for training data
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df) # "transform" only for testing data

            train_arr = np.c_[ # Concatenating preprocessed training data with the target feature of training data
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[ # Concatenating preprocessed testing data with the target feature of testing data
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            logging.info(f"Saved Preprocessing Object.") # As a pickle file

            save_object( # Preprocessed object saving ==> "artifacts/preprocessing.pkl"
                file_path = self.data_transormation_config.preprocessor_ob_file_path, # File Path
                obj = preprocessing_obj # Object to be saved
            )

            return (
                train_arr,
                test_arr,
                self.data_transormation_config.preprocessor_ob_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)           