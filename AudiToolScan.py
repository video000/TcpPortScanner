import threading
import time
import os
import socket
import ctypes
import AudiToolScan_rc
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Signal, QObject, Slot
from Ui_ScanMainWindow import Ui_MainWindow
from functools import wraps
from concurrent.futures import ThreadPoolExecutor


class MySignalStr(QObject):
    content = Signal(str)


class MySignalInt(QObject):
    content = Signal(int)


class MySignalBool(QObject):
    content = Signal(bool)


done = MySignalBool()
status = MySignalStr()
# 全局信号，并发通信和刷新qt主线程界面使用。


def Disable_While_Thread_Running(func):
    """
    显示函数运行时间的装饰器，同时也能起到完成后发送完成信号的作用。
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        done.content.emit(True)
        status.content.emit(str("扫描完成， 用时  ") +
                            str(int(time.time()-start)) + "秒！")
        print(str("扫描完成， 用时  ") + str(int(time.time()-start)) + "秒！")
        return f
    return wrapper


class Scanner:
    """
    扫描器类，用了futures的线程池进行控制，默认单线程，50ms超时tcp连接测试。
    """

    def __init__(self, hosts=[], ports=[], max_workers=None, timeout=0.05, isOpenOnly=True):
        self.hosts = hosts
        self.ports = ports
        self.timeout = timeout
        self.max_workers = max_workers
        self.__current = 0
        self.signal_out = MySignalStr()
        self.signal_out_per = MySignalInt()
        self.isOpenOnly = isOpenOnly

    @property
    def total(self):
        return len(self.hosts)*len(self.ports)

    def __progress_per(self):
        return int(100 * self.__current/self.total)

    def __endpoints(self):
        if self.total > 0:
            for host in self.hosts:
                for port in self.ports:
                    yield (host, port)

    def __output(self, endpoint, result):
        """
        用signal_out参数把结果同步输出到
        """
        self.__current += 1
        _out = str(endpoint[0]+":"+str(endpoint[1])+"," +
                   ("opened" if result == 0 else "closed"))

        if self.isOpenOnly:
            if result == 0:
                self.signal_out.content.emit(_out)
                self.signal_out_per.content.emit(self.__progress_per())
            else:
                self.signal_out_per.content.emit(self.__progress_per())
        else:
            self.signal_out.content.emit(_out)
            self.signal_out_per.content.emit(self.__progress_per())

        

    def _scan(self, endpoint):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as so:
            so.settimeout(self.timeout)
            result = so.connect_ex(endpoint)
            self.__output(endpoint, result)

    @ Disable_While_Thread_Running
    def scan(self):
        # self.__updateTotal()
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []

            def _go(a, b):
                # print(futures)
                try:
                    future = executor.submit(a, b)
                    futures.append(future)
                except RuntimeError:
                    time.sleep(0.1)
                    _go(a, b)

            for i in self.__endpoints():
                _go(self._scan, i)
            # print("done")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.setCurrentFile('')
        self.ui.pushButton_scan.clicked.connect(self.enableScanButton)
        self.ui.pushButton_scan.clicked.connect(self.scan)
        self.ui.pushButton_interrupt.clicked.connect(
            self.quit)
        self.ui.action_scan.triggered.connect(self.scan)
        self.ui.action_Abort.triggered.connect(self.quit)
        done.content.connect(self.enableScanButton)
        status.content.connect(self.updateStatusbar)

    @ Slot(str)
    def updateStatusbar(self, str):
        self.statusBar().showMessage(str)

    @ Slot(bool)
    def enableScanButton(self, bo):
        self.ui.pushButton_scan.setEnabled(bo)

    def quit(self):
        try:
            os._exit(5)
        except Exception as e:
            print(e)

    def endpoints_init(self):
        """
        从界面中生成host和port清单的函数，支持多种格式
        行内用空格分开如：www.baidu.com 192.168.1.1
        针对c类ip地址支持范围地址如：192.168.1.1-254
        port同理，同行用空格分开，支持范围表达式如：1-65535
        """
        
        hosts = self.ui.textEdit_dns_or_ip.toPlainText().splitlines()
        for line in hosts:
            if " " in line:
                temp = line.split(" ")
                for i in temp:
                    hosts.insert(hosts.index(line), i)
                hosts.remove(line)
      
        for line in hosts:
            if "-" in line:
                temp = line.split("-")
                temp_split = temp[0].split('.')
                temp_head = temp_split[:-1]
                temp_tail = temp_split
                # print(int(temp_tail[-1]),int(temp[1])+1)
                for i in range(int(temp_tail[-1]), int(temp[1])+1):
                    hosts.insert(hosts.index(line), '.'.join(temp_head)+'.'+str(i))
                    # hosts.insert(hosts.index(line), '.'.join(temp_head)+'.'+str(i))
                hosts.remove(line)

        hosts = list(set(hosts))
        if '' in hosts:
            hosts.remove('')
        ports = self.ui.textEdit_port.toPlainText().splitlines()
        for line in ports:
            if " " in line:
                temp = line.split(" ")
                for i in temp:
                    ports.insert(ports.index(line), i)
                ports.remove(line)
        for line in ports:
            if "-" in line:
                temp = line.split("-")
                for i in range(int(temp[0]), int(temp[1])+1):
                    #ports.insert(ports.index(line), str(i))
                    ports.append(str(i))
                ports.remove(line)
        ports = list(set(ports))
        if '' in ports:
            ports.remove('')
        ports = [int(x) for x in ports]  
        return hosts, ports

    def scan(self):
        self.ui.pushButton_scan.setEnabled(False)
        self.ui.textEdit_result.clear()
        _hosts, _ports = self.endpoints_init()
        self.scanner = Scanner(
            _hosts, _ports)

        self.scanner.isOpenOnly = self.ui.checkBox_show_only_valid.isChecked()
        self.scanner.timeout = float(
            int(self.ui.lineEdit_delay.text())/1000) if self.ui.radioButton_customize_delay.isChecked() else 0.5

        self.scanner.max_workers = int(
            self.ui.lineEdit_threads_amount.text()) if self.ui.radioButton_muti_hreads.isChecked() else 1

        self.scanner.signal_out.content.connect(
            self.UpdateResult)
        self.scanner.signal_out_per.content.connect(self.UpdateProcessBar)
        _t = threading.Thread(target=self.scanner.scan)
        _t.start()
        status.content.emit("扫描中...")

    @ Slot(str)
    def UpdateResult(self,  s):
        self.ui.textEdit_result.append(str(s))

    @ Slot(int)
    def UpdateProcessBar(self, s):
        self.ui.progressBar.setValue(s)
        self.ui.label_progress.setText(
            str(int(self.scanner.total*s/100))+"/"+str(self.scanner.total))

    def closeEvent(self, event):
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    def newFile(self):
        if self.maybeSave():
            map(lambda x: x.clear(), self.ui.textEdit_dns_or_ip,
                self.ui.textEdit_dns_or_ip, self.ui.textBrowser_result)
            self.setCurrentFile('')

    def open(self):
        if self.maybeSave():
            fileName, filtr = QtWidgets.QFileDialog.getOpenFileName(self)
            if fileName:
                self.loadFile(fileName)

    def save(self):
        if self.curFile:
            return self.saveFile(self.curFile)

        return self.saveAs()

    def saveAs(self):
        fileName, filtr = QtWidgets.QFileDialog.getSaveFileName(self)
        if fileName:
            return self.saveFile(fileName)

        return False

    def about(self):
        QtWidgets.QMessageBox.about(self, "关于",
                                    "< b > AutiTool—Scan < /b >"
                                    "<p>一个支持多线程并发方式的端口扫描工具，支持将扫描配置和结果读写文到文件"
                                    "用于测试域内网络端口到端口逻辑隔离策略。< /p >"
                                    "<p>当前版本V1.0。</p>"
                                    "<p>本软件为开源软件，遵守LGPL协议。</p>")

    def documentWasModified(self):
        if (self.ui.textEdit_dns_or_ip.document().isModified() or self.ui.textEdit_port.isModified() or self.ui.textEdit_result.isModified()):
            self.setWindowModified(True)
        else:
            self.setWindowModified(False)

    def createActions(self):
        self.newAct = QtWidgets.QAction(QtGui.QIcon(':/images/new.png'), "&新建",
                                        self, shortcut=QtGui.QKeySequence.New,
                                        statusTip="新建文件", triggered=self.newFile)

        self.openAct = QtWidgets.QAction(QtGui.QIcon(':/images/open.png'),
                                         "打开...", self, shortcut=QtGui.QKeySequence.Open,
                                         statusTip="打开文件", triggered=self.open)

        self.saveAct = QtWidgets.QAction(QtGui.QIcon(':/images/save.png'),
                                         "保存", self, shortcut=QtGui.QKeySequence.Save,
                                         statusTip="保存文件", triggered=self.save)

        self.saveAsAct = QtWidgets.QAction("另存为...", self,
                                           shortcut=QtGui.QKeySequence.SaveAs,
                                           statusTip="另存为",
                                           triggered=self.saveAs)

        self.exitAct = QtWidgets.QAction("退出", self, shortcut="Ctrl+Q",
                                         statusTip="退出程序", triggered=self.close)

        self.cutAct = QtWidgets.QAction(QtGui.QIcon(':/images/cut.png'), "剪切",
                                        self, shortcut=QtGui.QKeySequence.Cut,
                                        statusTip="将选中文本剪贴到剪贴板",
                                        triggered=self.ui.textEdit_dns_or_ip.cut)

        self.copyAct = QtWidgets.QAction(QtGui.QIcon(':/images/copy.png'),
                                         "复制", self, shortcut=QtGui.QKeySequence.Copy,
                                         statusTip="将选中位置复制到剪贴板",
                                         triggered=self.ui.textEdit_dns_or_ip.copy)

        self.pasteAct = QtWidgets.QAction(QtGui.QIcon(':/images/paste.png'),
                                          "粘贴", self, shortcut=QtGui.QKeySequence.Paste,
                                          statusTip="粘贴到指定位置",
                                          triggered=self.ui.textEdit_dns_or_ip.paste)

        self.aboutAct = QtWidgets.QAction("&关于", self,
                                          statusTip="关于",
                                          triggered=self.about)

        self.aboutQtAct = QtWidgets.QAction("About &Qt", self,
                                            statusTip="Show the Qt library's About box",
                                            triggered=qApp.aboutQt)

        self.cutAct.setEnabled(False)
        self.copyAct.setEnabled(False)
        self.ui.textEdit_dns_or_ip.copyAvailable.connect(
            self.cutAct.setEnabled)
        self.ui.textEdit_dns_or_ip.copyAvailable.connect(
            self.copyAct.setEnabled)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("文件")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("编辑")
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("帮助")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar("文件")
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)

        self.editToolBar = self.addToolBar("编辑")
        self.editToolBar.addAction(self.cutAct)
        self.editToolBar.addAction(self.copyAct)
        self.editToolBar.addAction(self.pasteAct)

    def createStatusBar(self):
        self.statusBar().showMessage("就绪")

    def setStatusBara(self, a):
        self.statusBar().showMessage(a, 2000)

    def readSettings(self):
        settings = QtCore.QSettings("", "AudiTool-Scan")
        pos = settings.value("pos", QtCore.QPoint(200, 200))
        size = settings.value("size", QtCore.QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        settings = QtCore.QSettings("", "AudiTool-Scan")
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())

    def maybeSave(self):
        if (self.ui.textEdit_dns_or_ip.document().isModified()) or (self.ui.textEdit_port.document().isModified()) or (self.ui.textEdit_result.document().isModified()):
            ret = QtWidgets.QMessageBox.warning(self, "AudiTool-Scan",
                                                "文件已修改.\n需要保存到本地吗？",
                                                QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard |
                                                QtWidgets.QMessageBox.Cancel)
            if ret == QtWidgets.QMessageBox.Save:
                return self.save()
            elif ret == QtWidgets.QMessageBox.Cancel:
                return False
        return True

    def loadFile(self, fileName):
        file = QtCore.QFile(fileName)
        if not file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            QtWidgets.QMessageBox.warning(self, "AudiTool-Scan",
                                          "无法读取 %s:\n%s." % (fileName, file.errorString()))
            return

        inf = QtCore.QTextStream(file).readAll().splitlines()

        self.ui.textEdit_dns_or_ip.setPlainText(
            '\n'.join(inf[inf.index('[hosts]')+1: inf.index('[ports]')]))

        self.ui.textEdit_port.setPlainText(
            '\n'.join(inf[inf.index('[ports]')+1: inf.index('[results]')]))

        self.ui.textEdit_result.setPlainText(
            '\n'.join(inf[inf.index('[results]')+1: inf.index('[show_only_valid]')]))

        self.ui.checkBox_show_only_valid.setChecked(
            False) if inf[inf.index('[show_only_valid]')+1] == '0' else self.ui.checkBox_show_only_valid.setChecked(True)

        self.ui.radioButton_default_delay.setChecked(
            True) if inf[inf.index('[customize_delay]')+1] == '0' else self.ui.radioButton_customize_delay.setChecked(True)

        self.ui.lineEdit_delay.setText(inf[inf.index('[customize_delay]')+1])

        self.ui.radioButton_single_thread.setChecked(
            True) if inf[inf.index('[threads_amount]')+1] == '1' else self.ui.radioButton_muti_hreads.setChecked(True)

        self.ui.lineEdit_threads_amount.setText(
            inf[inf.index('[threads_amount]')+1])

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        QtWidgets.QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("文件已读取", 2000)

    def saveFile(self, fileName):
        error = None
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        file = QtCore.QSaveFile(fileName)
        if file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            outf = QtCore.QTextStream(file)
            outf << "[hosts]\n"
            outf << self.ui.textEdit_dns_or_ip.toPlainText()
            outf << "\n[ports]\n"
            outf << self.ui.textEdit_port.toPlainText()
            outf << "\n[results]\n"
            outf << self.ui.textEdit_result.toPlainText()
            outf << "\n[show_only_valid]\n"
            outf << self.ui.checkBox_show_only_valid.isChecked()
            outf << "\n[customize_delay]\n"
            outf << (self.ui.lineEdit_delay.text() if self.ui.radioButton_customize_delay.isChecked(
            ) else '0')
            outf << "\n[threads_amount]\n"
            outf << (self.ui.lineEdit_threads_amount.text() if self.ui.radioButton_muti_hreads.isChecked(
            ) else '1')

            if not file.commit():
                error = "无法保存文件 %s:\n%s." % (
                    fileName, file.errorString())
        else:
            error = "无法打开文件 %s:\n%s." % (
                fileName, file.errorString())
        QtWidgets.QApplication.restoreOverrideCursor()

        if error:
            QtWidgets.QMessageBox.warning(self, "AudiTool-Scan", error)
            return False

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("文件已保存", 2000)
        return True

    def setCurrentFile(self, fileName):
        self.curFile = fileName
        self.ui.textEdit_dns_or_ip.document().setModified(False)
        self.ui.textEdit_port.document().setModified(False)
        self.ui.textEdit_result.document().setModified(False)
        self.setWindowModified(False)

        if self.curFile:
            shownName = self.strippedName(self.curFile)
        else:
            shownName = 'untitled.txt'

        self.setWindowTitle("%s[*] - AudiTool-Scan" % shownName)

    def strippedName(self, fullFileName):
        return QtCore.QFileInfo(fullFileName).fileName()


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
