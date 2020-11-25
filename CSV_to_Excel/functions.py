import os
import csv
import variablen
import shutil
import logging
logging.basicConfig(level=logging.DEBUG)


# Sucht alle Filenamen in dem Verzeichnis | Speichert diese in eine Liste
# Da es nur ein Filename ist, reicht mir result[0] als Ergebnis - dies ist dann das rawFile
def selectRawCsv(folder):
    result = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    variablen.rawFile = result[0]
    variablen.rawFileDir = variablen.workDir + variablen.rawFile
    logging.info("Funktion selectRawCsv wurde abgeschlossen. Filename = {}".format(variablen.rawFile))
    
# macht aus dem rawFile ('Healthy Heart History Report (.csv)') CSV Namen einen richtigen
# ('HealthyHeartHistoryReport.csv') und speichert diesen in der var csvName ab
def createCsvName(rawFileName):
    csvName = ''
    variablen.csvSrcFile = csvName
    for el in rawFileName:  
        if el != "(":
            if el != ")":
                if el != " ":
                    csvName = csvName + el
    variablen.csvSrcFile = csvName   
    logging.info("Funktion createCsvName wurde abgeschlossen. Filename = {}".format(variablen.csvSrcFile))
    
# Kopiere das rawFile in den src Folder. Benenne es dabei um
# Verschiebe das raw File in den Archivordner und benenne es um so das es eindeutig ist
def copyAndRename(rawFile):
    shutil.copy(rawFile , variablen.csvSrcDir + variablen.csvSrcFile)   
    '''shutil.move(rawFile, variablen.archivDir + '-' + variablen.csvSrcFile) Für Testzwecke auskommentiert'''
    logging.info("rawFile erfolgreich kopiert nach {srcDir} und umbenannt zu {srcFile}".format(srcDir=variablen.csvSrcDir, srcFile=variablen.csvSrcFile))
    

# Erstellt im destination Verzeichniss nur die leere csvDatei mit einem Header
def createCsvHeader(filename):  
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Datum', 'Uhrzeit','Systolisch', 'Diastolisch' , 'Puls']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        csvfile.close()
        variablen.persDstFile = filename
    logging.info("CSV Header correct erstellt")
    
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
        if (hrs + 12) < 24:
            hrs += 12
        else:
            hrs == 0
    hrsMint = "{}:{}".format(hrs, mint)
    return hrsMint

# Liest das CSV ein und bereitet die Daten auf
# schreibt eine CSV Datei und added neue lines
def writeCsv(srcFileName, dstFileName):
    with open(srcFileName) as csvdatei:
        csv_reader_object = csv.DictReader(csvdatei)
        for row in csv_reader_object:
            rawDate = row["Date"]
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
        csvdatei.close()
        csvfile.close()
    logging.info("CSV Datei erfolgreich geschrieben!!!")
    

    
   
