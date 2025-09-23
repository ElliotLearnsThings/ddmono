class MolekylFormel:
    def __init__(self) -> None:
        self.groups: 'list[MolekylDel]' = []

    def add_mol(self, mol: 'MolekylMol'):
        self.groups.append(mol)

class MolekylDel:
    def __init__(self) -> None:
        pass

class MolekylMol(MolekylDel):
    def __init__(self, group: 'MolekylGrupp', mol: 'MolekylMol | None' = None) -> None:
        super().__init__()
        self.group: 'MolekylGrupp' = group
        self.mol: 'MolekylMol | None' = mol

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

class MolekylNummer(MolekylDel):
    def __init__(self, nummer: int) -> None:
        self.nummer: int = nummer
        super().__init__()


class MolekylAtom(MolekylDel):
    def __init__(self, atom: str) -> None:
        self.atom: str = atom
        super().__init__()


