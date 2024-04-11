import unittest
import pandas

myData = pandas.DataFrame()
newData = myData.abs()
myData.describe()


from m_reading import add
#myCase = unittest.TestCase()

class TestAddMethod(unittest.TestCase):
    def test_positives(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_negatives(self):
        result = add(-3, -5)
        self.assertEqual(result, -8)

    def test_mix(self):
        result = add(-3, 5)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
