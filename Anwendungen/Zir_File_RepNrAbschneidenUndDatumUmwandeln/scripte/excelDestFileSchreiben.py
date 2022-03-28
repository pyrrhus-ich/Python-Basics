def createDstFile(baseList, dstFileName, workBook, worksheet): #resulList, dstFile
    print("\nBeginne jetzt mit dem schreiben des dst Files createDstFile()")
    for row in baseList: #Hängt jeden Eintrag in der resultList an das neu erzeugt sheet
        worksheet.append(row)
    worksheet.auto_filter.ref = worksheet.dimensions          #Setzt den Autofilter über alle Spalten
    workBook.save(dstFileName) #Speichert das File
    workBook.close()
    print("Das schreiben des Ausgabefiles ist abgeschlossen. Fürs Erste sind wir fertig")   