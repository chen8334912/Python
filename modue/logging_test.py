import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'logger.log',
    filemode = 'w',
    format = '%(filename)s %(asctime)s [%(lineno)s] %(message)s',
    # datefmt = ''
)



logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')