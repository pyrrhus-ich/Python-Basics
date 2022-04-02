from scripte.variablen import ws, val, indDateOfCreation, indRepairNumber, dstFile, wbDst, wsDst
from scripte.print import variablenPrint
from scripte.excelLesenUndInVariableSpeichern import fillList, changeHeadLine
from scripte.repNrKuerzen import repNrKuerzen
from scripte.excelDestFileSchreiben import createDstFile
from scripte.datumUmwandeln import createDateUmwandeln


variablenPrint()
fillList(ws, val, indDateOfCreation)
changeHeadLine(val, indDateOfCreation )
createDateUmwandeln(val, indDateOfCreation)
repNrKuerzen(val, indRepairNumber)
createDstFile(val, dstFile, wbDst, wsDst)





