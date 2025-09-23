from typing import override


class MolekylFormel:
    def __init__(self, mol) -> None:
        self.mol: MolekylMol = mol

    def print(self):
        print(self.mol)

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
        return f"\n<mol>: <{self.group}> {f" & <{self.mol}>" if self.mol else None}\n" 

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

    @override
    def __str__(self) -> str:
        if self.atom is not None and self.nummer is None:
            return f"""
<group> ::= <{self.atom}> 
        """
        if self.atom is not None:
            return f"""
<group> ::= <{self.atom}><{self.nummer}> & (<mol>)<num>
        """
        return f"""
<group> ::=  (<{self.mol}>)<{self.nummer}>
        """

class MolekylNummer(MolekylDel):
    def __init__(self, nummer: str) -> None:
        self.nummer: str = nummer
        super().__init__()

    @override
    def __str__(self) -> str:
        return f"<num> :== {self.nummer}"


class MolekylAtom(MolekylDel):
    def __init__(self, atom: str) -> None:
        self.atom: str = atom
        super().__init__()

    @override
    def __str__(self) -> str:
        if len(self.atom) > 1:
            return f"<atom> :== <{self.atom[0]}{self.atom[1]}>"
        return f"<num> :== <{self.atom[0]}>"


