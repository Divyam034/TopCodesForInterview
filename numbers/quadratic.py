# python program to find roots of quadratic equation

import math
def root(a,b,c):
    D = b*b-4*a*c
    sqr_val = math.sqrt(abs(D))
    if D == 0:
        return f"Roots are equal and real having value {-b/2*a}"
    elif D >0:
        return f"Roots are distinct and real having value {(-b - sqr_val)/2*a} and {(-b + sqr_val)/2*a}"
    else:
        return f"Roots are imaginary and distinct having value {-b/2*a}+i{sqr_val}"

print(root(1,4,4))