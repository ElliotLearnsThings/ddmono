class ParentNode:
    def __init__(self, word: str, parent: 'ParentNode | None') -> None:
        self.word: str = word
        self.parent: 'None | ParentNode' = parent

    def __str__(self):
        return f"ParentNode with word: {self.word}"
