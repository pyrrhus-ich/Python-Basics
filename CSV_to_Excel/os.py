import os
import variablen 
import os   
import shutil

wDir = os.getcwd()


def csvName():
    rCsvName = os.listdir(variablen.csvDir)[0]
    print("rCsvName = " + rCsvName)
    csvName = ""
    for el in rCsvName:  
        if el != "(":
            if el != ")":
                if el != " ":
                    csvName = csvName + el
    variablen.csvName = csvName
    print(csvName)
    print(variablen.csvName)

csvName()





