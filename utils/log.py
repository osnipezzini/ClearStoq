import logging
import os

from PySide2 import QtWidgets


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


logger = logging.getLogger('Check Estoque')
handler = logging.StreamHandler()
file_handler = logging.FileHandler(
    os.environ.get("LOGFILE", r"C:\\autosystem\\log\\check_stoq.log"))
formatter = logging.Formatter(
    '%(asctime)s | %(name)-12s | %(levelname)-2s : %(message)s', "%d/%m/%Y %H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(file_handler)
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
