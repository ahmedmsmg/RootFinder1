from sympy import *
def False_position(expr, l, u, max_iterations, epislon):
    x = symbols('x')
    z = expr.subs(x, l).evalf() * expr.subs(x, u).evalf()
    if z > 0 :
        return [], [] 
    if expr.subs(x, l).evalf() < 0:
        l_sign = 0
    else:
        l_sign = 1

    Approximations_roots = []
    Precision = []
    x_new = (((expr.subs(x, u).evalf() * l) - (expr.subs(x, l).evalf() * u)) / (expr.subs(x, u).evalf()- expr.subs(x, l).evalf()))
    i = 0
    while i < max_iterations:
        x_temp = x_new
        x_new = (((expr.subs(x, u).evalf() * l) - (expr.subs(x, l).evalf() * u)) / (expr.subs(x, u).evalf() - expr.subs(x, l).evalf()))
        if expr.subs(x, x_new).evalf() < 0:
            if l_sign == 0:
                 l= x_new
            else:
                u = x_new
        else:
            if l_sign == 1:
                l = x_new
            else:
                u = x_new
        Approximations_roots.append(x_new)
        if i == 0:
            Precision.append(0)
        else:
            Precision.append(abs((x_new - x_temp) / x_new))        
        if(Precision[i] < epislon and i != 0):
            break
        i = i + 1
    return Approximations_roots, Precision


        



    

