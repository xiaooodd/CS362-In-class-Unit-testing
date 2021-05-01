import unittest
import calculator

class TestCalculator(unittest.TestCase):
# Test calculator.py
    def test_addition(self):
        self.assertEqual(calculator.addition(1,1),2.0)
        self.assertEqual(calculator.addition(2,3),5.0)
        
    def test_substraction(self):
        self.assertEqual(calculator.subtraction(2,1),1.0)
        self.assertEqual(calculator.subtraction(1,2),-1.0)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(1,1),1.0)
        self.assertEqual(calculator.multiplication(10,10),100.0)
    
    def test_division(self):
        self.assertEqual(calculator.division(1,1),1.0)
        self.assertEqual(calculator.division(1,2),0.5)

if __name__ == '__main__':
    unittest.main(verbosity = 2)