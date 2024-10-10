import sys

from backend.Secant import Secant
sys.path.append('../frontend')
sys.path.append('../backend')

from sympy import *
import datetime

from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from frontend.roots_frontend import Ui_roots
from backend.Bisection import bisection
from backend.False_position import False_position
from backend.fixed_point import fixed_point
from backend.Newton_Rhapson import Newton_Rhapson

class RootsDialog(QDialog):
    def __init__(self, expr, method, eps, it_num, lower_bound, higher_bound, first_guess, second_guess, magic, parent=None):
        super().__init__(parent)
        self.ui = Ui_roots()    
        self.ui.setupUi(self)
        self.equation = sympify(expr)
        expr = expr.replace('**', '^')
        # print(expr)
        # x = symbols('x')
        # z = expr.subs(x, 0)
        # print(z)
        self.ui.expr.setText(expr)
        self.ui.state.setText('Calculating...')
        self.ui.finish.clicked.connect(self.end_session)
        self.find_roots(self.equation, method, eps, it_num, lower_bound, higher_bound, first_guess, second_guess,magic)

    def find_roots(self, expr, method, eps, it_num, lower_bound, higher_bound, first_guess, second_guess,magic):
        roots = precisions = []
        start_time = datetime.datetime.now()
        self.ui.method.setText(method)
        
        if method == 'Bisection':
            roots, precisions = bisection(expr, lower_bound, higher_bound, it_num, eps)
        elif method == 'False Position (Regula-Falsi)':
            roots, precisions = False_position(expr, lower_bound, higher_bound, it_num, eps)
        elif method == 'Fixed Point':
            roots,precisions = fixed_point(magic, it_num, eps, first_guess)
        elif method == 'Newton\'s Raphson':
            roots,precisions = Newton_Rhapson(expr,first_guess,it_num,eps)
        elif method == 'Secant':
            roots,precisions = Secant(expr,first_guess,second_guess,it_num,eps)

        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        
        if len(roots) == 0:
            if method == 'Bisection' or method == 'False Position (Regula-Falsi)':
                self.ui.expr.setText('Higher and lower bounds have same sign')
            elif method == 'Fixed Point':
                self.ui.expr.setText('Magic function does not converge')
            self.ui.state.setText('ERROR')
            self.ui.state.setStyleSheet('color: red')
            self.ui.expr.setStyleSheet('color: red')
        else:
            self.ui.IttTbl.setRowCount(len(roots))

            for i in range(len(roots)):
                self.ui.IttTbl.setItem(i, 0, QTableWidgetItem(str(i + 1)))
                self.ui.IttTbl.setItem(i, 1, QTableWidgetItem(str(round(roots[i], 10))))
                self.ui.IttTbl.setItem(i, 2, QTableWidgetItem(str(round(precisions[i], 10))))
                
            self.ui.ans.setText(str(round(roots[len(roots) - 1], 10)))
            self.ui.precision.setText(str(round(precisions[len(precisions) - 1], 10)))
            self.ui.state.setText('Done!!!')
            self.ui.time.setText(str(execution_time))
    
    def end_session(self):
        self.close()
        
