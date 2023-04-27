# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtWidgets
import res_rc

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(QMainWindow)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 612)
        MainWindow.setMinimumSize(QSize(842, 612))
        MainWindow.setMaximumSize(QSize(842, 612))
        icon = QIcon()
        icon.addFile(u":/icon/icons/unnamed.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.ctry_widget = QWidget(MainWindow)
        self.ctry_widget.setObjectName(u"ctry_widget")
        self.ctry_widget.setStyleSheet(u"background-color: qlineargradient(spread:pad x1:1, y1:1, x2:0, y2:0 stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Riffic;")
        self.main_table = QTableView(self.ctry_widget)
        self.main_table.setObjectName(u"main_table")
        self.main_table.setGeometry(QRect(10, 90, 821, 511))
        self.main_table.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.main_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_table.setShowGrid(False)
        self.main_table.horizontalHeader().setDefaultSectionSize(135)
        self.lbl_maybe = QLabel(self.ctry_widget)
        self.lbl_maybe.setObjectName(u"lbl_maybe")
        self.lbl_maybe.setGeometry(QRect(190, 120, 461, 211))
        self.lbl_maybe.setStyleSheet(u"color: White;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"")
        self.buttons_frame = QFrame(self.ctry_widget)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setGeometry(QRect(0, 10, 841, 71))
        self.buttons_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);")
        self.Frame_Buttons = QHBoxLayout(self.buttons_frame)
        self.Frame_Buttons.setObjectName(u"Frame_Buttons")
        self.btn_pusone = QPushButton(self.buttons_frame)
        self.btn_pusone.clicked.connect(self.openDialogWindow)
        self.btn_pusone.setObjectName(u"btn_pusone")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 30))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.btn_pusone.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Riffic"])
        font.setPointSize(13)
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.btn_pusone.setFont(font)
        self.btn_pusone.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pusone.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/kisspng-computer-icons-symbol-friendship-5b3ce20c10fd47.5944761315307166840696.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pusone.setIcon(icon1)
        self.btn_pusone.setIconSize(QSize(45, 45))

    def openDialogWindow(self):
        self.hide()
        self.Ui_Dialog = Ui_Dialog(self)
        self.Ui_Dialog.show()

        self.Frame_Buttons.addWidget(self.btn_pusone)

        self.btn_pusthree = QPushButton(self.buttons_frame)
        self.btn_pusthree.setObjectName(u"btn_pusthree")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.btn_pusthree.setPalette(palette1)
        self.btn_pusthree.setFont(font)
        self.btn_pusthree.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pusthree.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/kisspng-paper-clipboard-computer-icons-download-font-paper-text-5b404dadb980b3.2140126715309408457598.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pusthree.setIcon(icon2)
        self.btn_pusthree.setIconSize(QSize(45, 45))

        self.Frame_Buttons.addWidget(self.btn_pusthree)

        self.btn_pustwo = QPushButton(self.buttons_frame)
        self.btn_pustwo.setObjectName(u"btn_pustwo")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.btn_pustwo.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Riffic"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.btn_pustwo.setFont(font1)
        self.btn_pustwo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pustwo.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/img_516999.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pustwo.setIcon(icon3)
        self.btn_pustwo.setIconSize(QSize(45, 45))

        self.Frame_Buttons.addWidget(self.btn_pustwo)

        MainWindow.setCentralWidget(self.ctry_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FB Helper - \u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.lbl_maybe.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">\u041d\u0430\u0432\u0435\u0440\u043d\u043e\u0435 \u0437\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442</span></p><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\"> \u043a\u0430\u043a\u0430\u044f-\u0442\u043e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f</span></p></body></html>", None))
        self.btn_pusone.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.btn_pusthree.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430", None))
        self.btn_pustwo.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043f\u043e\u0441\u0442(\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430)", None))
    # retranslateUi

class Ui_Dialog(object):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self, Dialog):

        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(421, 321)
        Dialog.setMinimumSize(QSize(421, 321))
        Dialog.setMaximumSize(QSize(421, 321))
        icon = QIcon()
        icon.addFile(u":/icon/icons/unnamed.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad x1:1, y1:1, x2:0, y2:0 stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Riffic;")
        self.frame_names = QFrame(Dialog)
        self.frame_names.setObjectName(u"frame_names")
        self.frame_names.setGeometry(QRect(10, 10, 400, 300))
        self.frame_names.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame_names.setFrameShape(QFrame.StyledPanel)
        self.frame_names.setFrameShadow(QFrame.Raised)
        self.line_name = QLineEdit(self.frame_names)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setGeometry(QRect(70, 90, 261, 51))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.line_name.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Riffic"])
        font.setPointSize(16)
        self.line_name.setFont(font)
        self.line_name.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_name.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.line_name.setClearButtonEnabled(False)
        self.lbl_nick = QLabel(self.frame_names)
        self.lbl_nick.setObjectName(u"lbl_nick")
        self.lbl_nick.setGeometry(QRect(40, 20, 321, 61))
        self.buttn_pus = QPushButton(self.frame_names)
        self.buttn_pus.setObjectName(u"buttn_pus")
        self.buttn_pus.setGeometry(QRect(110, 150, 181, 91))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.buttn_pus.setPalette(palette1)
        self.buttn_pus.setFont(font)
        self.buttn_pus.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttn_pus.setMouseTracking(False)
        self.buttn_pus.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.buttn_pustwo = QPushButton(self.frame_names)
        self.buttn_pustwo.clicked.connect(self.closeDialogWindow)
        self.buttn_pustwo.setObjectName(u"buttn_pustwo")
        self.buttn_pustwo.setGeometry(QRect(10, 260, 131, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.buttn_pustwo.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Riffic"])
        font1.setPointSize(18)
        self.buttn_pustwo.setFont(font1)
        self.buttn_pustwo.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttn_pustwo.setMouseTracking(False)
        self.buttn_pustwo.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/img_251372.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttn_pustwo.setIcon(icon1)
        self.buttn_pustwo.setIconSize(QSize(35, 35))

    def closeDialogWindow(self):
        self.close()
        Ui_MainWindow = self.parent()
        Ui_MainWindow.show()
        Ui_MainWindow.setFocus()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"FB Helper - \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0433\u0440\u0443\u043f\u043f\u044b", None))
#if QT_CONFIG(tooltip)
        self.line_name.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">\u0412 \u0434\u0430\u043d\u043d\u043e\u0439 \u0433\u0440\u0430\u0444\u0435 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0418\u043c\u044f \u0438 \u0424\u0430\u043c\u0438\u043b\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f(\u0432\u0430\u0448\u0435\u0433\u043e \u0434\u0440\u0443\u0433\u0430), \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u043e \u0432\u0441\u0435 \u0432\u0430\u0448\u0438 \u0433\u0440\u0443\u043f\u043f\u044b.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.line_name.setText("")
        self.line_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: Vasya Pupkin", None))
        self.lbl_nick.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0418\u043c\u044f \u0438 \u0424\u0430\u043c\u0438\u043b\u0438\u044e:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.buttn_pus.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">\u0417\u0430\u043f\u0443\u0441\u043a\u0430\u0435\u0442 \u0441\u043a\u0440\u0438\u043f\u0442, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430 \u0432\u043e \u0432\u0441\u0435 \u0432\u0430\u0448\u0438 \u0433\u0440\u0443\u043f\u043f\u044b.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.buttn_pus.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.buttn_pustwo.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">\u0412\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442 \u0432\u0430\u0441 \u043e\u0431\u0440\u0430\u0442\u043d\u043e, \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.buttn_pustwo.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())
