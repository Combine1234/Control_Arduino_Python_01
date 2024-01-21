from PyQt5 import QtCore, QtGui, QtWidgets

import Controller as con

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        con.Cpin13_off()
        con.Cpin12_off()
        con.Cpin11_off()
        con.Cpin10_off()
        con.Cpin9_off()
        con.Cpin8_off()
        con.Cpin7_off()
        con.Cpin6_off()
        con.Cpin5_off()
        con.Cpin4_off()
        con.Cpin3_off()
        con.Cpin2_off()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 185)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Adpin13 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin13.setGeometry(QtCore.QRect(80, 10, 41, 41))
        self.Adpin13.setObjectName("Adpin13")
        self.Adpin13.setCheckable(True)
        self.Adpin13.clicked.connect(self.Pin13_clicked)

        self.Adpin12 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin12.setGeometry(QtCore.QRect(130, 10, 41, 41))
        self.Adpin12.setObjectName("Adpin12")
        self.Adpin12.setCheckable(True)
        self.Adpin12.clicked.connect(self.Pin12_clicked)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.Stpin13 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin13.setGeometry(QtCore.QRect(90, 60, 21, 16))
        self.Stpin13.setObjectName("Stpin13")
    
        self.Stpin12 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin12.setGeometry(QtCore.QRect(140, 60, 21, 16))
        self.Stpin12.setObjectName("Stpin12")

        self.Adpin11 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin11.setGeometry(QtCore.QRect(180, 10, 41, 41))
        self.Adpin11.setObjectName("Adpin11")
        self.Adpin11.setCheckable(True)
        self.Adpin11.clicked.connect(self.Pin11_clicked)

        self.Adpin10 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin10.setGeometry(QtCore.QRect(230, 10, 41, 41))
        self.Adpin10.setObjectName("Adpin10")
        self.Adpin10.setCheckable(True)
        self.Adpin10.clicked.connect(self.Pin10_clicked)

        self.Adpin8 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin8.setGeometry(QtCore.QRect(330, 10, 41, 41))
        self.Adpin8.setObjectName("Adpin8")
        self.Adpin8.setCheckable(True)
        self.Adpin8.clicked.connect(self.Pin8_clicked)

        self.Adpin9 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin9.setGeometry(QtCore.QRect(280, 10, 41, 41))
        self.Adpin9.setObjectName("Adpin9")
        self.Adpin9.setCheckable(True)
        self.Adpin9.clicked.connect(self.Pin9_clicked)

        self.Stpin11 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin11.setGeometry(QtCore.QRect(190, 60, 21, 16))
        self.Stpin11.setObjectName("Stpin11")

        self.Stpin10 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin10.setGeometry(QtCore.QRect(240, 60, 21, 16))
        self.Stpin10.setObjectName("Stpin10")

        self.Stpin9 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin9.setGeometry(QtCore.QRect(290, 60, 21, 16))
        self.Stpin9.setObjectName("Stpin9")

        self.Stpin8 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin8.setGeometry(QtCore.QRect(340, 60, 21, 16))
        self.Stpin8.setObjectName("Stpin8")

        self.Adpin7 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin7.setGeometry(QtCore.QRect(420, 10, 41, 41))
        self.Adpin7.setObjectName("Adpin7")
        self.Adpin7.setCheckable(True)
        self.Adpin7.clicked.connect(self.Pin7_clicked)

        self.Stpin7 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin7.setGeometry(QtCore.QRect(430, 60, 21, 16))
        self.Stpin7.setObjectName("Stpin7")

        self.Adpin6 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin6.setGeometry(QtCore.QRect(470, 10, 41, 41))
        self.Adpin6.setObjectName("Adpin6")
        self.Adpin6.setCheckable(True)
        self.Adpin6.clicked.connect(self.Pin6_clicked)

        self.Stpin6 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin6.setGeometry(QtCore.QRect(480, 60, 21, 16))
        self.Stpin6.setObjectName("Stpin6")

        self.Adpin5 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin5.setGeometry(QtCore.QRect(520, 10, 41, 41))
        self.Adpin5.setObjectName("Adpin5")
        self.Adpin5.setCheckable(True)
        self.Adpin5.clicked.connect(self.Pin5_clicked)

        self.Adpin4 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin4.setGeometry(QtCore.QRect(570, 10, 41, 41))
        self.Adpin4.setObjectName("Adpin4")
        self.Adpin4.setCheckable(True)
        self.Adpin4.clicked.connect(self.Pin4_clicked)

        self.Adpin3 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin3.setGeometry(QtCore.QRect(620, 10, 41, 41))
        self.Adpin3.setObjectName("Adpin3")
        self.Adpin3.setCheckable(True)
        self.Adpin3.clicked.connect(self.Pin3_clicked)

        self.Adpin2 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin2.setGeometry(QtCore.QRect(670, 10, 41, 41))
        self.Adpin2.setObjectName("Adpin2")
        self.Adpin2.setCheckable(True)
        self.Adpin2.clicked.connect(self.Pin2_clicked)

        self.Adpin0 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin0.setGeometry(QtCore.QRect(770, 10, 41, 41))
        self.Adpin0.setObjectName("Adpin0")
        self.Adpin0.setCheckable(True)

        self.Adpin1 = QtWidgets.QPushButton(self.centralwidget)
        self.Adpin1.setGeometry(QtCore.QRect(720, 10, 41, 41))
        self.Adpin1.setObjectName("Adpin1")
        self.Adpin1.setCheckable(True)

        self.Stpin5 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin5.setGeometry(QtCore.QRect(530, 60, 21, 16))
        self.Stpin5.setObjectName("Stpin5")

        self.Stpin4 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin4.setGeometry(QtCore.QRect(580, 60, 21, 16))
        self.Stpin4.setObjectName("Stpin4")

        self.Stpin3 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin3.setGeometry(QtCore.QRect(630, 60, 21, 16))
        self.Stpin3.setObjectName("Stpin3")

        self.Stpin2 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin2.setGeometry(QtCore.QRect(680, 60, 21, 16))
        self.Stpin2.setObjectName("Stpin2")

        self.Stpin1 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin1.setGeometry(QtCore.QRect(730, 60, 21, 16))
        self.Stpin1.setObjectName("Stpin1")

        self.Stpin0 = QtWidgets.QLabel(self.centralwidget)
        self.Stpin0.setGeometry(QtCore.QRect(780, 60, 21, 16))
        self.Stpin0.setObjectName("Stpin0")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Pin13_clicked(self):
        if self.Adpin13.isChecked():
            self.Stpin13.setText("on")
            con.Cpin13_on()
        else:
            self.Stpin13.setText("off")
            con.Cpin13_off()

    def Pin12_clicked(self):
        if self.Adpin12.isChecked():
            self.Stpin12.setText("on")
            con.Cpin12_on()
        else:
            self.Stpin12.setText("off")
            con.Cpin12_off()

    def Pin11_clicked(self):
        if self.Adpin11.isChecked():
            self.Stpin11.setText("on")
            con.Cpin11_on()
        else:
            self.Stpin11.setText("off")
            con.Cpin11_off()
    
    def Pin10_clicked(self):
        if self.Adpin10.isChecked():
            self.Stpin10.setText("on")
            con.Cpin10_on()
        else:
            self.Stpin10.setText("off")
            con.Cpin10_off()

    def Pin9_clicked(self):
        if self.Adpin9.isChecked():
            self.Stpin9.setText("on")
            con.Cpin9_on()
        else:
            self.Stpin9.setText("off")
            con.Cpin9_off()
    
    def Pin8_clicked(self):
        if self.Adpin8.isChecked():
            self.Stpin8.setText("on")
            con.Cpin8_on()
        else:
            self.Stpin8.setText("off")
            con.Cpin8_off()
    
    def Pin7_clicked(self):
        if self.Adpin7.isChecked():
            self.Stpin7.setText("on")
            con.Cpin7_on()
        else:
            self.Stpin7.setText("off")
            con.Cpin7_off()
    
    def Pin6_clicked(self):
        if self.Adpin6.isChecked():
            self.Stpin6.setText("on")
            con.Cpin6_on()
        else:
            self.Stpin6.setText("off")
            con.Cpin6_off()
    
    def Pin5_clicked(self):
        if self.Adpin5.isChecked():
            self.Stpin5.setText("on")
            con.Cpin5_on()
        else:
            self.Stpin5.setText("off")
            con.Cpin5_off()
    
    def Pin4_clicked(self):
        if self.Adpin4.isChecked():
            self.Stpin4.setText("on")
            con.Cpin4_on()
        else:
            self.Stpin4.setText("off")
            con.Cpin4_off()

    def Pin3_clicked(self):
        if self.Adpin3.isChecked():
            self.Stpin3.setText("on")
            con.Cpin3_on()
        else:
            self.Stpin3.setText("off")
            con.Cpin3_off()

    def Pin2_clicked(self):
        if self.Adpin2.isChecked():
            self.Stpin2.setText("on")
            con.Cpin2_on()
        else:
            self.Stpin2.setText("off")
            con.Cpin2_off()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Adpin13.setText(_translate("MainWindow", "13"))
        self.Adpin12.setText(_translate("MainWindow", "12"))
        self.label.setText(_translate("MainWindow", "Status :"))
        self.Stpin13.setText(_translate("MainWindow", "off"))
        self.Stpin12.setText(_translate("MainWindow", "off"))
        self.Adpin11.setText(_translate("MainWindow", "11"))
        self.Adpin10.setText(_translate("MainWindow", "10"))
        self.Adpin8.setText(_translate("MainWindow", "8"))
        self.Adpin9.setText(_translate("MainWindow", "9"))
        self.Stpin11.setText(_translate("MainWindow", "off"))
        self.Stpin10.setText(_translate("MainWindow", "off"))
        self.Stpin9.setText(_translate("MainWindow", "off"))
        self.Stpin8.setText(_translate("MainWindow", "off"))
        self.Adpin7.setText(_translate("MainWindow", "7"))
        self.Stpin7.setText(_translate("MainWindow", "off"))
        self.Adpin6.setText(_translate("MainWindow", "6"))
        self.Stpin6.setText(_translate("MainWindow", "off"))
        self.Adpin5.setText(_translate("MainWindow", "5"))
        self.Adpin4.setText(_translate("MainWindow", "4"))
        self.Adpin3.setText(_translate("MainWindow", "3"))
        self.Adpin2.setText(_translate("MainWindow", "2"))
        self.Adpin0.setText(_translate("MainWindow", "0"))
        self.Adpin1.setText(_translate("MainWindow", "1"))
        self.Stpin5.setText(_translate("MainWindow", "off"))
        self.Stpin4.setText(_translate("MainWindow", "off"))
        self.Stpin3.setText(_translate("MainWindow", "off"))
        self.Stpin2.setText(_translate("MainWindow", "off"))
        self.Stpin1.setText(_translate("MainWindow", "off"))
        self.Stpin0.setText(_translate("MainWindow", "off"))

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Connect the function to the button click using the class instance
    ui.Adpin11.clicked.connect(ui.Pin11_clicked)

    MainWindow.show()
    sys.exit(app.exec_())
