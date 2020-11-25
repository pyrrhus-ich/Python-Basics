import functions
import variablen
#import csv
#import os

# Macht aus dem Amerikanischen Datum ein Deutsches. Allerdings nur als String
# wird in der Funktion readCsv aufgerufen
def changeDate(date):
    rDate = date
    if len(rDate) < 8:
        rDate = date.zfill(8)
    MM = rDate[0:2]
    TT = rDate[3:5]
    YY = rDate[6:8]
    # trägt das ermittelte Deutsche Datum in die Variable germDate ein, damit es dann wieder in die CSV geschrieben werden kann
    variablen.germDate = TT + '.' + MM + '.' + YY

def changeTime(time):
    rawTime = time[8:].lstrip().rstrip("APM")
    hrs = 0
    mint = rawTime[-2:]
    timeFrame = time[-2:]
    if len(rawTime)==5:
        hrs = int(rawTime[:2])
    else:
        hrs = int(rawTime[:1])
    if timeFrame == 'PM':
        hrs += 12
    hrsMint = "{}:{}".format(hrs, mint)
    return hrsMint


# Liest das CSV ein und bereitet die Daten auf
# schreibt eine CSV Datei und added neue lines
def writeCsv(srcFileName, dstFileName):
    with open(srcFileName) as csvdatei:
        csv_reader_object = csv.DictReader(csvdatei)
        for row in csv_reader_object:
            rawDate = row["Date"]
            print(rawDate)
            amiDate = ""
            germTime = changeTime(rawDate)
            #print("germTime = ", germTime)
            amiTimeFrame = ""
            variablen.syst = row["Systolisch"]
            variablen.dias = row["Diastolisch"]
            variablen.puls = row["Puls"]
            # Hier fängt die Umwandlung des Datums an
            if rawDate.startswith('/',1):
                amiDate = rawDate[0:7]
            else:
                amiDate = rawDate[0:8]
            changeDate(amiDate) # Hier wird die unten definierte Funktion aufgerufen
            #Ab hier werden die Lines an das CSV File angehängt
            with open (dstFileName , 'a+', newline='') as csvfile:
                fieldnames = ['Datum', 'Uhrzeit','Systolisch', 'Diastolisch' , 'Puls']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Datum': variablen.germDate,'Uhrzeit': germTime, 'Systolisch': variablen.syst, 'Diastolisch': variablen.dias, 'Puls': variablen.puls  })
            #print(variablen.germDate + ' ' + variablen.syst + ' ' + variablen.dias + ' ' + variablen.puls)
        csvdatei.close()
        csvfile.close()
    print("OPERATION ERFOLGREICH BEENDET !!!")


    
    
    
    

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






       

         







