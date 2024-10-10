from pydoc import synopsis
from sympy import *

def Secant(expr,X0,X1,iter,eps):
    x=symbols('x')
    xi=X1
    xio=X0
    errs=[]
    app_root=[]
    i=0
    while i < iter:
        fx1 = expr.subs(x,xi).evalf()
        fx0 = expr.subs(x,xio).evalf()
        x_new = xi - fx1*((xi-xio)/(fx1-fx0))
        err=abs((x_new-xi)/x_new)
        errs.append(err)
        app_root.append(x_new)
        xio=xi
        xi=x_new
        if err < eps:
            break
        i = i+1
    return app_root,errs



