from linkedQ import LinkedQ
from molekylObjekt import MolekylAtom, MolekylFormel, MolekylGrupp, MolekylMol, MolekylNummer
from molgrafik import Molgrafik, Ruta

ATOMER_STR = """H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr
Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd
In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf
Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm
Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv"""
GILTIGA_ATOMER = set(ATOMER_STR.split())

class molekylFel(Exception):
    pass

def readformel(q) -> MolekylFormel:
    # <formel> ::= <mol>

    mol = readmol(q, inside_paren=False)
    stuktur = MolekylFormel(mol)
    return stuktur

def readmol(q: LinkedQ, inside_paren) -> MolekylMol:
    # <mol> ::= <group> | <group><mol>

    group = readgroup(q)
    mol = None

    while True:
        nxt = q.peek()
        if nxt is None:
            break
        if nxt == ')':
            if inside_paren:
                break
            raise molekylFel("Felaktig gruppstart vid radslutet")
        if nxt == '(' or ('A' <= nxt <= 'Z'):
            mol = readmol(q, inside_paren=True)
            continue
        if 'a' <= nxt <= 'z':
            raise molekylFel("Saknad stor bokstav vid radslutet")
        if nxt.isdigit():
            raise molekylFel("Felaktig gruppstart vid radslutet")
        raise molekylFel("Felaktig gruppstart vid radslutet")

    if mol is not None:
        mol = MolekylMol(group, mol)
    else:
        mol = MolekylMol(group)
    return mol

def readgroup(q) -> MolekylGrupp:
    # <group> ::= <atom> | <atom><num> | (<mol>)<num>

    atom = None
    nummer = None
    mol = None

    nxt = q.peek()
    if nxt is None:
        raise molekylFel("Felaktig gruppstart vid radslutet")
    if nxt == ')':
        raise molekylFel("Felaktig gruppstart vid radslutet")
    if nxt.isdigit():
        raise molekylFel("Felaktig gruppstart vid radslutet")

    if nxt == '(':
        q.dequeue()  # '('
        mol = readmol(q, inside_paren=True)
        if q.peek() != ')':
            raise molekylFel("Saknad högerparentes vid radslutet")
        q.dequeue()  # ')'
        if q.peek() is None or not q.peek().isdigit():
            raise molekylFel("Saknad siffra vid radslutet")
        nummer = readNummer(q)
        return MolekylGrupp(None, nummer, mol)
        

    atom = readatom(q)
    if q.peek() is not None and q.peek().isdigit():
        nummer = readNummer(q)

    if nummer is None:
        return MolekylGrupp(atom, None, None)
    else:
        return MolekylGrupp(atom, nummer, None)


# Atom-funktioner
def readatom(q) -> MolekylAtom:
    # <atom> ::= <LETTER> | <LETTER><letter>

    ch = q.peek()
    if ch is None or not ch.isalpha() or not ch.isupper():
        raise molekylFel("Saknad stor bokstav vid radslutet")

    symbol = readStorBokstav(q)
    nxt = q.peek()
    if nxt is not None and nxt.isalpha() and nxt.islower():
        symbol += readLitenBokstav(q)

    if symbol not in GILTIGA_ATOMER:
        raise molekylFel("Okänd atom vid radslutet")

    return MolekylAtom(symbol)

def readStorBokstav(q):
    ch = q.peek()
    if ch is None or not ch.isupper():
        raise molekylFel("Saknad stor bokstav vid radslutet")
    return q.dequeue()

def readLitenBokstav(q):
    ch = q.peek()
    if ch is None or not ch.islower():
        raise molekylFel("Felaktig liten bokstav vid radslutet")
    return q.dequeue()

# Nummer-funktion
def readNummer(q) -> MolekylNummer:
    d = q.dequeue()
    if d == "0":
        raise molekylFel("För litet tal vid radslutet")
    if d == "1":
        nxt = q.peek()
        if nxt is None or not nxt.isdigit():
            raise molekylFel("För litet tal vid radslutet")

    checked = False
    while True:
        nxt = q.peek()
        if d == "1" and nxt is None and not checked:
            raise molekylFel("För litet tal vid radslutet")
        if not checked:
            checked = True
        if nxt is not None and nxt.isdigit():
            d += q.dequeue()
            continue
        break
    return MolekylNummer(d)

def storeMolekyl(molekyl):
    q = LinkedQ()
    for ch in molekyl:
        q.enqueue(ch)

    return q

def skapaMolekylTrad(molekyl) -> MolekylFormel:
    q = storeMolekyl(molekyl)
    try:
        struktur = readformel(q)
        return struktur
        #struktur.print()
    except molekylFel as fel:
        rest_chars = []
        while True:
            nxt = q.peek()
            if nxt is None:
                break
            rest_chars.append(q.dequeue())
        rest = "".join(rest_chars)
        return f"{fel} {rest}" if rest else f"{fel}"

def kollaMolekyl(molekyl):
    q = storeMolekyl(molekyl)
    try:
        readformel(q)
        return "Formeln är syntaktiskt korrekt"
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
    mg = Molgrafik()

    s = input()
    tr: MolekylFormel = skapaMolekylTrad(s)
    print(tr.vikt)
    #mg.show(tr.ruta)

if __name__ == "__main__":
    main()




"""
<formel>::= <mol> \n
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
"""
