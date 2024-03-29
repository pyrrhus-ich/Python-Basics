from colorama import init, Fore, Style

def iter_rows(ws):
    print("\niter_rows() gestartet")
    for row in ws.iter_rows():
        yield [cell.value for cell in row]
    print("iter_rows_ beendet")

def fillList(workSheet, listVariable, indexOfCreationDay):
        #jede zeile wird einzeln eingelesen
    for el in iter_rows(workSheet):
            #und an eine bestehende listVariable angehängt
        listVariable.append(el)
    print("\nInsert in listVariable abgeschlossen")
    print(Fore.GREEN + "Es wurden {} Datensätze (ohne Kopfzeile) eingelesen".format(len(listVariable)-1))

def changeHeadLine(listVariable, indexOfCreationDay):
        #An Index[0] der listVariable liegt die Kopfzeile. Dieser werden jetzt 3 Spalten hinzugefügt
    listVariable[0].insert(indexOfCreationDay + 1,"Creation Day")
    listVariable[0].insert(indexOfCreationDay + 2,"Creation Month")
    listVariable[0].insert(indexOfCreationDay + 3,"Creation Year")
    print("Neue Spalten in listVariable eingefügt : {} | {} | {}".format(listVariable[0][4], listVariable[0][5], listVariable[0][6])) 

def changecolumNames(listVariable):
    print("\nBeginne mit der Umbenennung der Spalten")
    listVariable[0][0] = "ZIR ID"
    listVariable[0][1] = "Repair Nr."
    listVariable[0][2] = "Property"
    listVariable[0][3] = "Date of \ncreation"
    listVariable[0][10]= "Supplier \nNumber"
    print("Spalten erfolgreich umgewandelt")

