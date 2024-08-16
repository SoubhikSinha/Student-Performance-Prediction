# 1. READING THE DATA (INGESTING DATA)

# Importing necessary libraries
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass # Decorator - to directly define class variable
class DataIngestionConfig: # Any data input will given to this class
    train_data_path: str = os.path.join('artifacts', "train.csv") # The Train data will be saved in this path
    test_data_path: str = os.path.join('artifacts', "test.csv") # The Test data will be saved in this path
    raw_data_path: str = os.path.join('artifacts', "raw.csv") # The "Raw" data will be saved in this path

    '''
    "artifacts" is a folder
    '''
    
    # The above are the inputs we will be giving to the "data ingestion" component


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # Constructor variable taking train, test and raw data inputs

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method / component")
        '''
        Always try to keep writing logs - this will help to store
        the logs if any exception occurs / action is taken.
        '''
        try:
            # In this section itself you can read the data from any source (CSV file, mongodb, etc.) - you just need to change the code accordingly
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) 
            # We need to store the train data - thus a directory (artifacts) is creatd to store it
            # if the directory / file already exists (exist_ok = True), nothing will happen (at the most the file may get replaced)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train-Test Split - Initiated")
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42) # Splitting the "Raw" data - into Train and Test components

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True) # Storing the train data set (after Train-Test Split) - in the "artifacts" folder

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True) # Storing the test data set (after Train-Test Split) - in the "artifacts" folder

            logging.info("Ingestion of the data is completed !")

            return (
                self.ingestion_config.train_data_path, # Returning the "Train" data path
                self.ingestion_config.test_data_path, # Returning the "Train" data path
            )
        except Exception as e:
            raise CustomException(e, sys) # Exception Class function called (exception.py)
        

# Lets test the code
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

