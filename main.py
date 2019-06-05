import logging_local

logging_local.setup_logging()

# with open('config.yaml', 'r') as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)

# Get the logger specified in the file
logger = logging_local.logging.getLogger(__name__)
logger.debug('debug main module')
logger.error('Loaded error log')


print('Hello Swirl')
