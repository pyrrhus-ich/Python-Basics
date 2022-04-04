from scripte.import_ import *

print(Fore.RED + "<<<<<<<< Zum Starten Enter >>>>>>>>>>>>>>")
input() # Damit man weiß das es los geht
variablenPrint() # schreibt die wichtigsten variablen
print(Fore.RED + "<<< Prüfe die Variablenwerte. Insbesondere die Indexe >>> Weiter mit Enter :")
input()
fillList(ws, val, indDateOfCreation) # schreibt die Liste mit den Reihen aus dem Excel in den Speicher 
changeHeadLine(val, indDateOfCreation ) # fügt 3 neue Spalten in die Kopfzeile ein
changecolumNames(val) # Ändert ein paar Spaltennamen
createDateUmwandeln(val, indDateOfCreation) # wandelt das creatinDate (Auftragsdatum) um und trennt Tag | Monat | Jahr
repNrKuerzen(val, indRepairNumber) # schneidet den Appendix von der Reparaturnummer ab
createDstFile(val, dstFile, wbDst, wsDst) # schreibt die Zieldatei
print(Fore.RED + "<<<<<<<< Zum Beenden Enter >>>>>>>>>>>>>>  ")
input() # hält das Fenster offen





