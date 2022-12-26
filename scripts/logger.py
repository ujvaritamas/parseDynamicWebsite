import logging, logging.config
import os
import shutil

def create_logger():
    #create logdir
    if not os.path.exists('log'):
        os.mkdir('log')
    # set up logging
    logging.config.fileConfig("log_config.ini")
    logger = logging.getLogger('sLogger')
    # log something
    logger.debug('*'*100)
    logger.debug('logger created')
    logger.debug('*'*100)
    #logger.info('info message')
    #logger.warn('warn message')
    #logger.error('error message')
    #logger.critical('critical message')
    return logger

