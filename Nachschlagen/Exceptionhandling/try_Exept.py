

x = 5
y = b

def durch(a,b):
    try:
        z = a / b
    except Exception:
        print("Ein Fehler ist aufgetreten")
    else:
        print(z)
    finally:
        print("Division ist durch")


durch(x,y)