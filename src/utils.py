import os
import logging
import json
from functools import wraps
import threading

# Setup logging
def setup_logging(log_file='app.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger()

# Read JSON configuration file
def read_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

# Ensure directory exists
def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Run a function in a new thread
def run_in_new_thread(func):
    @wraps(func)
    def run(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        return t
    return run
