import os


def list_all(folder):
    #listet alle Dateien auf
    for files in os.listdir(folder):
        print (files)

def changeDate(date):
    rDate = date
    if len(rDate) < 8:
        rDate = date.zfill(8)
    MM = rDate[0:2]
    TT = rDate[3:5]
    YY = rDate[6:8]
    germDate = TT + '.' + MM + '.' + YY
    print(germDate)

