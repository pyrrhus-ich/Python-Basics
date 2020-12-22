import visaFunc
import os
from datetime import datetime
import logging

#---------------------------------------------------------------------------------------------------#

workDir = "/home/ich/Dokumente/Git/learnPython/Visa_import"

logFile = workDir + "/log/visaFunc.log"
logging.basicConfig(filename= logFile,level=logging.INFO)
logging.debug('Debug message')

# legt dateTime fest damit jede datei unique benamst werden kann
now = datetime.now()
dateTime = now.strftime("%Y%m%d-%H%M%S")

srcFolder = workDir + "/src/"
srcFile = os.listdir(srcFolder)[0]
src = srcFolder + srcFile
dstFolder = "/home/ich/Dokumente/Git/learnPython/Visa_import/dst/"
dstFile = dstFolder + dateTime + '-Importfile' + '.csv'



visaFunc.writeCsv(src,dstFile)



  


