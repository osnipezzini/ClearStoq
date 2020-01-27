import json
import os
import sys

from utils.log import logger


def check_version():
    import ftplib

    def getFile(ftp, filename):
        try:
            ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
        except:
            print("Error")

    ftp = ftplib.FTP('ADDRESS')
    ftp.login('USER', 'P@S5')
    ftp.cwd('programas')  # change directory to programas
    getFile(ftp, 'RELEASE')

    ftp.quit()
    with open('RELEASE') as json_file:
        data = json.load(json_file)
    ftp_version = data['nfe_proc']['version']
    import os
    version = os.environ.get('NfeProcVersion')
    os.remove('RELEASE')
    if ftp_version > int(version):
        logger.info('Há uma nova versão disponível no FTP !')
        return True
    return False


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
