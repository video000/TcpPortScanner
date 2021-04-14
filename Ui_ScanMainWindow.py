# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScanMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_scan = QAction(MainWindow)
        self.action_scan.setObjectName(u"action_scan")
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        self.action_Abort = QAction(MainWindow)
        self.action_Abort.setObjectName(u"action_Abort")
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_saveAs = QAction(MainWindow)
        self.action_saveAs.setObjectName(u"action_saveAs")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_dns_or_ip = QGroupBox(self.centralwidget)
        self.groupBox_dns_or_ip.setObjectName(u"groupBox_dns_or_ip")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_dns_or_ip)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEdit_dns_or_ip = QTextEdit(self.groupBox_dns_or_ip)
        self.textEdit_dns_or_ip.setObjectName(u"textEdit_dns_or_ip")
        self.textEdit_dns_or_ip.setAcceptDrops(False)
        self.textEdit_dns_or_ip.setAutoFormatting(QTextEdit.AutoNone)
        self.textEdit_dns_or_ip.setTabChangesFocus(True)
        self.textEdit_dns_or_ip.setLineWrapMode(QTextEdit.WidgetWidth)

        self.horizontalLayout_4.addWidget(self.textEdit_dns_or_ip)


        self.verticalLayout_3.addWidget(self.groupBox_dns_or_ip)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_port = QGroupBox(self.centralwidget)
        self.groupBox_port.setObjectName(u"groupBox_port")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_port)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textEdit_port = QTextEdit(self.groupBox_port)
        self.textEdit_port.setObjectName(u"textEdit_port")
        self.textEdit_port.setAcceptDrops(False)
        self.textEdit_port.setTabChangesFocus(True)

        self.horizontalLayout_5.addWidget(self.textEdit_port)


        self.verticalLayout_4.addWidget(self.groupBox_port)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3.setStretch(0, 7)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_result = QGroupBox(self.centralwidget)
        self.groupBox_result.setObjectName(u"groupBox_result")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_result)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_show_only_valid = QCheckBox(self.groupBox_result)
        self.checkBox_show_only_valid.setObjectName(u"checkBox_show_only_valid")
        self.checkBox_show_only_valid.setFocusPolicy(Qt.ClickFocus)
        self.checkBox_show_only_valid.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBox_show_only_valid)

        self.textEdit_result = QTextEdit(self.groupBox_result)
        self.textEdit_result.setObjectName(u"textEdit_result")
        self.textEdit_result.setFocusPolicy(Qt.ClickFocus)
        self.textEdit_result.setAcceptDrops(False)
        self.textEdit_result.setTabChangesFocus(True)

        self.verticalLayout_6.addWidget(self.textEdit_result)


        self.verticalLayout_5.addWidget(self.groupBox_result)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.groupBox_config = QGroupBox(self.centralwidget)
        self.groupBox_config.setObjectName(u"groupBox_config")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_config)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tabWidget_config = QTabWidget(self.groupBox_config)
        self.tabWidget_config.setObjectName(u"tabWidget_config")
        self.tabWidget_config.setTabletTracking(False)
        self.tabWidget_config.setFocusPolicy(Qt.ClickFocus)
        self.tabWidget_config.setTabShape(QTabWidget.Rounded)
        self.tabWidget_config.setElideMode(Qt.ElideLeft)
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_14 = QVBoxLayout(self.tab_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_6 = QGroupBox(self.tab_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.radioButton_single_thread = QRadioButton(self.groupBox_6)
        self.radioButton_single_thread.setObjectName(u"radioButton_single_thread")
        self.radioButton_single_thread.setFocusPolicy(Qt.ClickFocus)
        self.radioButton_single_thread.setChecked(False)

        self.verticalLayout_16.addWidget(self.radioButton_single_thread)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.radioButton_muti_hreads = QRadioButton(self.groupBox_6)
        self.radioButton_muti_hreads.setObjectName(u"radioButton_muti_hreads")
        self.radioButton_muti_hreads.setFocusPolicy(Qt.ClickFocus)
        self.radioButton_muti_hreads.setChecked(True)

        self.horizontalLayout_17.addWidget(self.radioButton_muti_hreads)

        self.lineEdit_threads_amount = QLineEdit(self.groupBox_6)
        self.lineEdit_threads_amount.setObjectName(u"lineEdit_threads_amount")
        self.lineEdit_threads_amount.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_threads_amount.sizePolicy().hasHeightForWidth())
        self.lineEdit_threads_amount.setSizePolicy(sizePolicy)
        self.lineEdit_threads_amount.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_threads_amount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.lineEdit_threads_amount)


        self.verticalLayout_16.addLayout(self.horizontalLayout_17)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.verticalLayout_14.addWidget(self.groupBox_6)

        self.tabWidget_config.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_11 = QVBoxLayout(self.tab_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_5 = QGroupBox(self.tab_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_default_delay = QRadioButton(self.groupBox_5)
        self.radioButton_default_delay.setObjectName(u"radioButton_default_delay")
        self.radioButton_default_delay.setFocusPolicy(Qt.ClickFocus)
        self.radioButton_default_delay.setChecked(True)

        self.verticalLayout_13.addWidget(self.radioButton_default_delay)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.radioButton_customize_delay = QRadioButton(self.groupBox_5)
        self.radioButton_customize_delay.setObjectName(u"radioButton_customize_delay")
        self.radioButton_customize_delay.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_16.addWidget(self.radioButton_customize_delay)

        self.lineEdit_delay = QLineEdit(self.groupBox_5)
        self.lineEdit_delay.setObjectName(u"lineEdit_delay")
        self.lineEdit_delay.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_delay.sizePolicy().hasHeightForWidth())
        self.lineEdit_delay.setSizePolicy(sizePolicy1)
        self.lineEdit_delay.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.lineEdit_delay)

        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_16.addWidget(self.label)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)


        self.verticalLayout_12.addLayout(self.verticalLayout_13)


        self.verticalLayout_11.addWidget(self.groupBox_5)

        self.tabWidget_config.addTab(self.tab_5, "")

        self.horizontalLayout_15.addWidget(self.tabWidget_config)


        self.horizontalLayout_2.addWidget(self.groupBox_config)

        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout.addWidget(self.progressBar)

        self.label_progress = QLabel(self.centralwidget)
        self.label_progress.setObjectName(u"label_progress")

        self.horizontalLayout.addWidget(self.label_progress)

        self.label_total = QLabel(self.centralwidget)
        self.label_total.setObjectName(u"label_total")

        self.horizontalLayout.addWidget(self.label_total)

        self.pushButton_interrupt = QPushButton(self.centralwidget)
        self.pushButton_interrupt.setObjectName(u"pushButton_interrupt")
        self.pushButton_interrupt.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.pushButton_interrupt)

        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.pushButton_reset)

        self.pushButton_scan = QPushButton(self.centralwidget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.pushButton_scan)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.textEdit_dns_or_ip, self.textEdit_port)
        QWidget.setTabOrder(self.textEdit_port, self.textEdit_result)
        QWidget.setTabOrder(self.textEdit_result, self.checkBox_show_only_valid)
        QWidget.setTabOrder(self.checkBox_show_only_valid, self.tabWidget_config)
        QWidget.setTabOrder(self.tabWidget_config, self.radioButton_default_delay)
        QWidget.setTabOrder(self.radioButton_default_delay, self.radioButton_customize_delay)
        QWidget.setTabOrder(self.radioButton_customize_delay, self.lineEdit_delay)
        QWidget.setTabOrder(self.lineEdit_delay, self.radioButton_single_thread)
        QWidget.setTabOrder(self.radioButton_single_thread, self.radioButton_muti_hreads)
        QWidget.setTabOrder(self.radioButton_muti_hreads, self.lineEdit_threads_amount)
        QWidget.setTabOrder(self.lineEdit_threads_amount, self.pushButton_interrupt)
        QWidget.setTabOrder(self.pushButton_interrupt, self.pushButton_reset)
        QWidget.setTabOrder(self.pushButton_reset, self.pushButton_scan)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_scan)
        self.menu.addAction(self.action_Abort)

        self.retranslateUi(MainWindow)
        self.pushButton_reset.clicked.connect(self.textEdit_dns_or_ip.clear)
        self.pushButton_reset.clicked.connect(self.textEdit_port.clear)
        self.pushButton_reset.clicked.connect(self.textEdit_result.clear)

        self.tabWidget_config.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_scan.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
#if QT_CONFIG(shortcut)
        self.action_scan.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a ", None))
#if QT_CONFIG(shortcut)
        self.action_clear.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
        self.action_Abort.setText(QCoreApplication.translate("MainWindow", u"\u5f3a\u5236\u9000\u51fa", None))
#if QT_CONFIG(shortcut)
        self.action_Abort.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.action_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_saveAs.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
#if QT_CONFIG(shortcut)
        self.action_saveAs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.groupBox_dns_or_ip.setTitle(QCoreApplication.translate("MainWindow", u"Host\u5730\u5740", None))
#if QT_CONFIG(tooltip)
        self.textEdit_dns_or_ip.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4ece\u754c\u9762\u4e2d\u751f\u6210host\u548cport\u6e05\u5355\u7684\u51fd\u6570\uff0c\u652f\u6301\u591a\u79cd\u683c\u5f0f</p><p>\u884c\u5185\u7528\u7a7a\u683c\u5206\u5f00\u5982\uff1awww.baidu.com 192.168.1.1</p><p>\u5bf9C\u7c7bip\u5730\u5740\u652f\u6301\u8303\u56f4\u5730\u5740\u5982\uff1a192.168.1.1-254</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.textEdit_dns_or_ip.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">127.0.0.1</p></body></html>", None))
        self.groupBox_port.setTitle(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3", None))
#if QT_CONFIG(tooltip)
        self.textEdit_port.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>port\u540c\u7406\uff0c\u540c\u884c\u7528\u7a7a\u683c\u5206\u5f00\uff0c\u652f\u6301\u8303\u56f4\u8868\u8fbe\u5f0f\u5982\uff1a1-65535</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.textEdit_port.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20-25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">53 69</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">80 89 443 8440-8450 8080-8089</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">110 111 2049</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "137 139 445 3389</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">143 161 389</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">512-514</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1443 3306 1521 5000 5432 6379 27017-27018</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3690 5900-5902</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7001-7002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9080-9081 9090 9200 9300</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\">11211</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">50070 50030</p></body></html>", None))
        self.groupBox_result.setTitle(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u7ed3\u679c", None))
        self.checkBox_show_only_valid.setText(QCoreApplication.translate("MainWindow", u"\u4ec5\u663e\u793a\u6709\u6548\u7ed3\u679c\u7ed3\u679c/\u663e\u793a\u6240\u6709\u7ed3\u679c", None))
        self.groupBox_config.setTitle(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b\u6570\u91cf\u914d\u7f6e", None))
        self.radioButton_single_thread.setText(QCoreApplication.translate("MainWindow", u"\u5355\u7ebf\u7a0b", None))
        self.radioButton_muti_hreads.setText(QCoreApplication.translate("MainWindow", u"\u591a\u7ebf\u7a0b\u5e76\u53d1\u91cf", None))
        self.lineEdit_threads_amount.setText(QCoreApplication.translate("MainWindow", u"64", None))
        self.tabWidget_config.setTabText(self.tabWidget_config.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u5e76\u53d1", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"TCP\u8fde\u63a5\u8d85\u65f6", None))
        self.radioButton_default_delay.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u8d85\u65f6(500ms)", None))
        self.radioButton_customize_delay.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u65f6\u65f6\u95f4", None))
        self.lineEdit_delay.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.tabWidget_config.setTabText(self.tabWidget_config.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u901f\u7387", None))
        self.label_progress.setText(QCoreApplication.translate("MainWindow", u"12/65535", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"\u5171\u8ba1", None))
        self.pushButton_interrupt.setText(QCoreApplication.translate("MainWindow", u"\u5f3a\u5236\u9000\u51fa", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u4fe1\u606f", None))
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf(F5)", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u626b\u63cf", None))
    # retranslateUi

