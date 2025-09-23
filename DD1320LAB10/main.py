from molekylobjekt.molekylnummer import Molekylnummer
from molekylobjekt.molekylstruktur import MolekylStruktur
from molgrafik import Molgrafik


def main():
    mg = Molgrafik()
    mol = input()
    test = MolekylStruktur()
    test2 = Molekylnummer()

class GraphNode:
    def __init__(self):
        self.prev = None

    def add_prev(self, node):
        self.prev = node
    

        



if __name__ == "__main__":
    main()
