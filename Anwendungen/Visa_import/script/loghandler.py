import logging
from settings import workDir
from logging.handlers import RotatingFileHandler

logFile = workDir + "/log/visaFunc.log"
formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

fh = RotatingFileHandler(logFile, mode='a', maxBytes=5*102*102, 
                                 backupCount=2, encoding=None, delay=0)




logger = logging.getLogger('visa.log')
logger.setLevel(logging.DEBUG)
#fh = logging.FileHandler(logFile)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
#formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

#while True:
 #   logger.info("data")

# Beispielnachrichten zum testen
#logger.debug('Debug-Nachricht')
#logger.info('Info-Nachricht')
#logger.warning('Warnhinweis')
#logger.error('Fehlermeldung')
#logger.critical('Schwerer Fehler')