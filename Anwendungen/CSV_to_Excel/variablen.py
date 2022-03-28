import os
from datetime import datetime

# legt dateTime fest damit jede datei unique benamst werden kann
now = datetime.now()
dateTime = now.strftime("%Y%m%d-%H%M%S")

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
csvDstName = 'blutdruck.csv'
csvDstFile = csvDstPath+dateTime+'-'+csvDstName
persDstFile = ''

# Das ArchivDirektory
archivDir = workDir + "archiv/" + dateTime + csvSrcFile

germDate = ""
germTime = ""
syst = ""
dias = ""
puls = ""


