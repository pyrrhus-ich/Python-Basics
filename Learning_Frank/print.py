print(type("hello")) gibt den Datentyp aus

# https://docs.python.org/3.6/library/string.html#format-specification-mini-language
# https://www.w3schools.com/python/ref_func_format.asp
#format() Methode
	es werden geschweifte klammern als Platzhalter eingefügt. Der Inhalt dieser Platzhalter wird in der Reihenfolge des
	Auftretens in format angegeben. Mann kann den Platzhaltern auch nummern geben. Diese Nummern beziehen sich dann auf den
	Index in .format(). Man kann auch Keywords benutzen. So lange man entweder Nummern ODER keywords benutzt kann man dieser
	Reihenfolge des Auftretens durch Eintragen in den Platzhaltern festlegen. Wenn man beides mischt, gilt: in der format methode
	kommt zuerst das Argument für die Zahl (positional argument) und dann das Argument für das keyword (keyword Argument)
  #Beispiel:
  print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
	Mix 2 eggs, 30 g of milk and a pinch of salt to make an ideal omelet.
  #Beispiel mit Index:
  print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
	Strangers in the Night by Frank Sinatra
  print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))
    Night in the Strangers by Frank Sinatra
  #Beispiel mit Keywords
   print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',adjective='incredible',theatre='BFI IMAX'))
	 The Lord of the Rings at BFI IMAX was incredible!
  #Beispiel für gemischt 
   print('The {0} was {adjective}!'.format('Lord of the Rings', adjective='incredible'))
	 The Lord of the Rings was incredible!
  #Beispiel für fehlerhafte Anordnumg der Argumente (SyntaxError)
   print('The {0} was {adjective}!'.format(adjective='incredible', 'Lord of the Rings'))
	 SyntaxError: positional argument follows keyword argument