# HANDLING EXCEPTIONS

import sys
import logging

# We need to import the loggin.py file
# so that the exception handling logs can also
# be recorded

from src.logger import logging

'''
Provides various functions and variables that are used 
to manipulate different parts of the Python runtime environment
'''

# Let us create our own custom exceptions 🔻

def error_message_detail(error, error_detail:sys): # Custom error message function
    _, _, exc_tb = error_detail.exc_info()

    # exc_tb --> Execution Tab

    file_name = exc_tb.tb_frame.f_code.co_filename # Getting the file name where exception (error) occured
    # The above will help you provide, in which file, which line, etc.
    # the exception has occured
    error_message = "Error Occured in Python Script Name [{0}], line number [{1}], error message : [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message

class CustomException(Exception): # Custom Exception Class - Inheriting "Exception Class"
    def __init__(self, error_message, error_detail:sys):
        # Inheriting the constructor of Super (Inherited) Class - "Exception"
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
        # error_detail is tracked by "sys"

    def __str__(self):
        return self.error_message # Getting the error message

'''
# Just testing the "exception.py" file
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
'''