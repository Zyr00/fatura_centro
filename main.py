import sys

from PyQt5.QtWidgets import (QApplication,
        QDialog,
        QFileDialog,
        QMainWindow,
        QMessageBox,
        QTableWidgetItem,
        QHeaderView
        )
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate

from main_window import Ui_MainWindow
from entry import Entry
from bill import Bill
from files import File

entries = []
bills = []
codes = []

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
        entries.clear()
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
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "Comma-separated values (*.csv)", options=options)
        if filename:
            if not filename.lower().endswith('.csv'):
                filename += '.csv'
            File.save(filename, bills, codes)


class BillWindow(QDialog):
    def __init__(self, parent=None, edit_pos=-1, bill=None):
        super().__init__(parent)
        loadUi("ui/bill.ui", self)
        global entries

        self.edit_pos = edit_pos
        if self.edit_pos != -1 and bill != None:
            self.lineSupplier.setText(bill.supplier)
            self.lineRegistry.setText(bill.registration)
            self.lineKms.setText(bill.kms)
            qtDate = QDate.fromString(bill.date, 'dd/MM/yyyy')
            self.dateEdit.setDate(qtDate)
            entries = bill.entries

        self.addEntry.clicked.connect(self.dialog)
        self.pushOk.clicked.connect(self.closeOk)
        self.pushCancel.clicked.connect(self.close)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(entries))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["Preço", "Código", "Numero Pneus", "Tamanho Pneus", "Obs", "Eliminar"])
        self.tableWidget.cellPressed.connect(self.edit)
        self.update_list()

    def closeOk(self):
        try:
            b = Bill(self.dateEdit.date(),
                    self.lineSupplier.text(),
                    self.lineRegistry.text(),
                    self.lineKms.text(), entries)
            if self.edit_pos != -1:
                bills[self.edit_pos] = b
            else:
                bills.append(b)
                entries.clear()
            self.close()
        except Exception as e:
            print("I am breaking here")
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
                entries.pop(row)
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

    codes = File.load(File.file)

    w = MainWindow()
    w.show()
    sys.exit(app.exec())
