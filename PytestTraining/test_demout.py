"""using unit test"""

import unittest
from psutils import power

class CustomTestCase(unittest.TestCase):
    def test_power_1(self):
        self.assertEqual(power(2, 3),8)

    def test_power_2(self):
        self.assertNotEqual(power(2, 3),18)

if __name__ == '__main__':
    unittest.main()