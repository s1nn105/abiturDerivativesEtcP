from sympy import *
from random import randint,choice
MAX_DEGREE=5
MIN_DEGREE=1
MAX_E_DEGREE=3
MIN_E_DEGREE=1
MAX_C_DEGREE=4
MIN_C_DEGREE=2
MIN_FACT=-3
MAX_FACT=20
MIN_L_FACT=-10
MAX_L_FACT=10
MIN_E_FACT=-7
MAX_E_FACT=9
DO_SIMPLIFY= False
def simple(x):
	if DO_SIMPLIFY:
		return simplify(x)
	else:
		return x

def create_term(back_end=False):
	t1 = create_polynomial()
	t2 = create_E1()
	t3 = create_polynomial2()
	t4 = create_linconc()
	pos = [t1,t2,t3,t4]
	if not back_end:
		t5=  create_polichain()
	else:
		return (choice(pos),choice(pos))
	return choice([(t3,1),(t1,1),(t2,0),(t4,0),(t5,0)])

def create_polynomial2(x=Symbol("x")):
	degree =randint(MIN_DEGREE,MAX_DEGREE)
	factors = [randint(MIN_FACT,MAX_FACT) for i in range(degree+1)]
	factors2 = [choice([-1,1]) for i in range(degree+1)]
	polynomial=[0]
	for i in range(degree,-1,-1):
		if randint(-4,2)>0:
			pass
		elif randint(-2,1)>0:
			polynomial.append(factors2[i]*factors[i]*x**(-1))	
		else:		
			polynomial.append(factors2[i]*factors[i]*x**(degree-i))
	#print(polynomial)
	pol=polynomial.pop()
	#print(pol)
	for i in polynomial:
		pol = pol+i
	#print(pol)
	return pol

def create_polynomial(x=Symbol("x")):
	degree =randint(MIN_DEGREE,MAX_DEGREE)
	factors = [randint(MIN_FACT,MAX_FACT) for i in range(degree+1)]
	factors2 = [randint(MIN_DEGREE,MAX_DEGREE) for i in range(degree+1)]
	factors3 = [choice([-2,-3,-1,1,2]) for i in range(degree+1)]
	polynomial=[0]
	for i in range(degree,-1,-1):
		if randint(-4,2)>0:
			pass
		else:		
			polynomial.append(factors[i]*x**(factors2[i]*factors3[i]))
	#print(polynomial)
	pol=polynomial.pop()
	#print(pol)
	for i in polynomial:
		pol = pol+i
	#print(pol)
	return pol

def create_polichain(x=Symbol("x")):#name ???
	terms = create_term(back_end=True)
	return terms[0]*terms[1]

def create_linconc(x=Symbol("x")):
	factors = [randint(MIN_L_FACT,MAX_L_FACT) for i in range(4)]
	factor2 = randint(MIN_DEGREE,MAX_DEGREE)
	factor3 = choice([-2,-1,1,2,1,2,1]) 	
	term = factors[0]*(factors[1]+factors[2]*x**(factor3))**(factor2)+factors[3]

	return term

#create_polynomial()

def create_E1(x=Symbol("x")):#TODO proper Variable rename 
	degree =randint(MIN_E_DEGREE,MAX_E_DEGREE)
	factors = [randint(MIN_E_FACT,MAX_E_FACT) for i in range(degree+1)]
	factors2 = [randint(MIN_E_FACT,MAX_E_FACT) for i in range(degree+1)]
	factors3 = [choice([-2,-3,-1,1,2,3]) for i in range(degree+1)]
	polynomial=[]
	for i in range(degree,-1,-1):
		polynomial.append(factors[i]*E**(factors2[i]*x**factors3[i]))
	#print(polynomial)
	pol=polynomial.pop()
	#print(pol)
	for i in polynomial[:-2]:
		pol = pol+i
	#print(pol)
	return pol
