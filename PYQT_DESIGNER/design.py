# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_window.ui'
#
# Created: Sun Nov 30 12:50:56 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(480, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setSizeIncrement(QtCore.QSize(960, 640))
        MainWindow.setBaseSize(QtCore.QSize(960, 640))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/icons/Logo_last_24x24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 960))
        self.centralwidget.setSizeIncrement(QtCore.QSize(480, 320))
        self.centralwidget.setBaseSize(QtCore.QSize(480, 320))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.radioButton_9 = QtGui.QRadioButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_9.sizePolicy().hasHeightForWidth())
        self.radioButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_9.setWhatsThis(_fromUtf8(""))
        self.radioButton_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_9.setAutoFillBackground(False)
        self.radioButton_9.setInputMethodHints(QtCore.Qt.ImhNone)
        self.radioButton_9.setIconSize(QtCore.QSize(24, 24))
        self.radioButton_9.setChecked(False)
        self.radioButton_9.setAutoExclusive(False)
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.horizontalLayout_10.addWidget(self.radioButton_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 1, 2, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.radioButton_10 = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setChecked(False)
        self.radioButton_10.setAutoExclusive(False)
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.horizontalLayout_9.addWidget(self.radioButton_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 2, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.START_BUTTON = QtGui.QPushButton(self.centralwidget)
        self.START_BUTTON.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.START_BUTTON.sizePolicy().hasHeightForWidth())
        self.START_BUTTON.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.START_BUTTON.setFont(font)
        self.START_BUTTON.setCheckable(True)
        self.START_BUTTON.setChecked(False)
        self.START_BUTTON.setDefault(False)
        self.START_BUTTON.setFlat(False)
        self.START_BUTTON.setObjectName(_fromUtf8("START_BUTTON"))
        self.horizontalLayout_6.addWidget(self.START_BUTTON)
        self.STOP_BUTTON = QtGui.QPushButton(self.centralwidget)
        self.STOP_BUTTON.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.STOP_BUTTON.sizePolicy().hasHeightForWidth())
        self.STOP_BUTTON.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.STOP_BUTTON.setFont(font)
        self.STOP_BUTTON.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.STOP_BUTTON.setCheckable(True)
        self.STOP_BUTTON.setChecked(False)
        self.STOP_BUTTON.setAutoRepeat(False)
        self.STOP_BUTTON.setAutoExclusive(False)
        self.STOP_BUTTON.setAutoDefault(False)
        self.STOP_BUTTON.setDefault(False)
        self.STOP_BUTTON.setFlat(False)
        self.STOP_BUTTON.setObjectName(_fromUtf8("STOP_BUTTON"))
        self.horizontalLayout_6.addWidget(self.STOP_BUTTON)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 8, 0, 1, 3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalSlider_3 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_3.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy)
        self.horizontalSlider_3.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_3.setMaximum(23)
        self.horizontalSlider_3.setPageStep(1)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.verticalLayout_3.addWidget(self.horizontalSlider_3)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 7, 0, 1, 3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lcdNumber_3 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lcdNumber_3.sizePolicy().hasHeightForWidth())
        self.lcdNumber_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_3.setFont(font)
        self.lcdNumber_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lcdNumber_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_3.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_3.setNumDigits(4)
        self.lcdNumber_3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.horizontalLayout_5.addWidget(self.lcdNumber_3)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 6, 0, 1, 3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalSlider_2 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_2.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_2.setMaximum(60)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.verticalLayout_2.addWidget(self.horizontalSlider_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 5, 0, 1, 3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lcdNumber_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lcdNumber_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_2.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_2.setNumDigits(4)
        self.lcdNumber_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.horizontalLayout_4.addWidget(self.lcdNumber_2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.gridLayout_2.addLayout(self.verticalLayout, 3, 0, 1, 3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.INIT = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INIT.sizePolicy().hasHeightForWidth())
        self.INIT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.INIT.setFont(font)
        self.INIT.setCheckable(False)
        self.INIT.setObjectName(_fromUtf8("INIT"))
        self.verticalLayout_5.addWidget(self.INIT)
        self.CHANGE_INIT = QtGui.QPushButton(self.centralwidget)
        self.CHANGE_INIT.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHANGE_INIT.sizePolicy().hasHeightForWidth())
        self.CHANGE_INIT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CHANGE_INIT.setFont(font)
        self.CHANGE_INIT.setCheckable(True)
        self.CHANGE_INIT.setObjectName(_fromUtf8("CHANGE_INIT"))
        self.verticalLayout_5.addWidget(self.CHANGE_INIT)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 1, 2, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_3.setIconSize(QtCore.QSize(24, 24))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lcdNumber.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setNumDigits(4)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.WIDTH_OBJECT = QtGui.QLabel(self.centralwidget)
        self.WIDTH_OBJECT.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WIDTH_OBJECT.sizePolicy().hasHeightForWidth())
        self.WIDTH_OBJECT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.WIDTH_OBJECT.setFont(font)
        self.WIDTH_OBJECT.setObjectName(_fromUtf8("WIDTH_OBJECT"))
        self.horizontalLayout_2.addWidget(self.WIDTH_OBJECT)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusBar.setFont(font)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_2.display)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_3.display)
        QtCore.QObject.connect(self.START_BUTTON, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.START_BUTTON.hide)
        QtCore.QObject.connect(self.STOP_BUTTON, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.START_BUTTON.show)
        QtCore.QObject.connect(self.STOP_BUTTON, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.STOP_BUTTON.hide)
        QtCore.QObject.connect(self.START_BUTTON, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.STOP_BUTTON.show)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lcdNumber.setDisabled)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.horizontalSlider.setDisabled)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButton_9.toggle)
        QtCore.QObject.connect(self.radioButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButton_3.toggle)
        QtCore.QObject.connect(self.radioButton_10, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.radioButton_2.toggle)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButton_10.toggle)
        QtCore.QObject.connect(self.radioButton_10, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lcdNumber.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "X-REC SLIDER", None))
        self.radioButton_9.setToolTip(_translate("MainWindow", "Каретка будет ехать \n"
"с права на лево", None))
        self.radioButton_9.setText(_translate("MainWindow", "<<<---------------------------------", None))
        self.radioButton_10.setToolTip(_translate("MainWindow", "Каретка будет ехать \n"
"заданное время и смотреть \n"
"на обьект  на заданном растоянии", None))
        self.radioButton_10.setText(_translate("MainWindow", "Езда со слежением", None))
        self.START_BUTTON.setText(_translate("MainWindow", "СТАРТ", None))
        self.STOP_BUTTON.setText(_translate("MainWindow", "СТОП", None))
        self.label_3.setText(_translate("MainWindow", "Время (часы)", None))
        self.label_2.setText(_translate("MainWindow", "Время (мин)", None))
        self.INIT.setText(_translate("MainWindow", "Перевезти каретку \n"
"на исходную \n"
"позицию", None))
        self.CHANGE_INIT.setText(_translate("MainWindow", "Изменить \n"
"начальные \n"
"настройки", None))
        self.radioButton_3.setToolTip(_translate("MainWindow", "Каретка будет ехать с лева на право", None))
        self.radioButton_3.setText(_translate("MainWindow", "-------------------------------------->>>", None))
        self.WIDTH_OBJECT.setText(_translate("MainWindow", "Расстояние до обьекта (м)", None))
        self.radioButton_2.setToolTip(_translate("MainWindow", "Каретка будет ехать задданое вами время", None))
        self.radioButton_2.setText(_translate("MainWindow", "                                                Езда", None))

import 1_rc
