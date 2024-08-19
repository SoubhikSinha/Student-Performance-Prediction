# PREDICTION PIPELINE

# Importing necessary libraries
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features): # Model Prediction Function - From Data Ingestion TO PREDICTION
        try:
            model_path = 'artifacts\model.pkl', # Model Path
            preprocesor_path = 'artifacts\preprocessor.pkl' # Preporcessor Path
            model = load_object(file_path = model_path) # Model Loading
            preprocessor = load_object(file_path = preprocesor_path) # Preprocessor loading
            data_scaled = preprocessor.transform(features) # Data Scaling
            preds = model.predict(data_scaled) # Model Prediction
            return preds # Returning Prediction Results
        except Exception as e:
            raise CustomException(e, sys)


class CustomData: # Responsible for getting values from HTML (Flask Web Application) to the backend
    def __init__(  
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    # Function for returning all the data received from frontend - in the form of Dataframe
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)