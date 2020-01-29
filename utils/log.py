import logging
import os


def log(text, text_ctrl=None):
    if text_ctrl is not None:
        _log = text_ctrl
        import datetime
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        _log.WriteText(f"{now} | INFO : {text}\n")
    logger.info(text)


class RedirectText(object):
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        import datetime
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.out.WriteText(f"{now} | ClearStoq | INFO : {string}")


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
