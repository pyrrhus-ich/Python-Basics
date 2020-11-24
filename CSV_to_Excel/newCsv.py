import csv

workDir = "C:/Users/pyrrh/GoogleDrive/blutdruckFrank/"
# Ab hier wird das Zielfile definiert (Pfad und Filename)
csvDstPath = workDir+"dst/"
csvDstName = 'write.csv'
csvDstFile = csvDstPath+csvDstName


print(csvDstFile)

# Erstellt im destination Verzeichniss nur die leere csvDatei mit einem Header
def createCsvHeader(filename):  
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Datum', 'Systolisch', 'Diastolisch' , 'Puls']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        csvfile.close()
       
def createCsvLines(filename):
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
        csvdatei.close()
    print("OPERATION ERFOLGREICH BEENDET !!!")

createCsvHeader(csvDstFile)