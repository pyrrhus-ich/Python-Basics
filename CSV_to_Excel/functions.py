import os
import csv
import variablen
import shutil


# Sucht alle Filenamen in dem Verzeichnis | Speichert diese in eine Liste
# Da es nur ein Filename ist, reicht mir result[0] als Ergebnis - dies ist dann das rawFile
def selectRawCsv(folder):
    result = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    variablen.rawFile = result[0]
    variablen.rawFileDir = variablen.workDir + variablen.rawFile
    print("1. - Separiert den rawFilename >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Funktion selectRawCsv wurde abgeschlossen. Filename = {}".format(variablen.rawFile))

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
    print("2. - CSV Name wurde korrekt erstellt >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Funktion createCsvName wurde abgeschlossen. Filename = {}".format(variablen.csvSrcFile))

# Kopiere das rawFile in den src Folder. Benenne es dabei um
# Verschiebe das raw File in den Archivordner und benenne es um so das es eindeutig ist
def copyAndRename(rawFile):
    shutil.copy(rawFile , variablen.csvSrcDir + '-' + variablen.csvSrcFile)   
    shutil.move(rawFile, variablen.archivDir + '-' + variablen.csvSrcFile)
    print("3. - Files wurden verschoben und umbenannt >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("rawFile erfolgreich kopiert nach {srcDir} und umbenannt zu {srcFile}".format(srcDir=variablen.csvSrcDir, srcFile=variablen.csvSrcFile))
    print("rawFile korrekt archiviert")

# Erstellt im destination Verzeichniss nur die leere csvDatei mit einem Header
def createCsvHeader(filename):  
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Datum', 'Systolisch', 'Diastolisch' , 'Puls']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        csvfile.close()


# Liest das CSV ein und bereitet die Daten auf
# schreibt eine CSV Datei und added neue lines
def readCsv(fileName):
    #Dieser auskommentierte Block erzeugt die Datei. 
    #Da muss noch ne Prüfung rein wenn Datei schon vorhanden überspringe es
    with open('weight.csv', 'w', newline='') as csvfile:
        fieldnames = ['Datum', 'Systolisch', 'Diastolisch' , 'Puls']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    with open(fileName) as csvdatei:
        csv_reader_object = csv.DictReader(csvdatei)
        for row in csv_reader_object:
            rawDate = row["Date"]
            amiDate = ""
            variablen.syst = row["Systolisch"]
            variablen.dias = row["Diastolisch"]
            variablen.puls = row["Puls"]
            if rawDate.startswith('/',1):
                amiDate = rawDate[0:7]
            else:
                amiDate = rawDate[0:8]
            changeDate(amiDate) # Hier wird die unten definierte Funktion aufgerufen
            #Ab hier werden die Lines an das CSV File angehängt
            with open ('weight.csv', 'a+', newline='') as csvfile:
                fieldnames = ['Datum', 'Systolisch', 'Diastolisch' , 'Puls']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Datum': variablen.germDate, 'Systolisch': variablen.syst, 'Diastolisch': variablen.dias, 'Puls': variablen.puls  })
            #print(variablen.germDate + ' ' + variablen.syst + ' ' + variablen.dias + ' ' + variablen.puls)
    print("OPERATION ERFOLGREICH BEENDET !!!")
    
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
    
   
