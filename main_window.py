# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, -1, 10)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAddBill = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddBill.setObjectName("buttonAddBill")
        self.horizontalLayout.addWidget(self.buttonAddBill)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 19))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoadMonth = QtWidgets.QAction(MainWindow)
        self.actionLoadMonth.setEnabled(True)
        self.actionLoadMonth.setObjectName("actionLoadMonth")
        self.actionSaveMonth = QtWidgets.QAction(MainWindow)
        self.actionSaveMonth.setEnabled(True)
        self.actionSaveMonth.setObjectName("actionSaveMonth")
        self.action_info = QtWidgets.QAction(MainWindow)
        self.action_info.setObjectName("action_info")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_load = QtWidgets.QAction(MainWindow)
        self.action_load.setObjectName("action_load")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menuAbout.addAction(self.action_info)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_load)
        self.menuFile.addAction(self.action_exit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonAddBill.setText(_translate("MainWindow", "Adicionar Fatura"))
        self.menuAbout.setTitle(_translate("MainWindow", "&Ajuda"))
        self.menuFile.setTitle(_translate("MainWindow", "&Ficheiro"))
        self.actionLoadMonth.setText(_translate("MainWindow", "Carregar"))
        self.actionLoadMonth.setToolTip(_translate("MainWindow", "Carregar  apartir do ficheiro csv"))
        self.actionLoadMonth.setShortcut(_translate("MainWindow", "Shift+C"))
        self.actionSaveMonth.setText(_translate("MainWindow", "Guardar"))
        self.actionSaveMonth.setToolTip(_translate("MainWindow", "Guardar em ficheiro csv"))
        self.actionSaveMonth.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_info.setText(_translate("MainWindow", "&Info"))
        self.action_save.setText(_translate("MainWindow", "&Guardar"))
        self.action_load.setText(_translate("MainWindow", "&Carregar"))
        self.action_exit.setText(_translate("MainWindow", "&Sair"))