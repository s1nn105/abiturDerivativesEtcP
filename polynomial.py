from sympy import *
from random import randint
MAX_DEGREE=5
MIN_DEGREE=1
MIN_FACT=1
MAX_FACT=20
DO_SIMPLIFY= False
def simple(x):
	if DO_SIMPLIFY:
		return simplify(x)
	else:
		return x
def create_polynomial(x=Symbol("x")):
	degree =randint(MIN_DEGREE,MAX_DEGREE)
	factors = [randint(MIN_FACT,MAX_FACT) for i in range(degree+1)]
	polynomial=[]
	for i in range(degree,-1,-1):
		polynomial.append(factors[i]*x**(degree-i))
	#print(polynomial)
	pol=polynomial.pop()
	#print(pol)
	for i in polynomial:
		pol = pol+i
	#print(pol)
	return pol
#create_polynomial()
