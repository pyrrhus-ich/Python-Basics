
# import Build in Module
import os, csv
# import eigene Module
from loghandler import logger as lg



# Liest das CSV ein und bereitet die Daten auf
# schreibt eine CSV Datei und added neue lines
def writeCsv(srcFileName, dstFileName):
    with open(srcFileName, newline = '') as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter = ';')
        #schreibt die Info in das logfile
        lg.info("CSV file" + srcFileName + " opened")
        rownum = 0
        Datum = ""
        Haendler = ""
        Betrag = ""
        for row in csv_reader_object:
            lg.info("Gelesen Reihe: {} : {}".format(rownum, row))
            # erforderlich weil die ersten 2 Zeilen im Amazon CSV Schrott sind
            # wenn die Nummer der Reihe < 2 ist setze den Zähler um 1 hoch und mache weiter
            if rownum < 2 :
                rownum += 1
            else:
                # wenn die Spalte 2 einer Reihe nicht leer ist schreibe die Werte in eine Datei
                if row[2] != "":
                    Datum = row[2]
                    Haendler = row[3]
                    Betrag = row[8]
                    # schreibt den Händler bei der Ausgleichsbuchung weil der von der Bank leer gelassen wurde
                    if row[3] == '':
                        Haendler = "Sparkasse Ausgleich Kreditkarte"
                    #logger.info(Datum + ' ' + Haendler + ' ' + Betrag)
                with open (dstFileName , 'a+', newline='') as csvfile:
                    fieldnames = ['Datum', 'Haendler','Betrag']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if Datum != '':
                        writer.writerow({'Datum': Datum,'Haendler': Haendler, 'Betrag': Betrag})
                        lg.info("Geschrieben Reihe {}: {} {} {}".format(rownum, Datum, Haendler, Betrag))
                        Datum = ""
                        Haendler = ""
                        Betrag = ""
                rownum += 1 # für den Ausdruck der Rownummer im Logging
        csvdatei.close()
        csvfile.close()
        lg.info("CSV geschrieben in Datei : " + dstFileName)
        lg.info("<<<<<<<<<<<<<<<<<<<<<< Neues CSV geschrieben >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

             

