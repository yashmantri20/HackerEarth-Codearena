'''Assume there is an Ideal Random Number Generator which generates any real number between 0 and given integer. Two numbers are generated from the above generator using integer A and B, let's assume the numbers generated are X1 and X2. There is another integer C. What is the probability that summation of X1 and X2 is less than C.

Input Format
A single line containing three integers A,B,C
1 <= A,B,C <= 100000

Output Format
Print the probability in form of P/Q

Problem Setter: Practo Tech Team

SAMPLE INPUT 
1 1 1
SAMPLE OUTPUT 
1/2
Explanation
For example if A and B are 1. Then the random number generated will be any real number between 0 - 1.

0 < x1 < 1 0 < x2 < 1

If C is also 1, then you need to determine the probability of that x1 + x2 < C.'''

from itertools import product
from fractions import Fraction

tmp = input().split()
A,B,C = [int(i) for i in tmp]
if A+B <= C: 
    fr = Fraction(1,1)
elif C <= A and C <= B: 
    fr = Fraction(C**2,(2*A*B))
elif C <= B: 
    fr = Fraction(2*C*A-A**2,(2*A*B))
elif C <= A: 
    fr = Fraction(2*C*B-B**2,(2*A*B))
else: 
    fr = Fraction((2*C*(A+B)-A**2-B**2-C**2),(2*A*B))
print(fr.numerator,'/',fr.denominator,sep='')