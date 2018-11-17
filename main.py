import sys
from PyQt5.QtWidgets import *

from Pages.MainLoginPage import *
from DialogBox.EventDialogBox import *
from DialogBox.newUserRegistartion import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MdTouch")
        self.loginpage = Ui_MainLoginWindow()
        self.loginpage.setupUi(self)
        self.setFixedSize(1390,915)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
