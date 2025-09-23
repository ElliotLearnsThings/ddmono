from typing import Any

from arrayQFile import ArrayQ
from linkedQFile import LinkedQ

class TrollKarlen():

    def __init__(self, type) -> None:
        if type == "ll":
            self.constructor = LinkedQ
        else:
            self.constructor = ArrayQ

    def find_forward(self, input: list[Any]):
        new_array = self.constructor()
        iterations = len(input)
        for i in range(iterations):
            x = input.pop(0)
            input.append(x)
            y = input.pop(0)
            new_array.enqueue(y)
        return new_array

    def find_reverse(self, input: list[Any]) -> ArrayQ:
        reversearray = self.constructor()
        input.reverse()
        for val in input:
            reversearray.insert(val, 0)
            x = reversearray.pop(-1)
            reversearray.insert(x, 0)
        return reversearray


def get_user_input():
    try:
        return [int(x) for x in input("Insert your numbers: ").split(" ")]
    except ValueError:
        print("Invalid input, try again")
        return get_user_input()

def run_troll_karlen(type: str = ""):

    user_input = get_user_input()
    print("Got user input: ", user_input)

    tk = TrollKarlen(type)

    if type == "ll":
        print(" ---------- Trial, LinkedQ ---------- ")
    else:
        print(" ---------- Trial, ArrayQ ---------- ")
    reversed_array = tk.find_reverse(user_input)
    print("Array reversed: ", reversed_array.get_all())


    original_array = tk.find_forward(reversed_array.get_all())
    print("Array original: ", original_array.get_all())

def main():
    run_troll_karlen("ll")
    run_troll_karlen()

if __name__ == "__main__":
    main()
