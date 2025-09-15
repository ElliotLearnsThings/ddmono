def utskrift(lista):
    if len(lista) > 0:
        print(lista[0])
        utskrift(lista[1:])

def utskrift2(lista):
    if len(lista) > 0:
        utskrift2(lista[1:])
        print(lista[0])

utskrift([1, 2, 3, 4, 5])
utskrift2([1, 2, 3, 4, 5])
