import sys

from PyQt5.QtWidgets import (QApplication,
        QDialog,
        QMainWindow,
        QMessageBox,
        QTableWidgetItem,
        QHeaderView
        )
from PyQt5.uic import loadUi

from main_window import Ui_MainWindow
from entry import Entry
from bill import Bill

entries = []
bills = []

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.action_load.triggered.connect(self.loadMonth)
        self.action_save.triggered.connect(self.saveMonth)
        self.action_info.triggered.connect(self.about)
        self.action_exit.triggered.connect(self.close)
        self.buttonAddBill.clicked.connect(self.addBill)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(bills))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["Data", "Fornecedor", "Matrícula", "KMs", "Numero Entradas", "Eliminar"])
        self.tableWidget.cellPressed.connect(self.edit)

    def addBill(self):
        dialog = BillWindow(self)
        dialog.exec()
        self.update_list()

    def edit(self, row, col):
        if col == 5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Eliminar Fatura")
            msg.setText(f"Eliminar fatura com os valores:\n {bills[row]}")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnvalue = msg.exec()
            if returnvalue == QMessageBox.Ok:
                bills.pop(row)
                self.update_list()
        else:
            b = bills[row]
            dialog = BillWindow(self, row, b)
            dialog.exec()
            self.update_list()

    def update_list(self):
        self.tableWidget.setRowCount(len(bills))
        for i in range(len(bills)):
            b = bills[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(b.date))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(b.supplier))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(b.registration))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(b.kms))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(len(b.entries))))
            self.tableWidget.setItem(i, 5, QTableWidgetItem("Eliminar"))

    def about(self):
        QMessageBox.about(self, "Informação sobre a aplicação",
             "<h2>Autor: </h2>"
             "<h4>&nbsp;&nbsp;&nbsp;&nbsp; João cunha</h4>",
             )

    def loadMonth(self):
        print("Load month")

    def saveMonth(self):
        print("Save month")


class BillWindow(QDialog):
    def __init__(self, parent=None, edit=-1, bill=None):
        super().__init__(parent)
        loadUi("ui/bill.ui", self)
        self.addEntry.clicked.connect(self.dialog)
        self.pushOk.clicked.connect(self.closeOk)
        self.pushCancel.clicked.connect(self.close)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(entries))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["Preço", "Código", "Numero Pneus", "Tamanho Pneus", "Obs", "Eliminar"])
        self.tableWidget.cellPressed.connect(self.edit)

    def closeOk(self):
        try:
            b = Bill(self.dateEdit.date(),
                    self.lineSupplier.text(),
                    self.lineRegistry.text(),
                    self.lineKms.text(), entries)
            bills.append(b)
            entries.clear()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro: {e}")

    def dialog(self):
        dialog = Dialog(self)
        dialog.exec()
        self.update_list()

    def edit(self, row, col):
        if col == 5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Eliminar Entrada")
            msg.setText(f"Eliminar entrada com os valores:\n {entries[row]}")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnvalue = msg.exec()
            if returnvalue == QMessageBox.Ok:
                bill.pop(row)
                self.update_list()
        else:
            e = entries[row]
            dialog = Dialog(self, row, e.price, e.code, e.ntires, e.size, e.obs)
            dialog.exec()
            self.update_list()

    def update_list(self):
        self.tableWidget.setRowCount(len(entries))
        for i in range(len(entries)):
            e = entries[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(e.price))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(e.code))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(e.ntires))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(e.size))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(e.obs))
            self.tableWidget.setItem(i, 5, QTableWidgetItem("Eliminar"))

class Dialog(QDialog):
    def __init__(self, parent=None, edit_pos=-1, price=None, code=None, ntires='0', size='0', obs=None):
        super().__init__(parent)
        loadUi("ui/dialgo.ui", self)
        self.dialogOk.clicked.connect(self.ok)
        self.linePrice.setText(price)
        self.lineCode.setText(code)
        self.lineNTires.setText(ntires)
        self.lineSize.setText(size)
        self.textDescription.setPlainText(obs)
        self.edit_pos = edit_pos

    def ok(self):
        try:
            e = Entry(
                    self.linePrice.text(),
                    self.lineCode.text(),
                    self.lineNTires.text(),
                    self.lineSize.text(),
                    self.textDescription.toPlainText())
            if self.edit_pos != -1:
                entries[self.edit_pos] = e
            else:
                entries.append(e)
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
