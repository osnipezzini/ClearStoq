# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 28 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import gettext

import wx
import wx.adv
import wx.xrc

_ = gettext.gettext


###########################################################################
## Class MainUI
###########################################################################

class MainUI(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=_(u"Clear Stoq"), pos=wx.DefaultPosition,
                          size=wx.Size(640, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, _(u"Data Movto"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        fgSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dateEdit = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                              wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN)
        fgSizer1.Add(self.dateEdit, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, _(u"Empresa"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        fgSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboEmpresaChoices = []
        self.comboEmpresa = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboEmpresaChoices, 0)
        self.comboEmpresa.SetSelection(0)
        fgSizer1.Add(self.comboEmpresa, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(fgSizer1, 0, wx.EXPAND, 5)

        logLayout = wx.BoxSizer(wx.VERTICAL)

        self.textLog = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TE_MULTILINE | wx.TE_READONLY)
        logLayout.Add(self.textLog, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(logLayout, 1, wx.EXPAND, 5)

        buttonBox = wx.StdDialogButtonSizer()
        self.buttonBoxOK = wx.Button(self, wx.ID_OK)
        buttonBox.AddButton(self.buttonBoxOK)
        self.buttonBoxCancel = wx.Button(self, wx.ID_CANCEL)
        buttonBox.AddButton(self.buttonBoxCancel)
        buttonBox.Realize();

        bSizer1.Add(buttonBox, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonBoxCancel.Bind(wx.EVT_BUTTON, self.cancel)
        self.buttonBoxOK.Bind(wx.EVT_BUTTON, self.make_actions)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancel(self, event):
        event.Skip()

    def make_actions(self, event):
        event.Skip()


###########################################################################
## Class ConfigUI
###########################################################################

class ConfigUI(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(u"Configurações do banco de dados"),
                           pos=wx.DefaultPosition, size=wx.Size(422, 200), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, _(u"Host     "), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        fgSizer2.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textHost = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.textHost, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, _(u"Porta"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        fgSizer2.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textPort = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.textPort, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer4.Add(fgSizer2, 0, wx.EXPAND, 5)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.AddGrowableCol(1)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, _(u"Usuário"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        fgSizer4.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textUser = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer4.Add(self.textUser, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, _(u"Senha"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        fgSizer4.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textPassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PASSWORD)
        fgSizer4.Add(self.textPassword, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, _(u"Nome"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        fgSizer4.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.textName = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer4.Add(self.textName, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(fgSizer4, 1, wx.EXPAND, 5)

        buttonBox = wx.StdDialogButtonSizer()
        self.buttonBoxSave = wx.Button(self, wx.ID_SAVE)
        buttonBox.AddButton(self.buttonBoxSave)
        self.buttonBoxCancel = wx.Button(self, wx.ID_CANCEL)
        buttonBox.AddButton(self.buttonBoxCancel)
        buttonBox.Realize();

        bSizer4.Add(buttonBox, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonBoxCancel.Bind(wx.EVT_BUTTON, self.cancel)
        self.buttonBoxSave.Bind(wx.EVT_BUTTON, self.accept)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancel(self, event):
        event.Skip()

    def accept(self, event):
        event.Skip()
