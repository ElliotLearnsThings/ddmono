import csv
from typing import override
from hash_table import HashTable


class KDrama:

    def __init__(self, *args) -> None:
        self.dramaname = args[0] 
        self.rating_outof10 = args[1] 
        self.actors = args[2]
        self.viewshiprate = args[3] 
        self.genre = args[4]
        self.director = args[5]
        self.writer = args[6]
        self.year = args[7]
        self.noofepisodes = args[8] 
        self.network = args[9]

    @override
    def __str__(self):
        return f"KDrama name: {self.dramaname}"

def main():

    my_table = HashTable(10000)
    objs = []

    with open("kdrama.csv") as f:
        first = True
        for line in csv.reader(f):
            if first == True:
                first = False
                continue
            objs.append(obj:=KDrama(*line))
            my_table.store(obj.dramaname, obj)

    print(my_table["Legend of the Blue Sea"])

if __name__ == "__main__":
    main()

