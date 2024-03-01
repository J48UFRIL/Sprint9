import unittest
from resta import restar

class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(0, 0), 0)
        self.assertEqual(restar(-5, 3), -8)
        self.assertEqual(restar(10, -3), 13)

if __name__ == '__main__':
    unittest.main()