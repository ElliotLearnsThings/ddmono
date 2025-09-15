from typing import Generic, TypeVar

T = TypeVar("T")
K = TypeVar("K")

class HashDict(Generic[T, K]):
    def __init__(self) -> None:
        super().__init__()
        self.dict: dict[T, K] = {}

    def store(self, key: T, value: K):
        self.dict[key] = value

    def search(self, key: T) -> K | None:
        try:
            return self.dict[key]
        except KeyError:
            return None

    def __getitem__(self, key: T):
        return self.search(key)

    def __contains__(self, key: T):
        return key in self.dict.keys()

def test_hash_dict():
    my_dict: HashDict[str, str] = HashDict()
    my_dict.store("hello", "world")
    my_dict.store("how", "are you?")
    my_val = my_dict.search("hello")

    assert my_val == "world"
    my_val = my_dict.search("No val")
    assert my_val is None

    print("Not ok" if my_val is None else "Could not find None... Good!")

    print("Finding 'Hello'")
    my_val = my_dict["hello"]
    assert my_val == "world"
    print(my_val)

    if "how" in my_dict:
        print("Found")
    assert "how" in my_dict

if __name__ == "__main__":
    test_hash_dict()

