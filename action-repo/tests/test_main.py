import unittest
from src.main import hello_world, calculate_sum, calculate_product

class TestMain(unittest.TestCase):
    
    def test_hello_world(self):
        """Test hello_world function"""
        result = hello_world()
        self.assertEqual(result, "Hello, World!")
    
    def test_calculate_sum(self):
        """Test calculate_sum function"""
        self.assertEqual(calculate_sum(2, 3), 5)
        self.assertEqual(calculate_sum(-1, 1), 0)
        self.assertEqual(calculate_sum(0, 0), 0)
    
    def test_calculate_product(self):
        """Test calculate_product function"""
        self.assertEqual(calculate_product(2, 3), 6)
        self.assertEqual(calculate_product(-2, 3), -6)
        self.assertEqual(calculate_product(0, 5), 0)

if __name__ == '__main__':
    unittest.main() 