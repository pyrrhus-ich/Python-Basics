class Person:
    def __init__(self, anrede, vorname, nachname, plz, ort, strasse, hausnummer):
        self.Anrede = anrede
        self.Vorname = vorname
        self.Nachname = nachname
        self.Postleitzahl = plz
        self.Ort = ort
        self.Straße = strasse
        self.Hausnummer = hausnummer
    def setNewAdress(self, plz, ort, strasse, hausnummer):
        self.Postleitzahl=plz
        self.Ort=ort
        self.Straße=strasse
        self.Hausnummer=hausnummer
    def getAll(self):
        print("{}\n{} {}\n{} {}\n{} {}".format(self.Anrede,self.Vorname,
        self.Nachname,self.Postleitzahl,self.Ort,self.Straße,self.Hausnummer))


K1 = Person("Herr", "Frank", "Menzel", 87527, "Sonthofen", "Stieglitzweg", 3)
K2=Person("Frau","" , "Schreiber",0 ,"" , "", 0,)

K1.getAll()
K1.setNewAdress(17389, "Anklam", "Tuchowstraße","3b")
K1.getAll()

K2.getAll()



    
