import logging
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test_log.log',     # log file name
    filemode='w'                 # overwrite on each run, use 'a' to append
)

# Create a logger object
logger = logging.getLogger()
