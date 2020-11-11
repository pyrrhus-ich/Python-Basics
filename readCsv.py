import csv
import functions


fileName = "HealthyHeartHistoryReport.csv"

""" with open(config.file) as csvdatei:
    csv_reader_object = csv.reader(csvdatei, delimiter=',')
    # print(csv_reader_object) Nur zum debuggen
    for row in csv_reader_object:
        print(row) """

with open(fileName) as csvdatei:
    csv_reader_object = csv.DictReader(csvdatei)
    for row in csv_reader_object:
        rawDate = row["Date"]
        amiDate = ""
        if rawDate.startswith('/',1):
            amiDate = rawDate[0:7]
        else:
            amiDate = rawDate[0:8]
        functions.changeDate(amiDate)
        
       

         







