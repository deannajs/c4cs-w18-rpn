#!/usr/bin/env python3

import operator
import logging
import sys
import math


def pplus(first, second):
	result = first * second / 100
	return first + result

def pminus(first, second):
	result = first * second / 100
	return first - result
	

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%+': pplus,
	'%-': pminus,
	'.': operator.floordiv,
	'&': operator.and_,
	'|': operator.or_,
	'~': operator.invert,
	'!': math.factorial,
}
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#sh = logging.StreamHandler(sys.stdout)
#logger.addHandler(sh)
#logger.basicConfig(level=logging.DEBUG)


def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			if (token == '~'):
				function = operators[token]
				arg1 = stack.pop()
				result = function(arg1)
				stack.append(result)	
			elif (token == '!'):
				function = operators[token]
				arg1 = stack.pop()
				result = function(arg1)
				stack.append(result)

			else:
				function = operators[token]
				arg2 = stack.pop()
				arg1 = stack.pop()
				result = function(arg1, arg2)
				stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()
	#logger.debug(stack)

def main():
	while True:
		print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
	main()
