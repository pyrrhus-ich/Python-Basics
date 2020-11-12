import os
import csv
import variablen


def list_all(folder):
    #listet alle Dateien auf
    for files in os.listdir(folder):
        print (files)

# Liest das CSV ein und bereitet die Daten auf
# schreibt eine CSV Datei und added neue lines
def readCsv(fileName):
    #Dieser auskommentierte Block erzeugt die Datei. 
    #Da muss noch ne Prüfung rein wenn Datei schon vorhanden überspringe es
    """ with open('weight.csv', 'w', newline='') as csvfile:
        fieldnames = ['Datum', 'Systolisch', 'Diastolisch' , 'Puls']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() """
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
            changeDate(amiDate)
            #Ab hier werden die Lines an das CSV File angehängt
            with open ('weight.csv', 'a+', newline='') as csvfile:
                fieldnames = ['Datum', 'Systolisch', 'Diastolisch' , 'Puls']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Datum': variablen.germDate, 'Systolisch': variablen.syst, 'Diastolisch': variablen.dias, 'Puls': variablen.puls  })
            #print(variablen.germDate + ' ' + variablen.syst + ' ' + variablen.dias + ' ' + variablen.puls)
    print("OPERATION ERFOLGREICH BEENDET !!!")
    
# Macht aus dem Amerikanischen Datum ein Deutsches. Allerdings nur als String
def changeDate(date):
    rDate = date
    if len(rDate) < 8:
        rDate = date.zfill(8)
    MM = rDate[0:2]
    TT = rDate[3:5]
    YY = rDate[6:8]
    variablen.germDate = TT + '.' + MM + '.' + YY
    
   
