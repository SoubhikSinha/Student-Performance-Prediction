# FOR LOGGING (KEEPING RECORD OF WHAT IS HAPPENING WHEN - TO KEEP A TRACK)

import logging
import os
from datetime import datetime

# Creating the log file 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# cwd ==> Current Working Directory🔻
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Name of the file ==> 'logs'

os.makedirs(log_path, exist_ok = True) # If file exists, keep on appending log info. into the file.

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig( # If you want to overtake the default functionality of "logging"
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s ] %(lineno)d %(name)s = %(levelname)s - %(message)s", # Log file name's naming format
    level = logging.INFO, 
)


'''
# Just testing the "logger.py" file
if __name__ == "__main__":
    logging.info("Loging has Started")
'''