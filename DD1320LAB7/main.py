import math
from hash_table import HashTable
from random import random

def main():
    random_word = lambda: str(math.floor(random() * 1000000))
    length = 100
    my_table: HashTable[str] = HashTable(20000)
    keys = set()
    for i in range(length):
        word = random_word()
        rand_val = random_word()
        if word not in keys:
            my_table.store(word, rand_val)
        keys.add(word)

    i = 0
    j = 0

    for key in keys:
        try:
            my_table[key]
            j += 1
        except KeyError:
            i += 1
            print("did not find", key)
    print(j)


if __name__ == "__main__":
    main()
