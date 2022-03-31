

# wenn das Datum in Englisch vorliegt
def dateOfCreationUmwandelnEnglisch(listVariable, indexofCreationDay):
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
            print(z)
            x=z[0].split("-")
            x.reverse()
            tag = x[0]
            monat = x[1]
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

# wenn das Datum in Deutsch vorliegt
def dateOfCreationUmwandelnDeutsch(listVariable, indexofCreationDay):
    # Hier wird das Datum bearbeitet und aus dem Zir datum 2022-03-25 12:35:00  wird 25.03.2022.
    # Ausserdem werden noch die 3 Spalten "creationDate, creationMonth, creationYear befüllt"
    print("\nBeginne mit Umwandeln des Datums")
    y=""
    jahr = ""
    monat =""
    tag = ""
    for el in listVariable:
        if el != listVariable[0]: # Damit die Überschrift (erste Zeile) nicht bearbeitet wird
            z = str(el[indexofCreationDay])
            slice_object = slice(10,)
            z=z[slice_object]
            #print("Zeile 48 z = {}".format(z))
            z = z.split("-")
            #print("Zeile 50 z = {}".format(z))
            x = z.reverse()
            #print("Zeile 52 x = {}".format(x))
            tag = z[0]
            monat = z[1]
            jahr=z[2]
            #print("Zeile 55 Tag {} Monat {} Jahr {}".format(tag,monat,jahr))
            z.insert(1,".")
            z.insert(3,".")
            #print("Zeile 58 z = {}".format(z))
            # Hier werden die 3 Spalten "creationDate, creationMonth, creationYear befüllt"
            for i in z:
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
    #listVariable[0].insert(indexDerReparaturnummer + 1,"cut Repairnumber for query")
    for el in listVariable:
        if el != listVariable[0]:
        #Hier bearbeiten wir die Auftragsnummer und schneiden die letzten 2 "-R" oder mehr ab
            i = (el[indexDerReparaturnummer])
            slice_RepairNumber = slice(0,10) # schneidet die Nummer auf M199-12345
            el0 = i[slice_RepairNumber]
            #slice_queryNumber = slice(5,10) # schneidet die Nummer so, das man in BO danach suchen kann
            #el1 = i[slice_queryNumber]+";"
            el.pop(indexDerReparaturnummer)
            el.insert(indexDerReparaturnummer,el0)
            #el.insert(indexDerReparaturnummer + 1, el1)
    print("Bearbeitung der Reparaturauftragsnummern beendet ")   