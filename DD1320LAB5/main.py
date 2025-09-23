from typing import override
from chars import CHARS
from graph import ParentNode
from linkedQ import LinkedQSimple
from solution_exception import SolutionFound

def get_user_input(prompt: str) -> str:
    try:
        if len((user_input := input("Insert your word: ").strip()).split(" ")) == 1 and all([x in CHARS for x in user_input]) and len(user_input) == 3 and user_input in get_words_set():
            return user_input  
        raise ValueError
    except ValueError:
        print("Either - whitespace found, invalid char, not allowed try again")
        return get_user_input(prompt)

def get_words_set() -> set[str]:
    word_set: set[str] = set()
    with open("word3.txt", mode="r") as f:
        [word_set.add(line.strip()) for line in f.readlines()]
    return word_set

class PathFinder:
    def __init__(self, first_word: str, second_word: str) -> None:
        self.first_word: str = first_word
        self.second_word: str = second_word
        self.chars: list[str] = CHARS
        self.found_words: set[str] = set()

    def find_path(self) -> None | ParentNode:
        ...

class PathFinderLinkedQ(PathFinder):
    def __init__(self, words_set: set[str], first_word: str, second_word: str) -> None:
        super().__init__(first_word, second_word)
        self.words_set: set[str] = words_set
        self.buffer: LinkedQSimple[ParentNode] = LinkedQSimple()

    @staticmethod
    def __create_new_word(new_char: str, index: int, initial_word: str):
        assert(len(new_char) == 1)
        return initial_word[:index] + new_char + initial_word[index + 1:]

    def __contains__(self, key: str) -> bool:
        return key in self.words_set

    def __make_children(self, parent_node: ParentNode, index: int) -> None | ParentNode:
        initial_word = parent_node.word
        current_char = initial_word[index]
        
        for c in self.chars:
            if current_char == c:
                continue

            # Generate a new word at the index
            generated_word = self.__create_new_word(c, index, initial_word)
            generated_word_node = ParentNode(generated_word, parent_node)

            if generated_word == self.second_word:
                return generated_word_node

            # If the generated word is in the word store, append it to the stack
            self.buffer.enqueue(generated_word_node) if generated_word_node.word in self else None
        return None

    @override
    def find_path(self, max_iter: int = 20):
        current_words: LinkedQSimple[ParentNode] = LinkedQSimple()
        main_parent = ParentNode(self.first_word, None)
        current_words.enqueue(main_parent)

        i = 0
        while i < max_iter:
            i += 1
            # For every char
            for j in range(len(current_words)):
                current_node: ParentNode | None = current_words.dequeue()
                if current_node is None:
                    continue

                word = current_node.word

                if word in self.found_words:
                    continue

                self.found_words.add(word)
                for k in range(len(word)):
                    # get all possible words that exist with each char
                    res = self.__make_children(current_node, k)
                    if res is not None:
                        raise SolutionFound(res)

            current_words = self.buffer
            self.buffer = LinkedQSimple()

        print("Reached max_iter")
        raise IndexError

def main():
    # Second version, missing binary tree

    first_word = get_user_input("Enter your first word")
    second_word = get_user_input("Enter your first word")

    try: 
        parent_node = PathFinderLinkedQ(get_words_set(), first_word, second_word).find_path()
    except SolutionFound as e:
        parent_node: ParentNode = e.final_word
        word_queue: LinkedQSimple[str] = LinkedQSimple()

        while parent_node.parent is not None:
            word_queue.enqueue(parent_node.word)
            parent_node = parent_node.parent

        print(f"Found in {len(word_queue)} steps:")
        print(f"0: {first_word}")
        for i in range(len(word_queue)):
            print(f"{i + 1}: {word_queue.dequeue()}")

    except IndexError as e:
        print("Could not find solution within max iter (optional param)")

if __name__ == "__main__":
    main()

