- importieren mit 'import modulnamen'
- import untereinander am Anfang des Scriptes
	import module1
	import Modul2
	from super_module import super_function
		in diesem Fall würde es heißen print(super_fuction(x) (ohne Modul)
#Python sucht in folgender Reihenfolge nach Modulen
- im aktuellen Verzeichniss
- built in module
wenn es dann nichts findet wird ein Fehler geworfen
# Dokumentation Python built in modules
https://docs.python.org/3/py-modindex.html

Beispiele für Module
- argparse
- collections | -deque(Stapel)mei
- copy | Modul zum kopieren von listen beachte deepcopy()
- math
- os - auf Betriebssystem zugreifen | Pfade erstellen
- random
- re - Regular expressions
- requests muss installiert werden | http requests in Python
- string - z.B. ascii_lowercase oder ascii_uppercase für das ganze Alphabet
- sys - zugriff auf Argumente
- lxml - schneller als built in etree. Zugriff auf XML Files


