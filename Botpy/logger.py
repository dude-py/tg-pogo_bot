import logging

class Logger:
    
    def getLogger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        log_file = logging.FileHandler('log_mesg.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file.setFormatter(formatter)
        logger.addHandler(log_file)
        return logger