

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20,30,70]))
    434.0
    """
    return sum(values,0.0)/len(values)

import  unittest
class uttest1(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20,30,70]),40.0)

unittest.main()



