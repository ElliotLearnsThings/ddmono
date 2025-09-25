from typing import override
from molgrafik import Ruta
from vikter import WEIGHTS

class MolekylFormel:
    def __init__(self, mol) -> None:
        self.mol: MolekylMol = mol

    def print(self):
        print(self.mol)

    @property
    def ruta(self) -> Ruta:
        ruta = self.mol.ruta
        return ruta

    @property
    def vikt(self) -> float:
        return self.mol.vikt()


class MolekylDel:
    def __init__(self) -> None:
        pass

class MolekylMol(MolekylDel):
    def __init__(self, group: 'MolekylGrupp', mol: 'MolekylMol | None' = None) -> None:
        super().__init__()
        self.group: 'MolekylGrupp' = group
        self.mol: 'MolekylMol | None' = mol

    @override
    def __str__(self) -> str:
        return f"\n<mol>: <{self.group}> {f" & <{self.mol}>" if self.mol else ""}\n" 
    
    @property
    def ruta(self) -> Ruta:
        ruta = self.group.ruta
        if self.mol is not None:
            ruta.next = self.mol.ruta
        return ruta

    def vikt(self) -> float:
        sum = 0
        sum += self.group.vikt()
        if self.mol is not None:
            sum += self.mol.vikt()
        return sum

class MolekylGrupp(MolekylDel):
    def __init__(
            self,
            atom: 'MolekylAtom | None' = None,
            nummer: 'MolekylNummer | None' = None,
            mol: 'MolekylMol | None' = None
            ) -> None:
        super().__init__()
        self.atom: 'MolekylAtom | None' = atom
        self.nummer: 'MolekylNummer | None' = nummer
        self.mol: 'MolekylMol | None' = mol

    @property
    def ruta(self) -> Ruta:
        ruta = Ruta()
        if self.mol is not None:
            ruta.num = int(self.nummer.nummer)
            ruta.down = self.mol.ruta
            return ruta
        if self.atom is not None and self.nummer is not None:
            ruta.atom = self.atom.atom
            ruta.num = int(self.nummer.nummer)
            return ruta

        ruta.atom = self.atom.atom
        return ruta

    @override
    def __str__(self) -> str:
        if self.atom is not None and self.nummer is None:
            return f"""
<group> ::= <{self.atom}> 
        """
        if self.atom is not None:
            return f"""
<group> ::= <{self.atom}><{self.nummer}>
        """
        return f"""
<group> ::=  (<{self.mol}>)<{self.nummer}>
        """

    def vikt(self) -> float:
        sum = 0
        if self.atom and self.nummer:
            sum += self.atom.vikt * int(self.nummer.nummer)
            return sum

        if self.atom:
            sum += self.atom.vikt
            return sum

        if self.mol is not None:
            sum += self.mol.vikt() * int(self.nummer.nummer)
            return sum

        return sum

class MolekylNummer(MolekylDel):
    def __init__(self, nummer: str) -> None:
        self.nummer: str = nummer
        super().__init__()

    @property
    def val(self):
        return int(self.nummer)

    @override
    def __str__(self) -> str:
        return f"<num> :== {self.nummer}"

class MolekylAtom(MolekylDel):
    def __init__(self, atom: str) -> None:
        self.atom: str = atom
        super().__init__()

    @property
    def vikt(self):
        return float(WEIGHTS.search(self.atom).getvikt())

    @override
    def __str__(self) -> str:
        if len(self.atom) > 1:
            return f"<atom> :== <{self.atom[0]}{self.atom[1]}>"
        return f"<num> :== <{self.atom[0]}>"



