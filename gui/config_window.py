# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(399, 300)
        Dialog.setModal(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(290, 20, 81, 241))
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok | QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 281, 291))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayoutWidget = QWidget(self.tab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 261, 354))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setBaseSize(QSize(0, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75);
        self.label.setFont(font)
        self.label.setInputMethodHints(Qt.ImhNone)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setBaseSize(QSize(0, 20))
        self.label_2.setFont(font)
        self.label_2.setInputMethodHints(Qt.ImhNone)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setBaseSize(QSize(0, 20))
        self.label_3.setFont(font)
        self.label_3.setInputMethodHints(Qt.ImhNone)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setBaseSize(QSize(0, 20))
        self.label_4.setFont(font)
        self.label_4.setInputMethodHints(Qt.ImhNone)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setBaseSize(QSize(0, 20))
        self.label_5.setFont(font)
        self.label_5.setInputMethodHints(Qt.ImhNone)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.textHost = QLineEdit(self.formLayoutWidget)
        self.textHost.setObjectName(u"textHost")
        font1 = QFont()
        font1.setPointSize(16)
        self.textHost.setFont(font1)
        self.textHost.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
                                    "")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textHost)

        self.textPort = QLineEdit(self.formLayoutWidget)
        self.textPort.setObjectName(u"textPort")
        self.textPort.setFont(font1)
        self.textPort.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
                                    "")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textPort)

        self.textUser = QLineEdit(self.formLayoutWidget)
        self.textUser.setObjectName(u"textUser")
        self.textUser.setFont(font1)
        self.textUser.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
                                    "")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textUser)

        self.textPassword = QLineEdit(self.formLayoutWidget)
        self.textPassword.setObjectName(u"textPassword")
        self.textPassword.setFont(font1)
        self.textPassword.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
                                        "")
        self.textPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textPassword)

        self.textName = QLineEdit(self.formLayoutWidget)
        self.textName.setObjectName(u"textName")
        self.textName.setFont(font1)
        self.textName.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
                                    "")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.textName)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableConfig = QTableView(self.tab_2)
        self.tableConfig.setObjectName(u"tableConfig")
        self.tableConfig.setGeometry(QRect(0, 0, 281, 271))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75);
        self.tableConfig.setFont(font2)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configura\u00e7\u00f5es locais", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Host", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Usu\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nome da base", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Senha", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Porta", None))
        self.textHost.setPlaceholderText(QCoreApplication.translate("Dialog", u"localhost", None))
        self.textPort.setPlaceholderText(QCoreApplication.translate("Dialog", u"5432", None))
        self.textUser.setPlaceholderText(QCoreApplication.translate("Dialog", u"postgres", None))
        self.textPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"***********", None))
        self.textName.setPlaceholderText(QCoreApplication.translate("Dialog", u"autosystem", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("Dialog", u"Padr\u00e3o", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("Dialog", u"Adicionais", None))
    # retranslateUi
