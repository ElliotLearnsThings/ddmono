from linkedQ import LinkedQ

smaBokstaver =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
storaBokstaver = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class molekylFel(Exception):
    pass

def readMolekyl(q):
    readAtom(q)
    nxt = q.peek()
    if nxt is not None and nxt.isdigit():
        readNummer(q)

def readAtom(q):
    readStorBokstav(q)
    nxt = q.peek()
    if nxt is not None and nxt.islower():
        readLitenBokstav(q)

def readStorBokstav(q):
    ch = q.peek()
    if ch not in storaBokstaver:
        raise molekylFel("Saknad stor bokstav vid radslutet")
    q.dequeue()

def readLitenBokstav(q):
    ch = q.peek()
    if ch not in smaBokstaver:
        raise molekylFel("Felaktig liten bokstav vid radslutet")
    q.dequeue()

def readNummer(q):
    # Läs första siffran
    d = q.dequeue()
    if d in ("0", "1"):
        raise molekylFel("För litet tal vid radslutet")
    # Om första siffran är 2–9 → läs resten (valfritt antal siffror)
    while True:
        nxt = q.peek()
        if nxt is None or not nxt.isdigit():
            break
        q.dequeue()

def storeMolekyl(molekyl):
    q = LinkedQ()
    for ch in molekyl:
        q.enqueue(ch)
    return q

def kollaMolekyl(molekyl):
    q = storeMolekyl(molekyl)
    try:
        readMolekyl(q)
        return "Formeln är syntaktiskt korrekt"   # OBS stavning: syntaktiskt
    except molekylFel as fel:
        rest_chars = []
        while True:
            nxt = q.peek()
            if nxt is None:
                break
            rest_chars.append(q.dequeue())
        rest = "".join(rest_chars)
        return f"{fel} {rest}" if rest else f"{fel}"

def main():
    while True:
        s = input()
        if s == "#":
            break
        print(kollaMolekyl(s))



        

if __name__ == "__main__":
    main()
"""
<molekyl> ::= <atom> | <atom><num>  
<atom>  ::= <character> | <character><character>  
<character>::= A | B | C | ... | Z
<character>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
"""