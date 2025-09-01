# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(647, 424)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(650, 428))
        self.centralwidget.setStyleSheet(u"background-color: #10383A;")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color: #768886;\n"
"border-radius:10px;\n"
"}")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 100))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"background-color: #10383A;\n"
"border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 50))
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.widget_4.setStyleSheet(u"background-color: #10383A;\n"
"")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color:#10383A;\n"
"color: #DAA112;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 0, 0, 1, 2)

        self.card2 = QWidget(self.frame)
        self.card2.setObjectName(u"card2")
        self.card2.setStyleSheet(u"QWidget#card2{\n"
"background-color: #666E51;\n"
"border-radius: 10px;\n"
"border: 1px solid #ccc;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.card2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.countainer_port = QWidget(self.card2)
        self.countainer_port.setObjectName(u"countainer_port")
        self.countainer_port.setMaximumSize(QSize(16777215, 100))
        self.countainer_port.setStyleSheet(u"QWidget#countainer_port{\n"
"background-color: #809276;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.gridLayout_9 = QGridLayout(self.countainer_port)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pb_connect = QPushButton(self.countainer_port)
        self.pb_connect.setObjectName(u"pb_connect")
        self.pb_connect.setStyleSheet(u"background-color:green;")

        self.gridLayout_9.addWidget(self.pb_connect, 1, 1, 1, 1)

        self.select_port = QComboBox(self.countainer_port)
        self.select_port.setObjectName(u"select_port")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_port.sizePolicy().hasHeightForWidth())
        self.select_port.setSizePolicy(sizePolicy)
        self.select_port.setContextMenuPolicy(Qt.PreventContextMenu)
        self.select_port.setStyleSheet(u"")
        self.select_port.setMaxVisibleItems(5)
        self.select_port.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.select_port.setMinimumContentsLength(1)

        self.gridLayout_9.addWidget(self.select_port, 0, 0, 2, 1)

        self.pb_refresh = QPushButton(self.countainer_port)
        self.pb_refresh.setObjectName(u"pb_refresh")

        self.gridLayout_9.addWidget(self.pb_refresh, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.countainer_port, 0, 0, 1, 1)

        self.countainer_value = QWidget(self.card2)
        self.countainer_value.setObjectName(u"countainer_value")
        self.countainer_value.setStyleSheet(u"QWidget#countainer_value{\n"
"background-color: #809276;\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.countainer_value)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_7 = QWidget(self.countainer_value)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color: #809276;\n"
"")
        self.gridLayout_11 = QGridLayout(self.widget_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_21 = QLabel(self.widget_7)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_11.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_22 = QLabel(self.widget_7)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_11.addWidget(self.label_22, 1, 0, 1, 1)

        self.label_23 = QLabel(self.widget_7)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_11.addWidget(self.label_23, 2, 0, 1, 1)

        self.pb_lokator2 = QPushButton(self.widget_7)
        self.pb_lokator2.setObjectName(u"pb_lokator2")
        self.pb_lokator2.setStyleSheet(u"background-color:#10383A;\n"
"")

        self.gridLayout_11.addWidget(self.pb_lokator2, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.countainer_value)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: #809276;\n"
"")
        self.gridLayout_10 = QGridLayout(self.widget_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.encoder_value = QLabel(self.widget_8)
        self.encoder_value.setObjectName(u"encoder_value")
        self.encoder_value.setStyleSheet(u"")
        self.encoder_value.setFrameShape(QFrame.NoFrame)

        self.gridLayout_10.addWidget(self.encoder_value, 0, 0, 1, 1)

        self.kondisi_value = QLabel(self.widget_8)
        self.kondisi_value.setObjectName(u"kondisi_value")

        self.gridLayout_10.addWidget(self.kondisi_value, 1, 0, 1, 1)

        self.dac_value = QLabel(self.widget_8)
        self.dac_value.setObjectName(u"dac_value")

        self.gridLayout_10.addWidget(self.dac_value, 2, 0, 1, 1)

        self.locator_value = QLineEdit(self.widget_8)
        self.locator_value.setObjectName(u"locator_value")
        self.locator_value.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_10.addWidget(self.locator_value, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_8)


        self.gridLayout_8.addWidget(self.countainer_value, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.card2, 1, 1, 1, 1)

        self.card1 = QWidget(self.frame)
        self.card1.setObjectName(u"card1")
        self.card1.setMaximumSize(QSize(300, 16777215))
        self.card1.setStyleSheet(u"QWidget#card1{\n"
"background-color: #666E51;\n"
"border-radius: 10px;\n"
"border: 1px solid #ccc;\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.card1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pb_LIDA = QPushButton(self.card1)
        self.pb_LIDA.setObjectName(u"pb_LIDA")

        self.gridLayout_4.addWidget(self.pb_LIDA, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.card1)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #666E51;")
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page_LIDA = QWidget()
        self.page_LIDA.setObjectName(u"page_LIDA")
        self.page_LIDA.setStyleSheet(u"QFrame{\n"
"background-color: #809276;\n"
"border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"background-color: #666E51;\n"
"}\n"
"QWidget#page_LIDA{\n"
"border-radius: 10px;\n"
"border:1px solid #ccc;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.page_LIDA)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_4 = QFrame(self.page_LIDA)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: #809276;\n"
"")
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Input_X1L_P1_LIDA = QLineEdit(self.frame_4)
        self.Input_X1L_P1_LIDA.setObjectName(u"Input_X1L_P1_LIDA")
        self.Input_X1L_P1_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Input_X1L_P1_LIDA)

        self.Input_X1L_P2_LIDA = QLineEdit(self.frame_4)
        self.Input_X1L_P2_LIDA.setObjectName(u"Input_X1L_P2_LIDA")
        self.Input_X1L_P2_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Input_X1L_P2_LIDA)

        self.Input_X1L_P3_LIDA = QLineEdit(self.frame_4)
        self.Input_X1L_P3_LIDA.setObjectName(u"Input_X1L_P3_LIDA")
        self.Input_X1L_P3_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Input_X1L_P3_LIDA)

        self.Input_X1L_P4_LIDA = QLineEdit(self.frame_4)
        self.Input_X1L_P4_LIDA.setObjectName(u"Input_X1L_P4_LIDA")
        self.Input_X1L_P4_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Input_X1L_P4_LIDA)

        self.Input_X1L_P5_LIDA = QLineEdit(self.frame_4)
        self.Input_X1L_P5_LIDA.setObjectName(u"Input_X1L_P5_LIDA")
        self.Input_X1L_P5_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Input_X1L_P5_LIDA)

        self.Input_X1L_P6_LIDA = QLineEdit(self.frame_4)
        self.Input_X1L_P6_LIDA.setObjectName(u"Input_X1L_P6_LIDA")
        self.Input_X1L_P6_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Input_X1L_P6_LIDA)


        self.gridLayout_6.addWidget(self.frame_4, 1, 2, 1, 1)

        self.frame_5 = QFrame(self.page_LIDA)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: #809276;\n"
"")
        self.frame_5.setFrameShape(QFrame.WinPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Input_X1R_P1_LIDA = QLineEdit(self.frame_5)
        self.Input_X1R_P1_LIDA.setObjectName(u"Input_X1R_P1_LIDA")
        self.Input_X1R_P1_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Input_X1R_P1_LIDA)

        self.Input_X1R_P2_LIDA = QLineEdit(self.frame_5)
        self.Input_X1R_P2_LIDA.setObjectName(u"Input_X1R_P2_LIDA")
        self.Input_X1R_P2_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Input_X1R_P2_LIDA)

        self.Input_X1R_P3_LIDA = QLineEdit(self.frame_5)
        self.Input_X1R_P3_LIDA.setObjectName(u"Input_X1R_P3_LIDA")
        self.Input_X1R_P3_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Input_X1R_P3_LIDA)

        self.Input_X1R_P4_LIDA = QLineEdit(self.frame_5)
        self.Input_X1R_P4_LIDA.setObjectName(u"Input_X1R_P4_LIDA")
        self.Input_X1R_P4_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Input_X1R_P4_LIDA)

        self.Input_X1R_P5_LIDA = QLineEdit(self.frame_5)
        self.Input_X1R_P5_LIDA.setObjectName(u"Input_X1R_P5_LIDA")
        self.Input_X1R_P5_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Input_X1R_P5_LIDA)

        self.Input_X1R_P6_LIDA = QLineEdit(self.frame_5)
        self.Input_X1R_P6_LIDA.setObjectName(u"Input_X1R_P6_LIDA")
        self.Input_X1R_P6_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Input_X1R_P6_LIDA)


        self.gridLayout_6.addWidget(self.frame_5, 1, 3, 1, 1)

        self.frame_2 = QFrame(self.page_LIDA)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #809276;\n"
"")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)


        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)

        self.label_2 = QLabel(self.page_LIDA)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 12))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.page_LIDA)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: #809276;\n"
"")
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Input_X2L_P1_LIDA = QLineEdit(self.frame_3)
        self.Input_X2L_P1_LIDA.setObjectName(u"Input_X2L_P1_LIDA")
        self.Input_X2L_P1_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Input_X2L_P1_LIDA)

        self.Input_X2L_P2_LIDA = QLineEdit(self.frame_3)
        self.Input_X2L_P2_LIDA.setObjectName(u"Input_X2L_P2_LIDA")
        self.Input_X2L_P2_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Input_X2L_P2_LIDA)

        self.Input_X2L_P3_LIDA = QLineEdit(self.frame_3)
        self.Input_X2L_P3_LIDA.setObjectName(u"Input_X2L_P3_LIDA")
        self.Input_X2L_P3_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Input_X2L_P3_LIDA)

        self.Input_X2L_P4_LIDA = QLineEdit(self.frame_3)
        self.Input_X2L_P4_LIDA.setObjectName(u"Input_X2L_P4_LIDA")
        self.Input_X2L_P4_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Input_X2L_P4_LIDA)

        self.Input_X2L_P5_LIDA = QLineEdit(self.frame_3)
        self.Input_X2L_P5_LIDA.setObjectName(u"Input_X2L_P5_LIDA")
        self.Input_X2L_P5_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Input_X2L_P5_LIDA)

        self.Input_X2L_P6_LIDA = QLineEdit(self.frame_3)
        self.Input_X2L_P6_LIDA.setObjectName(u"Input_X2L_P6_LIDA")
        self.Input_X2L_P6_LIDA.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Input_X2L_P6_LIDA)


        self.gridLayout_6.addWidget(self.frame_3, 1, 1, 1, 1)

        self.label_3 = QLabel(self.page_LIDA)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 10))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_4 = QLabel(self.page_LIDA)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 10))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_5 = QLabel(self.page_LIDA)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 10))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_LIDA)
        self.page_KCLKA = QWidget()
        self.page_KCLKA.setObjectName(u"page_KCLKA")
        self.page_KCLKA.setStyleSheet(u"QFrame{\n"
"background-color: #809276;\n"
"border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"background-color: #666E51;\n"
"}\n"
"QWidget#page_KCLKA{\n"
"border-radius: 10px;\n"
"border:1px solid #ccc;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.page_KCLKA)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_6 = QFrame(self.page_KCLKA)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(28, 16777215))
        self.frame_6.setStyleSheet(u"background-color: #809276;\n"
"")
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_5.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_5.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_5.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_5.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_5.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_5.addWidget(self.label_19)


        self.gridLayout_7.addWidget(self.frame_6, 1, 1, 1, 1)

        self.label_13 = QLabel(self.page_KCLKA)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 12))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_13, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.label_12 = QLabel(self.page_KCLKA)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 10))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_12, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.page_KCLKA)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: #809276;\n"
"")
        self.frame_7.setFrameShape(QFrame.WinPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Input_X1_P1_KCLKA = QLineEdit(self.frame_7)
        self.Input_X1_P1_KCLKA.setObjectName(u"Input_X1_P1_KCLKA")
        self.Input_X1_P1_KCLKA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Input_X1_P1_KCLKA)

        self.Input_X1_P2_KCLKA = QLineEdit(self.frame_7)
        self.Input_X1_P2_KCLKA.setObjectName(u"Input_X1_P2_KCLKA")
        self.Input_X1_P2_KCLKA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Input_X1_P2_KCLKA)

        self.Input_X1_P3_KCLKA = QLineEdit(self.frame_7)
        self.Input_X1_P3_KCLKA.setObjectName(u"Input_X1_P3_KCLKA")
        self.Input_X1_P3_KCLKA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Input_X1_P3_KCLKA)

        self.Input_X1_P4_KCLKA = QLineEdit(self.frame_7)
        self.Input_X1_P4_KCLKA.setObjectName(u"Input_X1_P4_KCLKA")
        self.Input_X1_P4_KCLKA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Input_X1_P4_KCLKA)

        self.Input_X1_P5_KCLKA = QLineEdit(self.frame_7)
        self.Input_X1_P5_KCLKA.setObjectName(u"Input_X1_P5_KCLKA")
        self.Input_X1_P5_KCLKA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Input_X1_P5_KCLKA)

        self.Input_X1_P6_KCLKA = QLineEdit(self.frame_7)
        self.Input_X1_P6_KCLKA.setObjectName(u"Input_X1_P6_KCLKA")
        self.Input_X1_P6_KCLKA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Input_X1_P6_KCLKA)


        self.gridLayout_7.addWidget(self.frame_7, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_KCLKA)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 2)

        self.pb_KCLKA = QPushButton(self.card1)
        self.pb_KCLKA.setObjectName(u"pb_KCLKA")

        self.gridLayout_4.addWidget(self.pb_KCLKA, 0, 1, 1, 1)

        self.pb_lokator1 = QPushButton(self.card1)
        self.pb_lokator1.setObjectName(u"pb_lokator1")

        self.gridLayout_4.addWidget(self.pb_lokator1, 2, 0, 1, 2)


        self.gridLayout_3.addWidget(self.card1, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.select_port.setCurrentIndex(-1)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KALIBRASI ENCODER IOT", None))
        self.pb_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pb_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Encoder Pulse", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Kondisi", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"DAC", None))
        self.pb_lokator2.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.encoder_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.kondisi_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dac_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pb_LIDA.setText(QCoreApplication.translate("MainWindow", u"LIDA", None))
        self.Input_X1L_P1_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1L_P2_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1L_P3_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1L_P4_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1L_P5_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1L_P6_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1R_P1_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1R_P2_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1R_P3_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1R_P4_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1R_P5_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1R_P6_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X2-L", None))
        self.Input_X2L_P1_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X2L_P2_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X2L_P3_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X2L_P4_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X2L_P5_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X2L_P6_LIDA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X1-L", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X1-R", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"No.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Position X1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"No.", None))
        self.Input_X1_P1_KCLKA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1_P2_KCLKA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1_P3_KCLKA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1_P4_KCLKA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1_P5_KCLKA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Input_X1_P6_KCLKA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pb_KCLKA.setText(QCoreApplication.translate("MainWindow", u"KCLKA", None))
        self.pb_lokator1.setText(QCoreApplication.translate("MainWindow", u"Input", None))
    # retranslateUi

