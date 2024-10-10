from sympy import *

def Newton_Rhapson(expr,X0,iter,eps):
    x = symbols('x')
    xi = X0
    drev = diff(expr,x)
    errs=[]
    app_root=[]
    i=0
    while i < iter:
        x_new=xi - (expr.subs(x,xi).evalf()/drev.subs(x,xi).evalf())
        err=abs((x_new-xi)/x_new)
        errs.append(err)
        app_root.append(x_new)
        xi=x_new
        if err < eps:
            break
        i= i+1
    return app_root, errs


