import unittest

from main import ArrayQ


class QueueTests(unittest.TestCase):

    def test_queue(self):
        q = ArrayQ()
        q.enqueue(1)
        q.enqueue(2)
        x = q.dequeue()
        y = q.dequeue()
        if (x == 1 and y == 2):
            print("OK")
        else:
            print("FAILED")

        self.assertEqual(x, 1)
        self.assertEqual(y, 2)


if __name__ == "__main__":
    _ = unittest.main()
