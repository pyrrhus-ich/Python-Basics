

zirDatum = "2022-03-14"


def changeZIRDate(datumZiR):
    x= datumZiR.split("-")
    x.reverse()
    x.insert(1,".")
    x.insert(3,".")
    y=""
    for el in x:
        y=y+el
    print(y)

changeZIRDate(zirDatum)