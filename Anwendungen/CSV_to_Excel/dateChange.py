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



time = "1/24/20 1:00PM"
def changeTime(rawDate):
    rawTime = time[8:].lstrip().rstrip("APM")
    hrs = 0
    mint = rawTime[-2:]
    hrsMint = "{}:{}".format(hrs, mint)

    if len(rawTime)==5:
        hrs = int(rawTime[:2])
    else:
        hrs = int(rawTime[:1])
    print(type(hrs))
    if time[-2:-1]== 'P':
        if (hrs + 12) < 24 : 
            hrs += 12
        else:
            hrs = 00
    print(hrs)
    print("{}:{} Uhr".format(hrs, mint))
    print(hrsMint)

changeTime(time)

#print(hrs+':'+mint+' '+timeFrame)
