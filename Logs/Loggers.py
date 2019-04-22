import logging
import logging.config

class logger_util(object):
    my_logger = '' #Logger Object.

    def __init__(self):
        logging.config.fileConfig('logging.conf') #Load log config file.
        self.my_logger = logging.getLogger(__name__) #Initilaze logger object


    def add_logger(self):
        return self.my_logger #Return Logger object

logger_util = logger_util() #Global Object for writing log files.