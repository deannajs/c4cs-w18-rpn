import unittest
import rpn

class TestBasics(unittest.TestCase):
	#def test_add(self):
	#	result = rpn.calculate("1 1 +")
	#	self.assertEqual(2, result)
	#def test_subtract(self):
	#	result = rpn.calculate("5 3 -")
	#	self.assertEqual(2, result)
	#def test_multiply(self):
	#	result = rpn.calculate("5 3 *")
	#	self.assertEqual(15, result)
	#def test_divide(self):
	#	result = rpn.calculate("6 3 /")
	#	self.assertEqual(2, result)
	#def test_toomany(self):
	#	with self.assertRaises(TypeError):
	#		result = rpn.calculate("1 2 3 +")
	#def test_pow(self):
	#	result = rpn.calculate("2 3 ^")
	#	self.assertEqual(8, result)
	#def test_percentplus(self):
	#	result = rpn.calculate("72 5 %+")
	#	self.assertEqual(75.6, result)
	#def test_percentminus(self):
	#	result = rpn.calculate("72 20 %-")
	#	self.assertEqual(57.6, result)
	#def test_intdivision(self):
	#	result = rpn.calculate("10 3 .")
	#	self.assertEqual(3, result)
	#def test_and(self):
	#	result = rpn.calculate("10 3 &")
	#	self.assertEqual(2, result)
	#def test_or(self):
	#	result = rpn.calculate("10 3 |")
	#	self.assertEqual(11, result)
	#def test_not(self):
	#	result = rpn.calculate("-6 ~")
	#	self.assertEqual(5, result)
	def test_factorial(self):
		result = rpn.calculate("4 !")
		self.assertEqual(24, result)
