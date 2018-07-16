# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Queing System -- Updated.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

"""
TODO: 
    Add "go back" button to stage 5
    Give more height to all labels, to accomodate for the new font
    make the UI in stage 5 more simple/tell them clearly what's going on
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from defaults import *

class PrinterUI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(DEFAULT_DIALOG_OBJECT_NAME)

        Dialog.resize(800, 400)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setWindowOpacity(1.0)
        Dialog.setStyleSheet(DEFAULT_DIALOG_STYLESHEET)

        self.lbl_St2_StudentIDDisplay = QtWidgets.QLabel(Dialog)
        self.lbl_St2_StudentIDDisplay.setEnabled(True)
        self.lbl_St2_StudentIDDisplay.setGeometry(QtCore.QRect(0, 100, 800, 32))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_LABEL_COMMON_FONT_FAMILY)
        font.setPointSize(15)
        self.lbl_St2_StudentIDDisplay.setFont(font)
        self.lbl_St2_StudentIDDisplay.setStyleSheet(DEFAULT_STYLE_SHEET_lbl_St2_StudentIDDisplay)
        self.lbl_St2_StudentIDDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_St2_StudentIDDisplay.setOpenExternalLinks(False)
        self.lbl_St2_StudentIDDisplay.setObjectName("lbl_St2_StudentIDDisplay")

        self.pb_St2_Num2 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num2.setEnabled(True)
        self.pb_St2_Num2.setGeometry(QtCore.QRect(360, 150, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num2.setFont(font)
        self.pb_St2_Num2.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num0)
        self.pb_St2_Num2.setObjectName("pb_St2_Num2")

        self.pb_St2_Num1 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num1.setEnabled(True)
        self.pb_St2_Num1.setGeometry(QtCore.QRect(300, 150, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num1.setFont(font)
        self.pb_St2_Num1.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num1)
        self.pb_St2_Num1.setObjectName("pb_St2_Num1")

        self.pb_St2_Num9 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num9.setEnabled(True)
        self.pb_St2_Num9.setGeometry(QtCore.QRect(420, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num9.setFont(font)
        self.pb_St2_Num9.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num2)
        self.pb_St2_Num9.setObjectName("pb_St2_Num9")

        self.pb_St2_Num3 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num3.setEnabled(True)
        self.pb_St2_Num3.setGeometry(QtCore.QRect(420, 150, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num3.setFont(font)
        self.pb_St2_Num3.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num3)
        self.pb_St2_Num3.setObjectName("pb_St2_Num3")

        self.pb_St2_Num6 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num6.setEnabled(True)
        self.pb_St2_Num6.setGeometry(QtCore.QRect(420, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num6.setFont(font)
        self.pb_St2_Num6.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num4)
        self.pb_St2_Num6.setObjectName("pb_St2_Num6")

        self.pb_St2_Num4 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num4.setEnabled(True)
        self.pb_St2_Num4.setGeometry(QtCore.QRect(300, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num4.setFont(font)
        self.pb_St2_Num4.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num5)
        self.pb_St2_Num4.setObjectName("pb_St2_Num4")

        self.pb_St2_Num5 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num5.setEnabled(True)
        self.pb_St2_Num5.setGeometry(QtCore.QRect(360, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num5.setFont(font)
        self.pb_St2_Num5.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num6)
        self.pb_St2_Num5.setObjectName("pb_St2_Num5")

        self.pb_St2_Num8 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num8.setEnabled(True)
        self.pb_St2_Num8.setGeometry(QtCore.QRect(360, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num8.setFont(font)
        self.pb_St2_Num8.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num7)
        self.pb_St2_Num8.setObjectName("pb_St2_Num8")

        self.pb_St2_Num7 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num7.setEnabled(True)
        self.pb_St2_Num7.setGeometry(QtCore.QRect(300, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num7.setFont(font)
        self.pb_St2_Num7.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num8)
        self.pb_St2_Num7.setObjectName("pb_St2_Num7")

        self.pb_St2_Num0 = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Num0.setEnabled(True)
        self.pb_St2_Num0.setGeometry(QtCore.QRect(360, 330, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St2_Num0.setFont(font)
        self.pb_St2_Num0.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Num9)
        self.pb_St2_Num0.setObjectName("pb_St2_Num0")

        self.lbl_St4_TimeRemaining = QtWidgets.QLabel(Dialog)
        self.lbl_St4_TimeRemaining.setEnabled(True)
        self.lbl_St4_TimeRemaining.setGeometry(QtCore.QRect(0, 60, 800, 32))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_LABEL_COMMON_FONT_FAMILY)
        font.setPointSize(15)
        self.lbl_St4_TimeRemaining.setFont(font)
        self.lbl_St4_TimeRemaining.setStyleSheet(DEFAULT_STYLE_SHEET_lbl_St4_TimeRemaining)
        self.lbl_St4_TimeRemaining.setLineWidth(1)
        self.lbl_St4_TimeRemaining.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_St4_TimeRemaining.setOpenExternalLinks(False)
        self.lbl_St4_TimeRemaining.setObjectName("lbl_St4_TimeRemaining")

        self.lbl_St1_DisplayPrinterNumber = QtWidgets.QLabel(Dialog)
        self.lbl_St1_DisplayPrinterNumber.setEnabled(True)
        self.lbl_St1_DisplayPrinterNumber.setGeometry(QtCore.QRect(0, 25, 800, 32))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_LABEL_COMMON_FONT_FAMILY)
        font.setPointSize(15)
        self.lbl_St1_DisplayPrinterNumber.setFont(font)
        self.lbl_St1_DisplayPrinterNumber.setStyleSheet(DEFAULT_STYLE_SHEET_lbl_St1_DisplayPrinterNumber)
        self.lbl_St1_DisplayPrinterNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_St1_DisplayPrinterNumber.setOpenExternalLinks(False)
        self.lbl_St1_DisplayPrinterNumber.setObjectName("lbl_St1_DisplayPrinterNumber")

        self.pb_St1_StartPrint = QtWidgets.QPushButton(Dialog)
        self.pb_St1_StartPrint.setEnabled(True)
        self.pb_St1_StartPrint.setGeometry(QtCore.QRect(200, 130, 360, 220))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_St1_StartPrint.sizePolicy().hasHeightForWidth())
        self.pb_St1_StartPrint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        font.setItalic(True)
        font.setUnderline(True)
        self.pb_St1_StartPrint.setFont(font)
        self.pb_St1_StartPrint.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St1_StartPrint)
        self.pb_St1_StartPrint.setAutoFillBackground(False)
        self.pb_St1_StartPrint.setObjectName("pb_St1_StartPrint")

        self.pb_St4_CancelPrint = QtWidgets.QPushButton(Dialog)
        self.pb_St4_CancelPrint.setEnabled(True)
        self.pb_St4_CancelPrint.setGeometry(QtCore.QRect(200, 130, 360, 220))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_St4_CancelPrint.sizePolicy().hasHeightForWidth())
        self.pb_St4_CancelPrint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        font.setItalic(True)
        font.setUnderline(True)
        self.pb_St4_CancelPrint.setFont(font)
        self.pb_St4_CancelPrint.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St4_CancelPrint)
        self.pb_St4_CancelPrint.setAutoFillBackground(False)
        self.pb_St4_CancelPrint.setObjectName("pb_St4_CancelPrint")

        self.lbl_St5_StudentOrPersonnelID = QtWidgets.QLabel(Dialog)
        self.lbl_St5_StudentOrPersonnelID.setEnabled(True)
        self.lbl_St5_StudentOrPersonnelID.setGeometry(QtCore.QRect(0, 100, 800, 32))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_LABEL_COMMON_FONT_FAMILY)
        font.setPointSize(15)
        self.lbl_St5_StudentOrPersonnelID.setFont(font)
        self.lbl_St5_StudentOrPersonnelID.setStyleSheet(DEFAULT_STYLE_SHEET_lbl_St5_StudentOrPersonnelID)
        self.lbl_St5_StudentOrPersonnelID.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_St5_StudentOrPersonnelID.setOpenExternalLinks(False)
        self.lbl_St5_StudentOrPersonnelID.setObjectName("lbl_St5_StudentOrPersonnelID")

        self.pb_St2_BackSpace = QtWidgets.QPushButton(Dialog)
        self.pb_St2_BackSpace.setEnabled(True)
        self.pb_St2_BackSpace.setGeometry(QtCore.QRect(520, 150, 71, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pb_St2_BackSpace.setFont(font)
        self.pb_St2_BackSpace.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_BackSpace)
        self.pb_St2_BackSpace.setObjectName("pb_St2_BackSpace")

        self.pb_St2_Enter = QtWidgets.QPushButton(Dialog)
        self.pb_St2_Enter.setEnabled(True)
        self.pb_St2_Enter.setGeometry(QtCore.QRect(480, 330, 111, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pb_St2_Enter.setFont(font)
        self.pb_St2_Enter.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St2_Enter)
        self.pb_St2_Enter.setObjectName("pb_St2_Enter")

        self.pb_St5_Enter = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Enter.setEnabled(True)
        self.pb_St5_Enter.setGeometry(QtCore.QRect(480, 330, 111, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pb_St5_Enter.setFont(font)
        self.pb_St5_Enter.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Enter)
        self.pb_St5_Enter.setObjectName("pb_St5_Enter")

        self.pb_St5_Num8 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num8.setEnabled(True)
        self.pb_St5_Num8.setGeometry(QtCore.QRect(360, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num8.setFont(font)
        self.pb_St5_Num8.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num0)
        self.pb_St5_Num8.setObjectName("pb_St5_Num8")

        self.pb_St5_BackSpace = QtWidgets.QPushButton(Dialog)
        self.pb_St5_BackSpace.setEnabled(True)
        self.pb_St5_BackSpace.setGeometry(QtCore.QRect(520, 150, 71, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pb_St5_BackSpace.setFont(font)
        self.pb_St5_BackSpace.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_BackSpace)
        self.pb_St5_BackSpace.setObjectName("pb_St5_BackSpace")

        self.pb_St5_Num6 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num6.setEnabled(True)
        self.pb_St5_Num6.setGeometry(QtCore.QRect(420, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num6.setFont(font)
        self.pb_St5_Num6.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num1)
        self.pb_St5_Num6.setObjectName("pb_St5_Num6")

        self.pb_St5_Num3 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num3.setEnabled(True)
        self.pb_St5_Num3.setGeometry(QtCore.QRect(420, 150, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num3.setFont(font)
        self.pb_St5_Num3.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num2)
        self.pb_St5_Num3.setObjectName("pb_St5_Num3")

        self.pb_St5_Num7 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num7.setEnabled(True)
        self.pb_St5_Num7.setGeometry(QtCore.QRect(300, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num7.setFont(font)
        self.pb_St5_Num7.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num3)
        self.pb_St5_Num7.setObjectName("pb_St5_Num7")

        self.pb_St5_Num0 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num0.setEnabled(True)
        self.pb_St5_Num0.setGeometry(QtCore.QRect(360, 330, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num0.setFont(font)
        self.pb_St5_Num0.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num4)
        self.pb_St5_Num0.setObjectName("pb_St5_Num0")

        self.pb_St5_Num2 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num2.setEnabled(True)
        self.pb_St5_Num2.setGeometry(QtCore.QRect(360, 150, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num2.setFont(font)
        self.pb_St5_Num2.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num5)
        self.pb_St5_Num2.setObjectName("pb_St5_Num2")

        self.pb_St5_Num9 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num9.setEnabled(True)
        self.pb_St5_Num9.setGeometry(QtCore.QRect(420, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num9.setFont(font)
        self.pb_St5_Num9.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num6)
        self.pb_St5_Num9.setObjectName("pb_St5_Num9")

        self.pb_St5_Num1 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num1.setEnabled(True)
        self.pb_St5_Num1.setGeometry(QtCore.QRect(300, 150, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num1.setFont(font)
        self.pb_St5_Num1.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num7)
        self.pb_St5_Num1.setObjectName("pb_St5_Num1")

        self.pb_St5_Num5 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num5.setEnabled(True)
        self.pb_St5_Num5.setGeometry(QtCore.QRect(360, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num5.setFont(font)
        self.pb_St5_Num5.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num8)
        self.pb_St5_Num5.setObjectName("pb_St5_Num5")

        self.pb_St5_Num4 = QtWidgets.QPushButton(Dialog)
        self.pb_St5_Num4.setEnabled(True)
        self.pb_St5_Num4.setGeometry(QtCore.QRect(300, 210, 40, 40))
        font = QtGui.QFont()
        font.setFamily(DEFAULT_PUSHBUTTON_COMMON_FONT_FAMILY)
        font.setPointSize(12)
        self.pb_St5_Num4.setFont(font)
        self.pb_St5_Num4.setStyleSheet(DEFAULT_STYLE_SHEET_pb_St5_Num9)
        self.pb_St5_Num4.setObjectName("pb_St5_Num4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self._setStageWidgets()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(DEFAULT_DIALOG_OBJECT_NAME, "Main"))
        self.lbl_St2_StudentIDDisplay.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_lbl_St2_StudentIDDisplay))
        self.pb_St2_Num2.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num2))
        self.pb_St2_Num1.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num1))
        self.pb_St2_Num9.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num9))
        self.pb_St2_Num3.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num3))
        self.pb_St2_Num6.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num6))
        self.pb_St2_Num4.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num4))
        self.pb_St2_Num5.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num5))
        self.pb_St2_Num8.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num8))
        self.pb_St2_Num7.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num7))
        self.pb_St2_Num0.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Num0))
        self.lbl_St4_TimeRemaining.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_lbl_St4_TimeRemaining))
        self.lbl_St1_DisplayPrinterNumber.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_lbl_St1_DisplayPrinterNumber))
        self.pb_St1_StartPrint.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St1_StartPrint))
        self.pb_St4_CancelPrint.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St4_CancelPrint))
        self.lbl_St5_StudentOrPersonnelID.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_lbl_St5_StudentOrPersonnelID))
        self.pb_St2_BackSpace.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_BackSpace))
        self.pb_St2_Enter.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St2_Enter))
        self.pb_St5_Enter.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Enter))
        self.pb_St5_Num8.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num8))
        self.pb_St5_BackSpace.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_BackSpace))
        self.pb_St5_Num6.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num6))
        self.pb_St5_Num3.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num3))
        self.pb_St5_Num7.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num7))
        self.pb_St5_Num0.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num0))
        self.pb_St5_Num2.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num2))
        self.pb_St5_Num9.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num9))
        self.pb_St5_Num1.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num1))
        self.pb_St5_Num5.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num5))
        self.pb_St5_Num4.setText(_translate(DEFAULT_DIALOG_OBJECT_NAME, DEFAULT_TEXT_pb_St5_Num4))

    def _setStageWidgets(self):
        self.stage1Widgets = [
            self.pb_St1_StartPrint,
            self.lbl_St1_DisplayPrinterNumber
        ]

        self.stage2Widgets = [
            self.pb_St2_Num0,
            self.pb_St2_Num1,
            self.pb_St2_Num2,
            self.pb_St2_Num3,
            self.pb_St2_Num4,
            self.pb_St2_Num5,
            self.pb_St2_Num6,
            self.pb_St2_Num7,
            self.pb_St2_Num8,
            self.pb_St2_Num9,
            self.pb_St2_BackSpace,
            self.pb_St2_Enter,
            self.lbl_St2_StudentIDDisplay
        ]

        self.stage3Widgets = []

        self.stage4Widgets = [
            self.pb_St4_CancelPrint,
            self.lbl_St4_TimeRemaining
        ]

        self.stage5Widgets = [
            self.pb_St5_Num0,
            self.pb_St5_Num1,
            self.pb_St5_Num2,
            self.pb_St5_Num3,
            self.pb_St5_Num4,
            self.pb_St5_Num5,
            self.pb_St5_Num6,
            self.pb_St5_Num7,
            self.pb_St5_Num8,
            self.pb_St5_Num9,
            self.pb_St5_BackSpace,
            self.pb_St5_Enter,
            self.lbl_St5_StudentOrPersonnelID
        ]

        self.stage6Widgets = []

    @property
    def stages(self):
        try:
            return (self.stage1Widgets, self.stage2Widgets, self.stage3Widgets, self.stage4Widgets, self.stage5Widgets, self.stage6Widgets)
        except AttributeError:
            self._setStageWidgets()
            return (self.stage1Widgets, self.stage2Widgets, self.stage3Widgets, self.stage4Widgets, self.stage5Widgets, self.stage6Widgets)

def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui = PrinterUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
