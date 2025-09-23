import unittest
from molekyl import kollaMolekyl

def load_testdata(mol_file, exp_file):
    with open(mol_file, encoding="utf-8") as f_mol, open(exp_file, encoding="utf-8") as f_exp:
        mols = [line.strip() for line in f_mol if line.strip() and line.strip() != "#"]
        exps = [line.strip() for line in f_exp if line.strip()]
    if len(mols) != len(exps):
        raise ValueError(f"Antal rader matchar inte: {len(mols)} molekyler vs {len(exps)} expected")
    return mols, exps

class TestMolekylFromFiles(unittest.TestCase):
    def test_file_based(self):
        mols, exps = load_testdata("molekyler.txt", "expected.txt")
        for i in range(len(mols)):
            with self.subTest(line=i+1, molekyl=mols[i]):
                self.assertEqual(kollaMolekyl(mols[i]), exps[i])

if __name__ == "__main__":
    unittest.main()
