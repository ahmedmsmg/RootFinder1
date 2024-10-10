from sympy import *

def fixed_point(magic, numOfIterations, approx, first_guess):
    roots = []
    approxList = []
    x = symbols("x")
    magic = sympify(magic)  #Magic function
    if not check_conv_div(magic):
        return roots, approxList

    roots += {int(first_guess)}
    approxList += {0}
    iter = 0
    newApprox = float('inf')
    while iter < numOfIterations:
        roots += {magic.evalf(subs={x:roots[-1]})}
        newApprox = abs(((roots[-1] - roots[-2]) / roots[-1]))
        approxList += {newApprox}
        if newApprox < approx:
            break
        iter += 1
    #print(roots)
    #print(approxList)
    return roots, approxList


def check_conv_div(expr):
    y = 10000
    x = symbols("x")
    expr = sympify(expr)
    diffExpr = diff(expr, x)
    z = abs(diffExpr.subs(x, y).evalf())
    print(z)
    if(z >= 1):
        return 0
    else:
        return 1


# (roots,approxList) = fixed_point("exp(-x)",10,0.1)

# print(roots)
# print(approxList)