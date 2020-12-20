
import os
import csv
import shutil
import logging
logging.basicConfig(level=logging.DEBUG)


# Sucht alle Filenamen in dem Verzeichnis | Speichert diese in eine Liste
# Da es nur ein Filename ist, reicht mir result[0] als Ergebnis - dies ist dann das rawFile
def selectRawCsv(folder):
    result = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    variablen.rawFile = result[0]
    variablen.rawFileDir = variablen.workDir + variablen.rawFile
    print(result)
    logging.info("Funktion selectRawCsv wurde abgeschlossen. Filename = {}".format(variablen.rawFile))


# Liest das CSV ein und bereitet die Daten auf
# schreibt eine CSV Datei und added neue lines
def writeCsv(srcFileName, dstFileName):
    with open(srcFileName, newline = '') as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter = ';')
        rownum = 0
        for row in csv_reader_object:
            if rownum < 2 :
                rownum += 1
            else:
                print(row[2])

             