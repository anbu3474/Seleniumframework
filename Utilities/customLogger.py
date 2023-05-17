import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        # logging.datefmt=('%m/%d/%y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

    # def loggen():
    #     logger = logging.getLogger()
    #     logging.basicConfig(filename='.\\Logs\\automation.log',
    #                         format='%(asctime)s: %(levelname)s: %(message)s',
    #                         datefmt='%m/%d/%y %I:%M:%S %p')
    #     logger.setLevel(logging.INFO)
    #     return logger
