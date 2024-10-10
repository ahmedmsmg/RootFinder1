import sys
sys.path.append('../frontend')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from frontend.main_frontend import Ui_RootFinder
from backend.roots_backend import RootsDialog
from sympy import * 

class RootFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.expr = ''
        self.ui = Ui_RootFinder()
        self.ui.setupUi(self)
        self.ui.MgcFnANDScndGs.setVisible(False)
        self.ui.CnclBtn.clicked.connect(self.cancel_expr)
        for button in self.ui.buttonGroup.buttons():
            button.clicked.connect(self.add_value)
        for button in self.ui.methodGroup.buttons():
            button.clicked.connect(self.change_box_visibility)
        self.ui.dltBtn.clicked.connect(self.backspace)
        self.ui.FndBtn.clicked.connect(self.find_roots)
        self.ui.equation.setEnabled(False)
        self.ui.equation.setStyleSheet('background-color: white; color: black;')
        
    def add_value(self):
        self.ui.equation.setText(self.ui.equation.text() + self.sender().text())
        if self.sender().text() == '^':
            self.expr += '**'
        elif self.sender().text() == 'sin':
            self.ui.equation.setText(self.ui.equation.text() + '(')
            self.expr += 'sin('
        elif self.sender().text() == 'cos':
            self.ui.equation.setText(self.ui.equation.text() + '(')
            self.expr += 'cos('
        elif self.sender().text() == 'e':
            self.ui.equation.setText(self.ui.equation.text() + '^(')
            self.expr += 'exp('
        elif self.sender().text() == 'π':
            self.expr += 'pi'
        else:
            self.expr += self.sender().text()

    def backspace(self):
        if self.ui.equation.text()[:-1] == '^' or self.ui.equation.text()[:-1] == 'π':
            self.expr = self.expr[:-2]
        else:
            self.expr = self.expr[:-1]
        self.ui.equation.setText(self.ui.equation.text()[:-1])

    def cancel_expr(self):
        self.ui.equation.setText('')
        self.expr = ''

    def change_box_visibility(self):
        if self.sender().text() == 'Fixed Point':
            self.ui.MgcFnANDScndGs.setVisible(True)
            self.ui.MgcFnANDScndGs.setPlaceholderText('Mgc Fn.')
        elif self.sender().text() == 'Secant':
            self.ui.MgcFnANDScndGs.setVisible(True)
            self.ui.MgcFnANDScndGs.setPlaceholderText('2nd guess')
        else:
            self.ui.MgcFnANDScndGs.setVisible(False)

    def find_roots(self):
        ok_for_submit = True
        lower_bound = higher_bound = first_guess = second_guess = None
        method = magic = ''
        
        if self.ui.Eps.text() == '':
            ok_for_submit = False
            self.ui.Eps.setStyleSheet('border: 1px solid red')
        else:
            self.ui.Eps.setStyleSheet('')
            eps = float(self.ui.Eps.text())

        if self.ui.MaxItt.text() == '':
            ok_for_submit = False
            self.ui.MaxItt.setStyleSheet('border: 1px solid red')
        else:
            self.ui.MaxItt.setStyleSheet('')
            it_num = int(self.ui.MaxItt.text())
            
        for radio_button in self.ui.methodGroup.buttons():
            if radio_button.isChecked():
                if radio_button.text() == 'Bisection' or radio_button.text() == 'False Position (Regula-Falsi)':
                    if self.ui.LowBnd.text() == '':
                        ok_for_submit = False
                        self.ui.LowBnd.setStyleSheet('border: 1px solid red')
                    else:
                        self.ui.LowBnd.setStyleSheet('')
                    if self.ui.HiBnd.text() == '':
                        ok_for_submit = False
                        self.ui.HiBnd.setStyleSheet('border: 1px solid red')
                    else:
                        self.ui.HiBnd.setStyleSheet('')
                    if self.ui.LowBnd.text() != '' and self.ui.HiBnd.text() != '':
                        lower_bound = float(self.ui.LowBnd.text())
                        higher_bound = float(self.ui.HiBnd.text())
                        method = radio_button.text()

                if radio_button.text() == 'Fixed Point':
                    try:
                        sympify(self.ui.MgcFnANDScndGs.text())
                        method = radio_button.text()
                        magic = self.ui.MgcFnANDScndGs.text()
                        first_guess = self.ui.FrstGs.text()                
                        self.ui.MgcFnANDScndGs.setStyleSheet('')
                    except:
                        self.ui.MgcFnANDScndGs.setStyleSheet('border: 1px solid red')
                        ok_for_submit = False
                if radio_button.text() == 'Newton\'s Raphson':
                    if self.ui.FrstGs.text() == '':
                        ok_for_submit = False
                        self.ui.FrstGs.setStyleSheet('border: 1px solid red')
                    else:
                        self.ui.FrstGs.setStyleSheet('')
                    if self.ui.FrstGs.text() != '':
                        first_guess = float(self.ui.FrstGs.text())
                        method = radio_button.text()
                if radio_button.text() == 'Secant':
                    if self.ui.FrstGs.text() == '':
                        ok_for_submit = False
                        self.ui.FrstGs.setStyleSheet('border: 1px solid red')
                    else:
                        self.ui.FrstGs.setStyleSheet('')
                    if self.ui.MgcFnANDScndGs.text() == '':
                        ok_for_submit = False
                        self.ui.MgcFnANDScndGs.setStyleSheet('border: 1px solid red')
                    else:
                        self.ui.MgcFnANDScndGs.setStyleSheet('')
                    if self.ui.FrstGs.text() != '' and self.ui.MgcFnANDScndGs.text() != '':
                        first_guess = float(self.ui.FrstGs.text())
                        second_guess = float(self.ui.MgcFnANDScndGs.text())
                        method = radio_button.text()


                if ok_for_submit:
                    try:
                        sympify(self.expr)
                        self.ui.equation.setStyleSheet('background-color: white; color: black;')
                        dlg = RootsDialog(self.expr, method, eps, it_num, lower_bound, higher_bound, first_guess, second_guess, magic ,self)
                        dlg.exec()
                    except SympifyError:
                        self.ui.equation.setStyleSheet('background-color: white; color: black; border: 1px solid red;')
                        print(self.expr)
                    
        return
        