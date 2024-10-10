from sympy import *


def bisection(expr, l, u, max_iterations, epislon):
    x = symbols('x')
    z = expr.subs(x, l).evalf() * expr.subs(x, u).evalf()
    if z > 0:
        return [], []
    if expr.subs(x, l).evalf() < 0:
        l_sign = 0
    else:
        l_sign = 1

    Approximations_roots = []
    Precision = []
    mid = (l + u) / 2
    i = 0
    print('started bisection')
    while i < max_iterations:
        mid_temp = mid
        mid = (l + u) / 2
        if expr.subs(x, mid).evalf() < 0:
            if(l_sign == 0):
                l = mid
            else:
                u = mid
        else:
            if(l_sign == 1):
                l = mid
            else:
                u = mid
        Approximations_roots.append(mid)
        if i == 0:
            Precision.append(0)
        else:
            Precision.append(abs((mid - mid_temp) / mid))
        if Precision[len(Precision) - 1] < epislon and i != 0:
            break
        i = i + 1
    return Approximations_roots, Precision


    

