from PyQt5 import QtWidgets
from backend.main_backend import RootFinder 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root_finder = RootFinder()
    root_finder.show()
    sys.exit(app.exec_())