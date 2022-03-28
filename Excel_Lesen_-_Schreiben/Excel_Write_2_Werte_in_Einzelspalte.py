from re import A
from openpyxl import Workbook
    # was hier nicht erläutert ist, steht im ersten File
wb=Workbook()
ws=wb.active
myList=['Frank','hat','bald','Geburtstag']
# Schreiben der Werte einer Liste untereinander in eine Reihe des Excel Files
for el in myList:
    i=1
    while i <= len(myList):
        cell="A"
        ws[cell+str(i)]=myList[i-1]
        i+=1
wb.save('Bsp_Excel_Write_2.xlsx')

