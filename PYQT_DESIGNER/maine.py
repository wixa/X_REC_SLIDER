# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Fri Nov 21 13:57:21 2014
# by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, uic
import sys
import time
import serial
import math
import untitled_ui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyWindowClass(QtGui.QMainWindow, untitled_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindowClass,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.setEnabled(False)
app = QtGui.QApplication(sys.argv)
window = MyWindowClass()
window.show()
sys.exit(app.exec_())