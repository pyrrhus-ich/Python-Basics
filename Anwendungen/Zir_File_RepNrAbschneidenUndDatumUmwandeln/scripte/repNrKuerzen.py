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

    