import os
from datetime import datetime


# Das WorkingDirectory - Hier spielt sich alles ab
workDir = "C:/Users/pyrrh/GoogleDrive/blutdruckFrank/"
# Das raw File - liegt direkt im WorkingDirectory
rawFile = ''
rawFileDir = workDir + rawFile
# Das ist das csv File mit ordentlicher .csv am Ende
csvSrcFile = ''
csvSrcDir = workDir + "src/"
# Ab hier wird das Zielfile definiert (Pfad und Filename)
csvDstPath = workDir+"dst/"
csvDstName = 'write.csv'
csvDstFile = csvDstPath+csvDstName
# legt dateTime fest damit jede Archivdatei unique benamst werden kann
now = datetime.now()
dateTime = now.strftime("%Y%m%d-%H%M%S")
# Das ArchivDirektory
archivDir = workDir + "archiv/" + dateTime + csvSrcFile

germDate = ""
syst = ""
dias = ""
puls = ""


