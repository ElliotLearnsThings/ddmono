from typing import override
from bintreeFile import Bintree
from chars import CHARS
from linkedQ import LinkedQSimple

def get_user_input(prompt: str) -> str:
    if len((user_input := input("Insert your word: ").strip()).split(" ")) == 1 and all([x in CHARS for x in user_input]):
        return user_input  
    print("Whitespace found or invalid char, not allowed, try again")
    return get_user_input(prompt)

def get_words() -> set[str]:
    myset: set[str] = set()
    with open("word3.txt", mode="r") as f:
        _ = [myset.add(line.strip()) for line in f.readlines()]
    return myset

def get_words_tree() -> Bintree[str]:
    mytree: Bintree[str] = Bintree()
    with open("word3.txt", mode="r") as f:
        _ = [mytree.put(line.strip()) for line in f.readlines()]
    return mytree


class PathFinder:
    def __init__(self, first_word: str, second_word: str) -> None:
        self.first_word: str = first_word
        self.second_word: str = second_word
        self.chars: list[str] = CHARS

    def find_path(self) -> None | int:
        ...

class PathFinderBinTree(PathFinder):
    def __init__(self, word_tree: Bintree[str], first_word: str, second_word: str) -> None:
        super().__init__(first_word, second_word)
        self.word_queue: Bintree[str] = word_tree
        self.buffer: LinkedQSimple[str] = LinkedQSimple()
        self.found_words: Bintree[str] = Bintree()

    @staticmethod
    def __create_new_word(new_char: str, index: int, initial_word: str):
        assert(len(new_char) == 1)
        return initial_word[:index] + new_char + initial_word[index + 1:]

    def __contains__(self, key: str) -> bool:
        return key in self.word_queue

    def __make_children(self, initial_word: str, index: int) -> bool:
        current_char = initial_word[index]
        
        for c in self.chars:
            if current_char == c:
                continue

            # Generate a new word at the index
            generated_word = self.__create_new_word(c, index, initial_word)
            if generated_word == self.second_word:
                return True

            # If the generated word is in the word store, append it to the stack
            self.buffer.enqueue(generated_word) if generated_word in self else None
        return False


    @override
    def find_path(self, max_iter: int = 20) -> int | None:
        current_words: LinkedQSimple[str] = LinkedQSimple()
        current_words.enqueue(self.first_word)

        found = False
        i = 0

        while not found and i < 20:
            i += 1
            # For every char
            for _ in range(len(current_words)):
                word = current_words.dequeue()
                if word is None:
                    return None

                if word in self.found_words:
                    continue

                self.found_words.put(word)
                for k in range(len(word)):
                    # get all possible words that exist with each char
                    if self.__make_children(word, k):
                        return i

            current_words = self.buffer

        print("Reached max_iter")
        return None

class PathFinderLinkedQ(PathFinder):
    def __init__(self, word_queue: set[str], first_word: str, second_word: str) -> None:
        super().__init__(first_word, second_word)
        self.word_queue: set[str] = word_queue
        self.buffer: LinkedQSimple[str] = LinkedQSimple()
        self.found_words: Bintree[str] = Bintree()

    @staticmethod
    def __create_new_word(new_char: str, index: int, initial_word: str):
        assert(len(new_char) == 1)
        return initial_word[:index] + new_char + initial_word[index + 1:]

    def __contains__(self, key: str) -> bool:
        return key in self.word_queue

    def __make_children(self, initial_word: str, index: int) -> bool:
        current_char = initial_word[index]
        
        for c in self.chars:
            if current_char == c:
                continue

            # Generate a new word at the index
            generated_word = self.__create_new_word(c, index, initial_word)
            if generated_word == self.second_word:
                return True

            # If the generated word is in the word store, append it to the stack
            self.buffer.enqueue(generated_word) if generated_word in self else None
        return False


    @override
    def find_path(self, max_iter: int = 20) -> int | None:
        current_words: LinkedQSimple[str] = LinkedQSimple()
        current_words.enqueue(self.first_word)

        found = False
        i = 0

        while not found and i < 20:
            i += 1
            # For every char
            for _ in range(len(current_words)):
                word = current_words.dequeue()
                if word is None:
                    return None

                if word in self.found_words:
                    continue
                self.found_words.put(word)

                for k in range(len(word)):
                    # get all possible words that exist with each char
                    if self.__make_children(word, k):
                        return i

            current_words = self.buffer

        print("Reached max iterations")
        return None


def main():
    # Second version, missing binary tree

    first_word = get_user_input("Enter your first word")
    second_word = get_user_input("Enter your first word")

    exists_path = PathFinderLinkedQ(get_words(), first_word, second_word).find_path()
    if exists_path:
        print("path exists at step", exists_path)
    else:
        print("path not found")
    exists_path = PathFinderBinTree(get_words_tree(), first_word, second_word).find_path()
    if exists_path:
        print("path exists at step", exists_path)
    else:
        print("path not found")


if __name__ == "__main__":
    main()

