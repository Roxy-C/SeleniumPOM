import sys
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class Logger:
    def __init__(self, log_prefix, logs_path):
        self.logs_path = logs_path
        self.file_prefix = log_prefix
            
    def log(self, test_name, message):
        try:
            current_time = datetime.now().strftime(" %d-%m-%Y %H-%M")
            log_name = self.logs_path + self.file_prefix + current_time + '.log'
            
            with open(log_name, 'a') as f:
                f.write(f'{current_time}    {test_name}: {message}\n')
                
        except Exception as e:
            print("Exception: " + str(e))
            sys.exit(1)