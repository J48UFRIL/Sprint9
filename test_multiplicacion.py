import unittest
from multiplicacion import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(0, 0), 0)
        self.assertEqual(multiplicar(-5, 3), -15)
        self.assertEqual(multiplicar(10, -3), -30)

if __name__ == '__main__':
    unittest.main()