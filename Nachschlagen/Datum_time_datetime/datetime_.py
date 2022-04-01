from datetime import datetime


import datetime

datum = datetime.datetime(2022, 3, 27, 14, 38, 45)
tag = datum.day
monat = datum.month
jahr = datum.year
stunde = datum.hour
minute = datum.minute
sekunde = datum.second
# Es gibt auch noch millisekunden

print("Das Datum ist der {}.{}.{} um {}:{}:{} Uhr".format(tag,monat,jahr,stunde,minute,sekunde))

