import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger