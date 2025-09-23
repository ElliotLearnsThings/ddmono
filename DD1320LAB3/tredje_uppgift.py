from bintreeFile import Bintree

tree3 = Bintree() #Skapa trädet för trebokstavsord (tree3)
with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if ordet not in tree3:
            tree3.put(ordet)

engelska = Bintree()#Skapa trädet för engelska ord
with open("engelska.txt", "r", encoding="utf-8") as engfil:
    for rad in engfil:
        for ordet in rad.split():          # dela upp raden i ord
            ordet = ordet.lower().strip() 
            if ordet not in engelska:    # undvik dubletter i engelska
                engelska.put(ordet)
                if ordet in tree3:   # kolla om det finns i tree3
                    print(ordet, end=" ")

print("\n")


# Svar: tag hit sex fat god mat bad far sin son