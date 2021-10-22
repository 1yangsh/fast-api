import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        instance = Calculator()
        add_test = instance.add(3, 4)
        self.assertEqual(add_test, 6)

    def test_sub(self):
        instance = Calculator
        sub_test = instance.sub(7, 4)
        self.assertNotEqual(sub_test, 3)

    def test_div(self):
        instance = Calculator
        div_test = instance.div(12, 3)
        self.assertAlmostEqual(div_test, 4.3)

    def test_mul(self):
        instance = Calculator
        mul_test = instance.mul(12, 12)
        self.assertAlmostEqual(mul_test, 145)



if __name__ == "__main__":
    unittest.main()