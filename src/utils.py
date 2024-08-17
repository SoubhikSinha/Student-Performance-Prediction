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