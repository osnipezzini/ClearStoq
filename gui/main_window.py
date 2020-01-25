# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 264)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 321, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelDate = QLabel(self.formLayoutWidget)
        self.labelDate.setObjectName(u"labelDate")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelDate)

        self.dateEdit = QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEdit)

        self.labelEmpresa = QLabel(self.formLayoutWidget)
        self.labelEmpresa.setObjectName(u"labelEmpresa")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelEmpresa)

        self.comboEmpresa = QComboBox(self.formLayoutWidget)
        self.comboEmpresa.setObjectName(u"comboEmpresa")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboEmpresa)

        self.textLog = QTextBrowser(self.centralwidget)
        self.textLog.setObjectName(u"textLog")
        self.textLog.setGeometry(QRect(10, 60, 321, 121))
        self.buttonReady = QPushButton(self.centralwidget)
        self.buttonReady.setObjectName(u"buttonReady")
        self.buttonReady.setGeometry(QRect(200, 190, 131, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 338, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelDate.setText(QCoreApplication.translate("MainWindow", u"Data Movto", None))
        self.labelEmpresa.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.buttonReady.setText(QCoreApplication.translate("MainWindow", u"Limpar tabelas", None))
    # retranslateUi
