from sympy import *
from random import randint,choice
MAX_DEGREE=3
MIN_DEGREE=1

#parameters for normal polinomials
MIN_FACT=-5
MAX_FACT=10
#parameters for linear terms like a*(b-c*x)**d
MIN_L_FACT=-10
MAX_L_FACT=10
#Parameters for e Terms like e**x etc pp
MIN_E_FACT=-7
MAX_E_FACT=9
MAX_E_DEGREE=3
MIN_E_DEGREE=1
#Simply the derivatives and priors ? not recommended due to a lack of arithmetic polynomial reshaping skills of the author
DO_SIMPLIFY= False
def simple(x):
	if DO_SIMPLIFY:
		return simplify(x)
	else:
		return x

def create_term(back_end=False):#wraps the functions of the file to make it usable for further better concartinations of terms like kettenregel (where it is used already)
	t1 = create_polynomial()
	t2 = create_E1()
	t3 = create_polynomial2()
	t4 = create_linconc()
	t6 = create_trignometric()
	pos = [t1,t2,t3,t4,t6]
	if not back_end:
		t5=  create_polichain()
	else:
		return (choice(pos),choice(pos))
	return choice([(t6,1),(t3,1),(t1,1),(t2,0),(t4,0),(t5,0)])

def create_trignometric(x=Symbol("x")):
	factors = [randint(MIN_FACT,MAX_FACT) for i in range(3)]
	factor = choice([-1,1])
	kind = choice([-1,1])
	if kind <0:
		poly = sin(factors[1]*x)
	else:
		poly = cos(factors[1]*x)
	poly = factor*factors[0]*poly+factors[2]
	return poly



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

def create_polynomial(x=Symbol("x")):#factures included name is missleading a bit
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
