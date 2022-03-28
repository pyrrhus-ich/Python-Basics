from scripte.variablen import ws, val, indDateOfCreation, indRepairNumber, dstFile, wbDst, wsDst
from scripte.print import variablenPrint
from scripte.excelLesenUndInVariableSpeichern import fillList
from scripte.repNrUndDatumUmwandeln import repNrKuerzen, dateOfCreationUmwandeln
from scripte.excelDestFileSchreiben import createDstFile


variablenPrint()
fillList(ws, val, indDateOfCreation)
repNrKuerzen(val, indRepairNumber)
dateOfCreationUmwandeln(val, indDateOfCreation)
createDstFile(val, dstFile, wbDst, wsDst)





