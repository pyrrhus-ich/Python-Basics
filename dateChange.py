startDate = "7/28/20" 
# Wandelt ein Datum im Format MM/TT/YY um in ein Deutsches Datum
# Dabei wird eine fehlende Null am Anfang eingefügt
def changeDate(date):
    rDate = date
    if len(rDate) < 8:
        rDate = date.zfill(8)
    MM = rDate[0:2]
    TT = rDate[3:5]
    YY = rDate[6:8]
    germDate = TT + '.' + MM + '.' + YY
    print(germDate)

   
changeDate(startDate)