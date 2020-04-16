import unittest
from SimplyCal import SimplyCal



class AdditionCase(unittest.TestCase):
    def setUp(self):
        self.simplyCal = SimplyCal()

    def tearDown(self):
        """use after every test"""
        print("after the test case. Results ")

    def test_add(self):
        result = self.simplyCal.add(1,1)
        self.assertEqual(result, 2)

    def test_adddecimal(self):
        result = self.simplyCal.add(2.5, 6.8)
        self.assertEqual(result, 9.3 )

    def test_addNegative(self):
        result = self.simplyCal.add(-1,1)
        self.assertEqual(result,0)

    def test_subtract(self):
        result = self.simplyCal.subtract(2,1)
        self.assertEqual(result, 1)

    def test_subtractdecimal(self):
        result = self.simplyCal.subtract(8.9,1.1)
        self.assertEqual(result, 7.8)

    def test_subtractNegative(self):
        result = self.simplyCal.subtract(-1,1)
        self.assertEqual(result,-2)


    def test_multiply(self):
        result = self.simplyCal.multiply(4,5)
        self.assertEqual(result, 20)

    def test_multiplyNegative(self):
        result = self.simplyCal.multiply(-1,1)
        self.assertEqual(result,-1)

    def test_divide(self):
        result = self.simplyCal.divide(2,4)
        self.assertEqual(result, .5)

    def test_divideNegative(self):
        result = self.simplyCal.add(-1,1)
        self.assertEqual(result,1)

    def test_dividedecimal(self):
        result = self.simplyCal.divide(2,5)
        self.assertEqual(result, 2.5)


        result = self.simplyCal.divide(10,0)
        self.assertRaises(ValueError)



if __name__ == '__main__':
    unittest.main()
