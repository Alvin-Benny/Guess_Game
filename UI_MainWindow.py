# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1000, 800)
        mainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        mainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.intro_screen = QtWidgets.QWidget()
        self.intro_screen.setObjectName("intro_screen")
        self.title_2 = QtWidgets.QLabel(self.intro_screen)
        self.title_2.setGeometry(QtCore.QRect(260, 50, 461, 91))
        font = QtGui.QFont()
        font.setFamily("STXinwei")
        font.setPointSize(36)
        self.title_2.setFont(font)
        self.title_2.setTextFormat(QtCore.Qt.RichText)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.info_lbl = QtWidgets.QLabel(self.intro_screen)
        self.info_lbl.setGeometry(QtCore.QRect(70, 130, 881, 501))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.info_lbl.setFont(font)
        self.info_lbl.setStyleSheet("color: rgb(255, 255, 127);")
        self.info_lbl.setWordWrap(True)
        self.info_lbl.setObjectName("info_lbl")
        self.one_player_btn = QtWidgets.QRadioButton(self.intro_screen)
        self.one_player_btn.setGeometry(QtCore.QRect(250, 590, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.one_player_btn.setFont(font)
        self.one_player_btn.setChecked(False)
        self.one_player_btn.setObjectName("one_player_btn")
        self.two_player_btn = QtWidgets.QRadioButton(self.intro_screen)
        self.two_player_btn.setGeometry(QtCore.QRect(590, 590, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.two_player_btn.setFont(font)
        self.two_player_btn.setChecked(True)
        self.two_player_btn.setObjectName("two_player_btn")
        self.intro_submit_btn = QtWidgets.QPushButton(self.intro_screen)
        self.intro_submit_btn.setGeometry(QtCore.QRect(730, 680, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.intro_submit_btn.setFont(font)
        self.intro_submit_btn.setAutoFillBackground(False)
        self.intro_submit_btn.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.intro_submit_btn.setDefault(False)
        self.intro_submit_btn.setFlat(False)
        self.intro_submit_btn.setObjectName("intro_submit_btn")
        self.stackedWidget.addWidget(self.intro_screen)
        self.input_screen = QtWidgets.QWidget()
        self.input_screen.setObjectName("input_screen")
        self.title = QtWidgets.QLabel(self.input_screen)
        self.title.setGeometry(QtCore.QRect(260, 50, 461, 91))
        font = QtGui.QFont()
        font.setFamily("STXinwei")
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.secret_word_lbl = QtWidgets.QLabel(self.input_screen)
        self.secret_word_lbl.setGeometry(QtCore.QRect(50, 630, 911, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.secret_word_lbl.setFont(font)
        self.secret_word_lbl.setWordWrap(True)
        self.secret_word_lbl.setObjectName("secret_word_lbl")
        self.word_submit_btn = QtWidgets.QPushButton(self.input_screen)
        self.word_submit_btn.setGeometry(QtCore.QRect(730, 680, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.word_submit_btn.setFont(font)
        self.word_submit_btn.setAutoFillBackground(False)
        self.word_submit_btn.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.word_submit_btn.setDefault(False)
        self.word_submit_btn.setFlat(False)
        self.word_submit_btn.setObjectName("word_submit_btn")
        self.input_error_lbl = QtWidgets.QLabel(self.input_screen)
        self.input_error_lbl.setGeometry(QtCore.QRect(50, 500, 911, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.input_error_lbl.setFont(font)
        self.input_error_lbl.setStyleSheet("color: rgb(255, 255, 127);")
        self.input_error_lbl.setText("")
        self.input_error_lbl.setWordWrap(True)
        self.input_error_lbl.setObjectName("input_error_lbl")
        self.label = QtWidgets.QLabel(self.input_screen)
        self.label.setGeometry(QtCore.QRect(140, 210, 691, 201))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.word_input = QtWidgets.QLineEdit(self.input_screen)
        self.word_input.setGeometry(QtCore.QRect(50, 670, 611, 87))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.word_input.setFont(font)
        self.word_input.setStyleSheet("border: 5px solid black;\n"
"color: white;")
        self.word_input.setText("")
        self.word_input.setObjectName("word_input")
        self.stackedWidget.addWidget(self.input_screen)
        self.guess_screen = QtWidgets.QWidget()
        self.guess_screen.setObjectName("guess_screen")
        self.guess_lbl = QtWidgets.QLabel(self.guess_screen)
        self.guess_lbl.setGeometry(QtCore.QRect(50, 630, 891, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.guess_lbl.setFont(font)
        self.guess_lbl.setWordWrap(True)
        self.guess_lbl.setObjectName("guess_lbl")
        self.title2 = QtWidgets.QLabel(self.guess_screen)
        self.title2.setGeometry(QtCore.QRect(260, 50, 461, 91))
        font = QtGui.QFont()
        font.setFamily("STXinwei")
        font.setPointSize(36)
        self.title2.setFont(font)
        self.title2.setTextFormat(QtCore.Qt.RichText)
        self.title2.setAlignment(QtCore.Qt.AlignCenter)
        self.title2.setWordWrap(False)
        self.title2.setObjectName("title2")
        self.label_3 = QtWidgets.QLabel(self.guess_screen)
        self.label_3.setGeometry(QtCore.QRect(680, 310, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.guess_screen)
        self.label_4.setGeometry(QtCore.QRect(60, 310, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.guess_count_lbl = QtWidgets.QLabel(self.guess_screen)
        self.guess_count_lbl.setGeometry(QtCore.QRect(750, 360, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.guess_count_lbl.setFont(font)
        self.guess_count_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.guess_count_lbl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.guess_count_lbl.setLineWidth(5)
        self.guess_count_lbl.setObjectName("guess_count_lbl")
        self.time_lbl = QtWidgets.QLabel(self.guess_screen)
        self.time_lbl.setGeometry(QtCore.QRect(60, 360, 201, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.time_lbl.setFont(font)
        self.time_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.time_lbl.setLineWidth(5)
        self.time_lbl.setObjectName("time_lbl")
        self.hint_lbl = QtWidgets.QLabel(self.guess_screen)
        self.hint_lbl.setGeometry(QtCore.QRect(210, 150, 586, 145))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.hint_lbl.setFont(font)
        self.hint_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hint_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.hint_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.hint_lbl.setObjectName("hint_lbl")
        self.guess_submit_btn = QtWidgets.QPushButton(self.guess_screen)
        self.guess_submit_btn.setGeometry(QtCore.QRect(740, 687, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.guess_submit_btn.setFont(font)
        self.guess_submit_btn.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.guess_submit_btn.setObjectName("guess_submit_btn")
        self.guess_error_lbl = QtWidgets.QLabel(self.guess_screen)
        self.guess_error_lbl.setGeometry(QtCore.QRect(50, 530, 911, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.guess_error_lbl.setFont(font)
        self.guess_error_lbl.setStyleSheet("color: rgb(255, 255, 127);")
        self.guess_error_lbl.setText("")
        self.guess_error_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.guess_error_lbl.setWordWrap(True)
        self.guess_error_lbl.setObjectName("guess_error_lbl")
        self.user_input = QtWidgets.QLineEdit(self.guess_screen)
        self.user_input.setGeometry(QtCore.QRect(40, 680, 611, 87))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.user_input.setFont(font)
        self.user_input.setStyleSheet("border: 5px solid black;\n"
"color: white;")
        self.user_input.setText("")
        self.user_input.setObjectName("user_input")
        self.stackedWidget.addWidget(self.guess_screen)
        self.win_screen = QtWidgets.QWidget()
        self.win_screen.setObjectName("win_screen")
        self.bingus_lbl = QtWidgets.QLabel(self.win_screen)
        self.bingus_lbl.setGeometry(QtCore.QRect(120, 20, 761, 551))
        self.bingus_lbl.setText("")
        self.bingus_lbl.setPixmap(QtGui.QPixmap(":/images/images/bingus.png"))
        self.bingus_lbl.setScaledContents(True)
        self.bingus_lbl.setObjectName("bingus_lbl")
        self.win_lbl = QtWidgets.QLabel(self.win_screen)
        self.win_lbl.setGeometry(QtCore.QRect(20, 620, 931, 121))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.win_lbl.setFont(font)
        self.win_lbl.setStyleSheet("color: rgb(0, 255, 0);")
        self.win_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.win_lbl.setObjectName("win_lbl")
        self.stackedWidget.addWidget(self.win_screen)
        self.lose_screen = QtWidgets.QWidget()
        self.lose_screen.setObjectName("lose_screen")
        self.bully_lbl = QtWidgets.QLabel(self.lose_screen)
        self.bully_lbl.setGeometry(QtCore.QRect(70, 20, 841, 521))
        self.bully_lbl.setText("")
        self.bully_lbl.setPixmap(QtGui.QPixmap(":/images/images/bully.jpg"))
        self.bully_lbl.setScaledContents(True)
        self.bully_lbl.setObjectName("bully_lbl")
        self.lose_lbl = QtWidgets.QLabel(self.lose_screen)
        self.lose_lbl.setGeometry(QtCore.QRect(70, 640, 841, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lose_lbl.setFont(font)
        self.lose_lbl.setStyleSheet("color: rgb(255, 0, 0);\n"
"")
        self.lose_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lose_lbl.setObjectName("lose_lbl")
        self.stackedWidget.addWidget(self.lose_screen)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Guess The Word"))
        self.title_2.setText(_translate("mainWindow", "Guess The Word"))
        self.info_lbl.setText(_translate("mainWindow", "Welcome to Guess The Word. This is a multiplayer word guessing game where one player must input a secret word, and the other player must guess the word in 60 seconds. The guesser has 10 guesses.\n"
"\n"
"Update 1.1:\n"
"A new single-player mode has been implemented in response to lockdown. (software maintenance for changing user requirements)\n"
"\n"
"Good Luck.\n"
"\n"
""))
        self.one_player_btn.setText(_translate("mainWindow", "1 Player"))
        self.two_player_btn.setText(_translate("mainWindow", "2 Player"))
        self.intro_submit_btn.setText(_translate("mainWindow", "GO"))
        self.title.setText(_translate("mainWindow", "Guess The Word"))
        self.secret_word_lbl.setText(_translate("mainWindow", " Enter the secret word:"))
        self.word_submit_btn.setText(_translate("mainWindow", "Submit"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Effective User Interface Design</span><span style=\" font-size:12pt;\">:</span><br/></p><p><span style=\" color:#ffffff;\">WHITESPACE</span></p></body></html>"))
        self.guess_lbl.setText(_translate("mainWindow", "Enter a guess:"))
        self.title2.setText(_translate("mainWindow", "Guess The Word"))
        self.label_3.setText(_translate("mainWindow", "Guesses Remaining:"))
        self.label_4.setText(_translate("mainWindow", "Time Remaining:"))
        self.guess_count_lbl.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">10</span></p></body></html>"))
        self.time_lbl.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">60</span></p></body></html>"))
        self.hint_lbl.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">* * * * * *</span></p></body></html>"))
        self.guess_submit_btn.setText(_translate("mainWindow", "Submit"))
        self.win_lbl.setText(_translate("mainWindow", "Guesser Wins!!!"))
        self.lose_lbl.setText(_translate("mainWindow", "YOU LOSER: THE WAS WAS: SDFSDF"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
