import sys

from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QMessageBox)
from PyQt5.uic import loadUi

from main_window import Ui_MainWindow
from bill_window import Ui_BillWindow
from entry import Entry

entries = []

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = None
        self.setupUi(self)
        self.action_load.triggered.connect(self.loadMonth)
        self.action_save.triggered.connect(self.saveMonth)
        self.action_info.triggered.connect(self.about)
        self.action_exit.triggered.connect(self.close)
        self.buttonAddBill.clicked.connect(self.addBill)

    def about(self):
        QMessageBox.about(self, "Informação sobre a aplicação",
             "<h2>Autor: </h2>"
             "<h4>&nbsp;&nbsp;&nbsp;&nbsp; João cunha</h4>",
             )

    def loadMonth(self):
        print("Load month")

    def saveMonth(self):
        print("Save month")

    def addBill(self):
        if BillWindow.bill_is_open == 0:
            self.w = BillWindow()
            self.w.show()

class BillWindow(QMainWindow, Ui_BillWindow):
    bill_is_open = 0;

    def __init__(self, parent=None):
        super().__init__(parent)
        bill_is_open = 1
        self.setupUi(self)
        self.addEntry.clicked.connect(self.dialog)

    def closeEvent(self, event):
        bill_is_open = 0
        event.accept()

    def dialog(self):
        dialog = Dialog(self)
        dialog.exec()
        print(entries)

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/dialgo.ui", self)
        self.dialogOk.clicked.connect(self.ok)

    def ok(self):
        try:
            e = Entry(
                self.linePrice.text(),
                self.lineCode.text(),
                self.lineNTires.text(),
                self.lineSize.text(),
                self.textDescription.toPlainText())
            entries.append(e)
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
