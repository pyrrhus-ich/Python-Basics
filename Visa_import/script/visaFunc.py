
import os
import csv
import shutil
#import logging
import loghandler




# Liest das CSV ein und bereitet die Daten auf
# schreibt eine CSV Datei und added neue lines
def writeCsv(srcFileName, dstFileName):
    with open(srcFileName, newline = '') as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter = ';')
        loghandler.logger.info("CSV file" + srcFileName + " opened")
        rownum = 0
        Datum = ""
        Haendler = ""
        Betrag = ""
        for row in csv_reader_object:
            if rownum < 2 :
                rownum += 1
            else:
                if row[2] != '':
                    Datum = row[2]
                    Haendler = row[3]
                    Betrag = row[8]
                with open (dstFileName , 'a+', newline='') as csvfile:
                    fieldnames = ['Datum', 'Haendler','Betrag']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'Datum': Datum,'Haendler': Haendler, 'Betrag': Betrag})
        csvdatei.close()
        csvfile.close()

             

