import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("nopCommerceLogger")
        logger.setLevel(logging.INFO)

        # Prevent adding multiple handlers in case of multiple calls
        if not logger.handlers:
            # Ensure Logs directory exists
            os.makedirs(".\\Logs", exist_ok=True)

            # File handler
            file_handler = logging.FileHandler(".\\Logs\\automation.log", mode='a')
            formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s', datefmt='%y/%m/%d %I:%M:%S %p')
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger
