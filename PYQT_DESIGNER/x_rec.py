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
import main_window_ui

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
length = 1300.0  # length of slider
way = float((length / 2) * 200)
rotate = 0
acceleration = 722
change = 0

class MyWindowClass(QtGui.QMainWindow, main_window_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindowClass,self).__init__(parent)
        self.setupUi(self)
        self.showFullScreen()
        self.ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
        self.ser.open()
        self.timer = QtCore.QTimer()
        self.CHANGE_INIT.hide()
        self.STOP_BUTTON.hide()
        self.START_BUTTON.setDisabled(1)
        self.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.distance)
        self.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.lcdNumber_2.display)
        self.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.lcdNumber_3.display)
        self.connect(self.START_BUTTON, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.START_RUN)
        self.connect(self.STOP_BUTTON, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.STOP_RUN)
        self.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")),
                               self.lcdNumber.setDisabled)
        self.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")),
                               self.horizontalSlider.setDisabled)
        self.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButton_9.toggle)
        self.connect(self.radioButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButton_3.toggle)
        self.connect(self.radioButton_10, QtCore.SIGNAL(_fromUtf8("clicked(bool)")),
                               self.radioButton_2.toggle)
        self.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButton_10.toggle)
        self.connect(self.INIT, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.INIT_FINISH)
        self.connect(self.CHANGE_INIT, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.INIT_CHANGE)
        self.connect(self.timer, QtCore.SIGNAL(_fromUtf8("timeout()")), self.PRINT_TIME)

        self.statusbar.showMessage(u'Выберите режим и направление езды затем нажмите "Перевезти каретку ..."', 0)

    def distance(self, hsv):
        dcmetr = float(hsv / 10.0)
        self.lcdNumber.display(dcmetr)

    def INIT_FINISH(self):
        self.INIT.hide()
        self.START_BUTTON.setEnabled(1)
        self.CHANGE_INIT.show()
        self.radioButton_2.setDisabled(1)
        self.radioButton_3.setDisabled(1)
        self.radioButton_9.setDisabled(1)
        self.radioButton_10.setDisabled(1)
        if self.radioButton_10.isChecked():
            self.lcdNumber.setEnabled(1)
            self.horizontalSlider.setEnabled(1)
            self.lcdNumber.display(1.0)
            self.horizontalSlider.setValue(1)
            self.statusbar.showMessage(u'Задайте время езды и растояние до объекта, затем нажмите "СТАРТ" ', 0)
        if self.radioButton_2.isChecked():
            self.lcdNumber.display(0)
            self.horizontalSlider.setValue(0)
            self.statusbar.showMessage(u'Задайте время езды, затем нажмите "СТАРТ" ', 0)
        self.lcdNumber_2.setEnabled(1)
        self.horizontalSlider_2.setEnabled(1)
        self.lcdNumber_2.display(1)
        self.horizontalSlider_2.setValue(1)
        self.lcdNumber_3.setEnabled(1)
        self.horizontalSlider_3.setEnabled(1)
        self.horizontalSlider_3.setValue(0)
        if self.radioButton_3.isChecked():
            self.direct = 1
        else:
            self.direct = 0
        self.ser.write('d'+self.direct+'d')
        global change
        change=0


    def INIT_CHANGE(self):
        self.CHANGE_INIT.hide()
        self.START_BUTTON.setDisabled(1)
        self.INIT.show()
        self.radioButton_2.setEnabled(1)
        self.radioButton_3.setEnabled(1)
        self.radioButton_9.setEnabled(1)
        self.radioButton_10.setEnabled(1)
        self.lcdNumber.setDisabled(1)
        self.horizontalSlider.setDisabled(1)
        self.lcdNumber_2.setDisabled(1)
        self.horizontalSlider_2.setDisabled(1)
        self.lcdNumber_3.setDisabled(1)
        self.horizontalSlider_3.setDisabled(1)
        global change
        change=1
        self.ser.write('c'+str(change)+'c')


    def START_RUN(self):
        self.START_BUTTON.hide()
        self.STOP_BUTTON.show()
        self.radioButton_2.setDisabled(1)
        self.radioButton_3.setDisabled(1)
        self.radioButton_9.setDisabled(1)
        self.radioButton_10.setDisabled(1)
        self.CHANGE_INIT.setDisabled(1)
        self.lcdNumber.setDisabled(1)
        self.lcdNumber_2.setDisabled(1)
        self.lcdNumber_3.setDisabled(1)
        self.horizontalSlider.setDisabled(1)
        self.horizontalSlider_2.setDisabled(1)
        self.horizontalSlider_3.setDisabled(1)
        distance = self.lcdNumber.value() * 1000
        global length

        if self.radioButton_10.isChecked():
            global rotate
            x = (length / 2) / distance
            angel = ((math.atan(x) * 180) / math.pi) * 2
            rotate = int((angel * 6400) / 360)
        timerun = (self.lcdNumber_2.intValue() + (self.lcdNumber_3.intValue()) * 60) * 60
        if timerun >= 800:
            stepmode = 1
            global way
            way16 = way * 16
            speed = float(way16 / timerun)
        else:
            stepmode = 0
            speed = float(way / timerun)
        global acceleration
        timeaccel = float(speed / acceleration)
        statusbarstring = ('s' + str(int(speed)) + 's') + ('m'+(stepmode)+'m')+('a'+str(acceleration)+'a')+ ('r' + str(rotate) + 'r') + (
            't' + str(way) + 't')
        self.ser.write(statusbarstring)
        self.direct = ''
        self.stepmode = ''
        self.speed = 0
        self.timeaccel = 0
        rotate = 0
        self.timer.start(1000)
        self.timeleft = timerun


    def PRINT_TIME(self):
        self.timeleft = self.timeleft - 1
        if self.timeleft == 0:
            self.timer.stop()
            self.STOP_RUN()
        else:
            self.string = u'До окончания цикла осталось: '
            hms = time.strftime('%H:%M:%S', time.gmtime(self.timeleft))
            self.statusbar.showMessage(self.string + str(hms), 0)


    def STOP_RUN(self):
        self.CHANGE_INIT.setEnabled(1)
        self.timer.stop()
        self.START_BUTTON.show()
        self.START_BUTTON.setDisabled(1)
        self.STOP_BUTTON.hide()
        self.INIT.setEnabled(1)
        self.INIT.show()
        self.radioButton_2.setEnabled(1)
        self.radioButton_3.setEnabled(1)
        self.radioButton_9.setEnabled(1)
        self.radioButton_10.setEnabled(1)
        self.CHANGE_INIT.hide()
        self.statusbar.showMessage(u'Выберите режим и направление езды затем нажмите "Перевезти каретку ..."', 0)
        self.ser.write('t0t')

app = QtGui.QApplication(sys.argv)
window = MyWindowClass()
window.show()
sys.exit(app.exec_())