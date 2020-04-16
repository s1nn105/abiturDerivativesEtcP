from sympy import *
from polynomial import *
import sys
import time
init_printing()
polynomial,ad = create_term()
x = Symbol('x')
f= polynomial #everybody likes f(x) instead of polynomial(x)
# first the derivative
print(pretty(f))
print("Whats the derivative ? ")
t1 = time.time()
input("press any key if finished")
t2=time.time()
print(f"you needed {int(t2-t1)} seconds here is the derivative")
td=int(t2-t1)

print(pretty(simple(diff(f,x))))
if ad==0:
	sys.exit(0)
input("Ready ? ")
print()
print("Whats the Antiderivative ? ")
print(pretty(Integral(f)))
t1 = time.time()
input("press any key if finished")
t2=time.time()
print(f"you needed {int(t2-t1)} seconds here is the derivative")

print(pretty((integrate(f))))
tad = int(t2-t1)
print("The times :")
print(f"f'(x):{td}")
print(f"F(x):{tad}")
