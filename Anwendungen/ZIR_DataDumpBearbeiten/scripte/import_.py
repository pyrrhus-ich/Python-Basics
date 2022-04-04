from scripte.variablen import ws, val, indDateOfCreation, indRepairNumber, dstFile, wbDst, wsDst
from scripte.print import variablenPrint
from scripte.excelLesenUndInVariableSpeichern import fillList, changeHeadLine, changecolumNames
from scripte.repNrKuerzen import repNrKuerzen
from scripte.excelDestFileSchreiben import createDstFile
from scripte.datumUmwandeln import createDateUmwandeln
from openpyxl.styles import PatternFill, Font
from colorama import init, Fore, Style # Colorama für farbige Terminalausgaben
init(autoreset=True) # setzt colorama nach beenden des Programms wieder zurück

"""
Dieses Skript enthält nur die Importe, damit das run.py nicht so voll ist
"""