import unittest
from monte_carlo import Equation
epsilon = 0.1
class MonteCarloIntegration(unittest.TestCase):
    def test_integral(self):
        integral = Equation("x^2").integral([(1,3)])
        expected = 26/3
        self.assertAlmostEqual(integral,expected,delta=epsilon)
        
        integral = Equation("x^2 + y^2 -10").integral([(-1,1),(-1,1)])
        expected = -112/3
        self.assertAlmostEqual(integral,expected,delta=epsilon)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Div.testName']
    unittest.main()
