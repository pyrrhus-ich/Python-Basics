class Person:
    def __init__(self, anrede, vorname, nachname, plz, ort, strasse, hausnummer):
        self.Anrede = anrede
        self.Vorname = vorname
        self.Nachname = nachname
        self.Postleitzahl = plz
        self.Ort = ort
        self.Straße = strasse
        self.Hausnummer = hausnummer
    def zeige(self):
        print("{}\n{} {}\n{} {}\n{} {}".format(self.Anrede,self.Vorname,
        self.Nachname,self.Postleitzahl,self.Ort,self.Straße,self.Hausnummer))

K1 = Person("Herr", "Frank", "Menzel", 87527, "Sonthofen", "Stieglitzweg", 3)


K1.zeige()





    
