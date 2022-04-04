import os
from pathlib import Path

"""
Dieses Script findet jeweils die neueste Datei in einem Verzeichnis.
Die Variablen sind selbsterklärend.
Gut zu wissen : os.path.split(neuesteDateiPfad) gibt eine Liste mit 2 Elementen aus
el[0] ist der Pfad | el[1] ist der Dateiname
"""

srcFld = os.getcwd()

def by_mtime(file):
    return file.stat().st_mtime
    
neusteDateiPfad = max((p for p in Path(srcFld).iterdir() if p.is_file()), key=by_mtime)
neuesteDateiName = os.path.split(neusteDateiPfad)[1]

print("Kompletter Pfad zur neuesten Datei : {}".format(neusteDateiPfad))
print("Der Name der neuesten Datei ist : {}".format(neuesteDateiName))