from scripte.variablen import ws, val, indDateOfCreation, indRepairNumber, dstFile, wbDst, wsDst
from scripte.print import variablenPrint
from scripte.excelLesenUndInVariableSpeichern import fillList
from scripte.repNrUndDatumUmwandeln import repNrKuerzen, dateOfCreationUmwandelnDeutsch
from scripte.excelDestFileSchreiben import createDstFile


variablenPrint()
fillList(ws, val, indDateOfCreation)
dateOfCreationUmwandelnDeutsch(val, indDateOfCreation)
repNrKuerzen(val, indRepairNumber)
createDstFile(val, dstFile, wbDst, wsDst)





