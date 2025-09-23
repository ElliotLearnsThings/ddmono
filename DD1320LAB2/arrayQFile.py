from array import array
from typing import Any, override


class ArrayQ:
    def __init__(self) -> None:
        self.__array = array("l")
        self.__type = "l - i32"
        self.length = 0

    @override
    def __str__(self) -> str:
        return f"Queue object with type: {self.__type} has values {self.get_all()}"

    def enqueue(self, val: Any) -> None:
        """
        Inserts a val object to the end of internal array
        val: any
        returns: None
        """
        try:
            self.length += 1
            self.__array.append(val)
        except TypeError as e:
            raise TypeError(f"Error enqueue val, type error, insert val: {val}, expected type: {self.__type}") from e
        except Exception as e:
            raise Exception(f"Unhandled error enqueue val") from e

    def insert(self, val: Any, index: int = 0) -> None:
        """
        Inserts a val object to start of internal array, with optional index
        val: Any
        index: int
        returns: None
        """
        try:
            self.length += 1
            self.__array.insert(index, val)
        except TypeError as e:
            raise TypeError(f"Error enqueue val, type error, insert val: {val}, expected type: {self.__type}") from e
        except Exception as e:
            raise Exception(f"Unhandled error enqueue val") from e

    def pop(self, index: int = -1) -> Any:
        """
        Removes a val object at the given index of internal array
        returns: Any
        """
        try:
            if (self.length == 0):
                return
            self.length -= 1
            return self.__array.pop(index)
        except IndexError as e:
            raise IndexError(f"Error dequeue val, index error") from e
        except Exception as e:
            raise Exception(f"Unhandled error in dequeue val") from e

    def dequeue(self) -> Any:
        """
        Removes a val object at the start of internal array
        returns: Any
        """
        index = 0
        try:
            if (self.length == 0):
                return
            self.length -= 1
            return self.__array.pop(index)
        except IndexError as e:
            raise IndexError(f"Error dequeue val, index error") from e
        except Exception as e:
            raise Exception(f"Unhandled error in dequeue val") from e

    @override
    def __getitem__(self, index: int) -> Any:
        return self.__array[index]

    def get_all(self) -> list[Any]:
        return [self[i] for i in range(self.length)]

def main():
    myQueue = ArrayQ()
    print(myQueue)
    myQueue.enqueue(1)
    print(myQueue[0])

    print(myQueue.get_all())

if __name__ == "__main__":
    main()

