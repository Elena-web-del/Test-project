import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_x_any_type(self):
        """Негативный, символы в переменной Число1"""
        self.assertEqual(calc_me("string", 2,"+"), "ERROR: now it is does not supported")
        
    def test_y_any_type(self):
        """Негативный, символы в переменной Число2"""
        self.assertEqual(calc_me(1, "string","+"), "ERROR: now it is does not supported")
        
    def test_no_x_argument(self):
        """Негативный, вызов функции вез аргумента x"""
        self.assertEqual(calc_me(y = 3, oper = "+"), "ERROR: send me Number1")
        
    def test_no_y_argument(self):
        """Негативный, вызов функции вез аргумента y"""
        self.assertEqual(calc_me(x = 3, oper = "+"), "ERROR: send me Number2")
        
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_oper_neg(self):
        """Негативный, возведение в степень"""
        self.assertEqual(calc_me(4, 2,"^"), 16)

if __name__ == '__main__':
    unittest.main(verbosity=2)