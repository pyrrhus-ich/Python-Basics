def dateOfCreationUmwandeln(listVariable, indexofCreationDay):
    # Hier wird das Datum bearbeitet und aus dem Zir datum 2022-03-25 12:35:00  wird 25.03.2022.
    # Ausserdem werden noch die 3 Spalten "creationDate, creationMonth, creationYear befüllt"
    print("\nBeginne mit Umwandeln des Datums")
    y=""
    jahr = ""
    monat =""
    tag = ""
    for el in listVariable:
        if el != listVariable[0]: # Damit die Überschrift (erste Zeile) nicht bearbeitet wird
            z = el[2].split(" ")
            x=z[0].split("-")
            x.reverse()
            tag = x[0]
            monat = x [1]
            jahr=x[2]
            x.insert(1,".")
            x.insert(3,".")
            # Hier werden die 3 Spalten "creationDate, creationMonth, creationYear befüllt"
            for i in x:
                y=y+i
            el.pop(indexofCreationDay)
            el.insert(indexofCreationDay, y)
            el.insert(indexofCreationDay + 1, tag)
            el.insert(indexofCreationDay + 2, monat)
            el.insert(indexofCreationDay + 3, jahr)
        y=""    
    print("Umwandlung des Datums abgeschlossen")


def repNrKuerzen(listVariable, indexDerReparaturnummer):
    print("\nDie Bearbeitung der Reparaturnummern beginnt.")
    # Spalte einfügen für die Reparaturnummer für die Suche in BO
    listVariable[0].insert(indexDerReparaturnummer + 1,"cut Repairnumber for query")
    for el in listVariable:
        if el != listVariable[0]:
        #Hier bearbeiten wir die Auftragsnummer und schneiden die letzten 2 "-R" oder mehr ab
            i = (el[indexDerReparaturnummer])
            slice_RepairNumber = slice(0,10) # schneidet die Nummer auf M199-12345
            el0 = i[slice_RepairNumber]
            slice_queryNumber = slice(5,10) # schneidet die Nummer so, das man in BO danach suchen kann
            el1 = i[slice_queryNumber]+";"
            el.pop(indexDerReparaturnummer)
            el.insert(indexDerReparaturnummer,el0)
            el.insert(indexDerReparaturnummer + 1, el1)
    print("Bearbeitung der Reparaturauftragsnummern beendet ")   