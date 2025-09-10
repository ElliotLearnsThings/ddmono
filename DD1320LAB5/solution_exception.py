from graph import ParentNode


class SolutionFound(Exception):
    def __init__(self, final_word: ParentNode, *args: object) -> None:
        super().__init__(*args)
        self.final_word: ParentNode = final_word

