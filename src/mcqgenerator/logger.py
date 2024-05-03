# Logging is a importpant file part of the structure 
import logging 
import os 
from datetime import datetime 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# It'll create a log file by that spedicfied name 
log_path=os.path.join(os.getcwd(), "logs")
# Now it'll assigned the joingin of current dir and logs in log_path 
os.makedirs(log_path, exist_ok=True) 

LOG_FILEPATH=os.path.join(log_path, LOG_FILE)
logging.basicConfig(level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    )
