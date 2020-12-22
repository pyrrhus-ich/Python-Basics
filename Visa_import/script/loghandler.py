import logging

workDir = "/home/ich/Dokumente/Git/learnPython/Visa_import"

logFile = workDir + "/log/visaFunc.log"

logger = logging.getLogger('visa.log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(logFile)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Beispielnachrichten zum testen
#logger.debug('Debug-Nachricht')
#logger.info('Info-Nachricht')
#logger.warning('Warnhinweis')
#logger.error('Fehlermeldung')
#logger.critical('Schwerer Fehler')