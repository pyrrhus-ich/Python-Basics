import os
import csv


def list_all(folder):
    #listet alle Dateien auf
    for files in os.listdir(folder):
        print (files)


def readCsv(fileName):
    with open(fileName) as csvdatei:
        csv_reader_object = csv.DictReader(csvdatei)
        for row in csv_reader_object:
            rawDate = row["Date"]
            amiDate = ""
            if rawDate.startswith('/',1):
                amiDate = rawDate[0:7]
            else:
                amiDate = rawDate[0:8]
            changeDate(amiDate)


def changeDate(date):
    rDate = date
    if len(rDate) < 8:
        rDate = date.zfill(8)
    MM = rDate[0:2]
    TT = rDate[3:5]
    YY = rDate[6:8]
    germDate = TT + '.' + MM + '.' + YY
    print(germDate)

