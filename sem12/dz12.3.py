import random
import unittest


def Quicksort(A):
    print(a)
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return Quicksort(L) + M + Quicksort(R)


# a = '123'
a = [1, 2, 3]


class TestType(unittest.TestCase):
    def test_Type(self):
        self.assertEqual(type(a), list, "should be list")


class TestElements(unittest.TestCase):
    def test_Elements(self):
        self.assertEqual(sum([str(i).isdigit() for i in a]), len(a),
                         "all elements should be numbers")


class TestInts(unittest.TestCase):
    def test_Ints(self):
        self.assertEqual(sum([type(i) == int for i in a]), len(a),
                         "all elements should be intagers")


if __name__ == "__main__":
    unittest.main()

print(Quicksort(a))
