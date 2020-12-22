import visaFunc
import os
from datetime import datetime

#---------------------------------------------------------------------------------------------------#

# legt dateTime fest damit jede datei unique benamst werden kann
now = datetime.now()
dateTime = now.strftime("%Y%m%d-%H%M%S")

srcFolder = "/home/ich/Dokumente/Git/learnPython/Visa_import/src/"
srcFile = os.listdir(srcFolder)[0]
src = srcFolder + srcFile
dstFolder = "/home/ich/Dokumente/Git/learnPython/Visa_import/dst/"
dstFile = dstFolder + dateTime + '-Importfile' + '.csv'

print(src)
print(dstFile)

visaFunc.writeDRCsv(src,dstFile)



  


