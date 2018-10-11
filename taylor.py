__author__ = "Jamal Muradov"
#!/usr/bin/env python3

from math import *
from sympy import var
from mpmath import *

print('Maclaurin series(Taylor,a=0) and use variable x')
x = var('x')
function = input('Enter your function:')

if 'import' in function or 'system' in function:
    print("Malicious code terminated!")
    exit()
    
    
f = lambda x: eval(function)
n = int(input('Enter the number of terms:'))
a = int(input('Enter expansion point(a):'))

diff_list=list()

for i in range(n):
    diff_list.append(diff(f, a, i))
    
diff_list = list(map(int, diff_list))

def factorial(n):
    p = 1
    for i in range(1,n+1): p*=i
    return p

taylor_list = list()

for i in range(n):
    fun = lambda x: diff_list[i]/factorial(i)
    f1 = lambda x: (x-a)**i
    taylor_list.append(fun(x)*f1(x))

print("="*50,"Taylor expansion:\n","f(x)="+str(sum(taylor_list)),sep='\n')
