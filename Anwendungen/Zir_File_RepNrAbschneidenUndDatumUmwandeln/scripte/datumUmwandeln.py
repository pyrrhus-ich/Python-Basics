def createDateUmwandeln(listVariable, indexofCreationDay):
    print(listVariable[1])
    # Hier wird das Datum bearbeitet und aus dem Zir datum 2022-03-25 12:35:00  wird 25.03.2022.
    # Ausserdem werden noch die 3 Spalten "creationDate, creationMonth, creationYear befüllt"
    print("\nBeginne mit Umwandeln des Datums")
    for el in listVariable:
        if el != listVariable[0]: # Damit die Überschrift (erste Zeile) nicht bearbeitet wird
            tag = el[3].day
            monat = el[3].month 
            jahr=el[3].year
            # Hier werden die 3 Spalten "creationDate, creationMonth, creationYear befüllt"
            el.pop(indexofCreationDay)
            #el.insert(indexofCreationDay, str(tag)+"."+str(monat)+"."+str(jahr))
            el.insert(indexofCreationDay, str(tag)+"."+str(monat)+"."+str(jahr))
            el.insert(indexofCreationDay + 1, tag)
            el.insert(indexofCreationDay + 2, monat)
            el.insert(indexofCreationDay + 3, jahr)   
    print("Umwandlung des Datums abgeschlossen")