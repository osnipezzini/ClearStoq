import json
import os
from utils import log

logger = log.logger


class Config:
    def __init__(self):
        self.cfg = 'default'
        self.cfg_file = r'C:\autosystem\blu.conf'
        self.config = None

    def make(self):
        cor_alert = ''
        cor_ok = ''
        print(f"{cor_alert}Configurações não encontradas , favor informar as configurações !")
        host = input(f"{cor_ok}Digite o ip do host ou deixe em branco para localhost : ").strip()
        port = input(f"{cor_ok}Digite a porta do host ou deixe em branco para 5432").strip()
        dbname = input(f"{cor_ok}Digite o nome do banco de dados ou deixe em branco para autosystem").strip()
        user = input(f"{cor_ok}Digite o usuario do banco de dados ou deixe em branco para postgres").strip()
        password = input(f"{cor_ok}Digite a senha do banco de dados : ").strip()
        con_name = 'main'
        if self.cfg != 'main':
            con_name = input(f"{cor_ok}Digite o nome da conexão : ").strip()

        if host == '':
            host = 'localhost'
        if port == '':
            port = '5432'
        if dbname == '':
            dbname = 'autosystem'
        if user == '':
            user = 'postgres'
        conf = self._get()
        config = dict()
        config['host'] = host
        config['port'] = port
        config['dbname'] = dbname
        config['user'] = user
        config['password'] = password
        conf[con_name] = config

        self.set(conf)

    def get(self, name='default'):
        f = self._get()
        self.config = f[name]
        return f[name]

    def _get(self):
        try:
            with open(self.cfg_file) as json_file:
                data = json.load(json_file)
                return data
        except Exception as e:
            logger.warning(f'Ocorreu o seguinte erro ao carregar as configurações : {e}')
            return dict()

    def set(self, cfg):
        try:
            if os.path.exists(self.cfg_file):
                os.remove(self.cfg_file)
            with open(self.cfg_file, 'w') as outfile:
                json.dump(cfg, outfile)
                logger.info('Configurações salvas em : ' + self.cfg_file)
            return True
        except Exception as e:
            logger.info("Erro ao salvar configurações : " + e)
            return False

    def is_config(self, db_conn):
        if os.path.exists(self.cfg_file):
            try:
                ca = self._get()
                if db_conn in ca:
                    return True
                return False
            except Exception as e:
                logger.debug("Configuração não existe", e)
                return False
