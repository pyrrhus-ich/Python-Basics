# map iteriert über eine Liste und ersetzt so die for schleife
myl = [2,4,6]
def f(el):
    return el**2
 # die folgenden 3 Zeilen machen das selbe wie...  
y=[]
for el in myl:
    y.append(f(el))
print(y)
print(y[2])
#...die folgende Zeile.
#beide brauchen aber noch die funktion "f"
x=list(map(f,myl))
print(x)
print(x[2])
#die folgende Zeile arbeitet mit map und einer anonymen(lambda) Funktion
y=list(map(lambda el: el** 2, myl))
print(y)
print(y[2])

