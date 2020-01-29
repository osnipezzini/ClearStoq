import os
import sys

import wx

import db
from config import Config
from gui.main_ui import ConfigUI, MainUI
from utils import resource_path
from utils.log import log as logger

path = resource_path("Icon.ico")


class ConfigWindow(ConfigUI):
    def __init__(self, parent):
        super(ConfigWindow, self).__init__(parent)
        self.parent = parent
        self.config = dict()
        cfg = Config()
        self.exit = True
        if cfg.is_config('default'):
            self.config = cfg.get('default')
            self.dict2field(self.config)

    def accept(self, event):
        cfg = self.field2dict()
        self.config['default'] = cfg
        self.save()

    def save(self):
        cfg = Config()
        conn = db.DB(**self.config['default'])
        if conn.conn():
            if cfg.set(self.config):
                msg = wx.MessageBox(
                    "As configurações foram salvas em : " + cfg.cfg_file,
                    caption="Sucesso", style=wx.OK | wx.CENTRE | wx.ICON_INFORMATION, parent=None,
                )
                if msg == wx.OK:
                    self.EndModal(wx.OK)
            else:
                wx.MessageBox(
                    "Ocorreu um erro ao salvar as configurações , verificar se o arquivo " +
                    cfg.cfg_file + " não está sendo usado e se você tem permissão de escrita !",
                    caption="Erro", style=wx.OK | wx.CENTRE | wx.ICON_ERROR, parent=None,
                )
        else:
            wx.MessageBox(
                "Ocorreu um erro ao conectar ao banco de dados, verifique os dados informados e tente novamente !",
                caption="Erro", style=wx.OK | wx.CENTRE | wx.ICON_WARNING, parent=None,
            )

    def dict2field(self, cfg):
        self.textHost.setText(cfg["host"])
        self.textPort.setText(cfg["port"])
        self.textUser.setText(cfg["user"])
        self.textPassword.setText(cfg["password"])
        self.textName.setText(cfg["dbname"])

    def validate_fields(self):
        self.textHost.SetValue("localhost" if self.textHost.GetValue() == "" else self.textHost.GetValue())
        self.textPort.SetValue("5432" if self.textPort.GetValue() == "" else self.textPort.GetValue())
        self.textName.SetValue("autosystem" if self.textName.GetValue() == "" else self.textName.GetValue())
        self.textUser.SetValue("postgres" if self.textUser.GetValue() == "" else self.textUser.GetValue())

    def field2dict(self):
        self.validate_fields()
        cfg = dict()
        cfg["host"] = self.textHost.GetValue()
        cfg["port"] = self.textPort.GetValue()
        cfg["dbname"] = self.textName.GetValue()
        cfg["user"] = self.textUser.GetValue()
        cfg["password"] = self.textPassword.GetValue()
        return cfg

    def reset(self):
        self.textHost.SetValue("")
        self.textPort.SetValue("")
        self.textUser.SetValue("")
        self.textPassword.SetValue("")
        self.textName.SetValue("")

    def cancel(self, event):
        sys.exit()


class MainWindow(MainUI):

    def log(self, text):
        logger(text, self.textLog)

    def make_actions(self, event):
        self.textLog.AppendText("")
        idx = self.comboEmpresa.CurrentSelection
        empresa = None
        if idx > 0:
            empresa = self.grids[idx]

        data = self.dateEdit.GetValue()
        conn = db.DB(**self.cfg, text_ctrl=self.textLog)
        if conn.conn():
            self.log('Conexão feita com sucesso !')
            conn.update(data.__str__(), empresa)
            conn.delete(data.Format("%Y-%m-%d"), empresa)
            path = os.path.join('C:\\', 'autosystem', 'main.exe')
            os.chdir("C:\\autosystem")
            os.spawnl(os.P_NOWAIT, path, '--estoque')

    def print_empresa(self):
        self.log(
            f"GRID : {self.grids[0][self.comboEmpresa.currentIndex()]} Nome : {self.comboEmpresa.currentText()}")

    def set_combo(self):
        conn = db.DB(**self.cfg, text_ctrl=self.textLog)
        if conn.conn():
            self.log('Conexão feita com sucesso !')
            procs = conn.get_empresa()
            self.grids.append(0)
            self.comboEmpresa.Append("TODAS AS EMPRESAS")
            for proc in procs:
                empresa = proc['nome']
                grid = proc['grid']
                self.grids.append((grid, empresa))
                self.comboEmpresa.Append(empresa)

    def __init__(self, parent, cfg):
        super(MainWindow, self).__init__(parent)
        self.grids = []
        self.cfg = cfg
        self.set_combo()
        self.dateEdit.SetValue(wx.DateTime.Today())
        self.SetIcon(icon)


def run():
    cfg = Config()
    if not cfg.is_config('default'):
        msg = wx.MessageBox(
            "As configurações não foram encontradas , será aberta uma janela para configurar.",
            caption="Aviso", style=wx.OK | wx.CENTRE | wx.ICON_ERROR, parent=None,
        )

        if msg == wx.OK:
            cfg = ConfigWindow(None)
            cfg.SetIcon(icon)
            if cfg.ShowModal() == wx.OK:
                run()

    else:
        cfg.config = cfg.get('default')
        window = MainWindow(None, cfg.config)
        window.Show()


if __name__ == "__main__":
    app = wx.App()
    icon = wx.Icon(path)

    run()

    app.MainLoop()
