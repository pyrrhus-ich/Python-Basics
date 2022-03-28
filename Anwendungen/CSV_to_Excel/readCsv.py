import functions
import variablen
#import csv
#import os




    
    
    
    

# selectiert die raw Datei
functions.selectRawCsv(variablen.workDir)
# macht aus dem alten Namen einen neuen und speichert diesen in einer Variablen
functions.createCsvName(variablen.rawFile)
# verschiebt Raw Datei in archiv und kopiert in src
functions.copyAndRename(variablen.rawFileDir)
# erstellt ein Destination File und den korrekten Header
functions.createCsvHeader(variablen.csvDstFile)
# schreibt die Daten in das File
functions.writeCsv(variablen.csvSrcDir + variablen.csvSrcFile, variablen.persDstFile)






       

         







