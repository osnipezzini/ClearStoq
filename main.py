import os
import sys

from PySide2 import QtCore
from PySide2.QtCore import QTime
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QDialogButtonBox
from PySide2.QtGui import QIcon  # Get the package to add an icon

import db
from gui.main_window import Ui_MainWindow
from gui.config_window import Ui_Dialog
from utils import resource_path
from utils.log import logger
from config import Config

path = resource_path("Icon.ico")


class ConfigWindow(QDialog):
    def __init__(self, parent):
        super(ConfigWindow, self).__init__()
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.config = dict()
        self.connect_signals()
        cfg = Config()
        if cfg.is_config('default'):
            self.config = cfg.get('default')
            self.dict2field(self.config)

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.cancel)
        self.ui.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.reset)

    def accept(self):
        self.validate_fields()
        cfg = self.field2dict()
        self.config['default'] = cfg
        dbe = db.DB(**cfg)
        if dbe.conn():
            self.save()
        else:
            msg = QMessageBox()
            msg.setWindowIcon(self.windowIcon())
            msg.setWindowTitle("Aviso")
            msg.setText(f"Ocorreu um erro ao conectar ao banco de dados , verifique os dados informados e tente novamente .")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            ret = msg.exec_()

    def validate_fields(self):
        self.ui.textHost.setText(self.ui.textHost.text() if self.ui.textHost.text() != "" else "localhost")
        self.ui.textPort.setText(self.ui.textPort.text() if self.ui.textPort.text() != "" else "5432")
        self.ui.textUser.setText(self.ui.textUser.text() if self.ui.textUser.text() != "" else "postgres")
        self.ui.textName.setText(self.ui.textName.text() if self.ui.textName.text() != "" else "autosystem")

    def save(self):
        cfg = Config()
        if cfg.set(self.config):
            msg = QMessageBox()
            msg.setWindowIcon(self.windowIcon())
            msg.setWindowTitle("Aviso")
            msg.setText(f"As configurações foram salvas em : {cfg.cfg_file} .")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            ret = msg.exec_()
            if ret == QMessageBox.Ok:
                self.close()

    def dict2field(self, cfg):
        self.ui.textHost.setText(cfg["host"])
        self.ui.textPort.setText(cfg["port"])
        self.ui.textUser.setText(cfg["user"])
        self.ui.textPassword.setText(cfg["password"])
        self.ui.textName.setText(cfg["dbname"])

    def field2dict(self):
        cfg = dict()
        cfg["host"] = self.ui.textHost.text()
        cfg["port"] = self.ui.textPort.text()
        cfg["dbname"] = self.ui.textName.text()
        cfg["user"] = self.ui.textUser.text()
        cfg["password"] = self.ui.textPassword.text()
        return cfg

    def reset(self):
        self.ui.textHost.setText("")
        self.ui.textPort.setText("")
        self.ui.textUser.setText("")
        self.ui.textPassword.setText("")
        self.ui.textName.setText("")

    def cancel(self):
        sys.exit()


class MainWindow(QMainWindow):

    def log(self, text):
        logger.info(text)

    def make_actions(self):
        self.ui.textLog.appendPlainText("")
        idx = self.ui.comboEmpresa.currentIndex()
        empresa = None
        if idx > 0:
            empresa = self.grids[idx]

        data = self.ui.dateEdit.text()
        import datetime
        data = datetime.datetime.strptime(data, "%d/%m/%Y")
        conn = db.DB(self.cfg.config)
        if conn.conn():
            logger.debug('Conexão feita com sucesso !')
            conn.update(data.__str__(), empresa)
            conn.delete(data.strftime("%Y-%m-%d"), empresa)
            path = os.path.join('C:\\', 'autosystem', 'main.exe')
            os.chdir("C:\\autosystem")

    def print_empresa(self):
        self.log(
            f"GRID : {self.grids[0][self.ui.comboEmpresa.currentIndex()]} Nome : {self.ui.comboEmpresa.currentText()}")

    def set_combo(self):
        if self.cfg.is_config('default'):
            conn = db.DB(self.cfg.config)
            if conn.conn():
                logger.debug('Conexão feita com sucesso !')
                procs = conn.get_empresa()
                self.grids.append(0)
                self.ui.comboEmpresa.addItem("TODAS AS EMPRESAS")
                for proc in procs:
                    empresa = proc['nome']
                    grid = proc['grid']
                    self.grids.append((grid, empresa))
                    self.ui.comboEmpresa.addItem(empresa)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.grids = []
        self.ui = Ui_MainWindow()
        self.cfg = Config()
        self.ui.setupUi(self)
        self.ui.centralwidget.resize(445, 300)
        self.ui.buttonReady.clicked.connect(self.make_actions)
        self.set_combo()
        self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        icon = QIcon(path)
        self.setWindowIcon(icon)
        if not self.cfg.is_config('default'):
            msg = QMessageBox()
            msg.setWindowIcon(icon)
            msg.setWindowTitle("Atenção")
            msg.setText("As configurações não foram encontradas , será aberta uma janela para configurar .")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            ret = msg.exec_()
            if ret == QMessageBox.Ok:
                cfg = ConfigWindow(self)
                cfg.setWindowIcon(icon)
                cfg.exec_()

            self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
