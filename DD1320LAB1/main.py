import csv
import math
from random import random
import traceback
from typing import Any, TypeVar, override
from datetime import datetime

COLUMN_NAMES = [
    "Drama Name",             #Drama Name,             
    "Rating(Out of 10)",      #Rating(Out of 10)       
    "Actors",                 #Actors,                 
    "Viewship Rate",          #Viewship Rate,          
    "Genre",                  #Genre,                  
    "Director",               #Director,               
    "Writer",                 #Writer,                 
    "Year",                   #Year,                   
    "No of Episodes",         #No of Episodes,         
    "Network"                 #Network                 
]                                        

class DramaObject:
    def __init__(
            self,
            # Assume ordered list
            *args
            ) -> None:

        self.is_valid = True
        self.drama_name: str = ""
        self.rating: float = 0.0
        self.actors: str = ""
        self.viewship_rate: float = 0.0
        self.genre: str = ""
        self.director: str = ""
        self.writer: str = ""
        self.year: int = 1990
        self.no_of_episodes: int = 0
        self.network: str = ""

        try: 
            self.drama_name: str = args[0]
            self.rating: float = float(args[1])
            self.actors: str = args[2]
            self.viewship_rate: float = float(args[3])
            self.genre: str = args[4]
            self.director: str = args[5]
            self.writer: str = args[6]
            self.year: int = int(args[7])
            self.no_of_episodes: int = int(args[8])
            self.network: str = args[9]
        except ValueError:
            self.is_valid = False
            print("Failed to generate object due to bad input string")
        except IndexError:
            self.is_valid = False
            print("Failed to generate object due to not enough params")
        except Exception:
            self.is_valid = False
            print(f"Failed to generate object due to unhandled error {traceback.format_exc()}")

    def health_check(self):
        """ Health check - Throws AssertionError if object is invalid
        """
        assert self.is_valid
        # Assert type conversions successful
        assert isinstance(self.drama_name, str)
        assert isinstance(self.year, int)
        assert isinstance(self.rating, float)

    def __lt__(self, other: 'DramaObject'):
        return self.viewship_rate < other.viewship_rate

    @override
    def __str__(self):
        return f"Drama name: {self.drama_name}, rating: {self.rating}, genre: {self.genre}, year: {self.year}"

    def compare_year(self, other: 'DramaObject'):
        return self.year < other.year

    def max_year(self, other: 'DramaObject'):
        return max(self.year, other.year)

T = TypeVar("T")

def get_random_item(input_list: list[T]) -> T: 
    index = math.floor(random() * len(input_list))
    item = input_list.pop(index)
    return item

def get_objects(number_of_objects: int | None) -> list[DramaObject] | None:
    lines = []

    with open("data.csv", mode="r") as f:
        data = csv.reader(f)
        for line in data:
            lines.append(line)

    col_names = lines[0]
    lines = lines[1:]
    print(col_names)
    assert(all([name in COLUMN_NAMES for name in col_names]))

    # Given number of lines
    number_lines = number_of_objects
    print(number_lines)
    if number_lines:
        newLines = [get_random_item(lines) for _ in range(number_lines)] # note not to iterate over mutable object
    else:
        newLines = lines

    attributesAll = [line for line in newLines]
    objects = [DramaObject(*attributes) for attributes in attributesAll]

    # Assert correct formation
    try:
        [drama_object.health_check() for drama_object in objects]
    except AssertionError as e:
        print("Some objects failed health check, retrying")
        return None

    return objects

def main():
    drama_objects = get_objects(2)
    if drama_objects is None:
        print("Found no objects")
        return
    print(drama_objects[0])
    print(drama_objects[1])
    print(drama_objects[1] > drama_objects[0])

    # Find which has the greater year (least old)
    if drama_objects[0].compare_year(drama_objects[1]):
        print(f"{drama_objects[0].drama_name} is older than {drama_objects[1].drama_name}")  
    else: 
        print(f"{drama_objects[1].drama_name} is older than {drama_objects[0].drama_name}")

    all_drama_objects = get_objects(None)
    if all_drama_objects is None:
        print("Found no objects")
        return

    search = input("Search for a drama's name: ")
    print("Search results:\n")
    for object in all_drama_objects:
        if search.strip().lower().replace(" ", "") in object.drama_name.strip().lower().replace(" ", ""):
            print(object)


if __name__ == "__main__":
    main()
