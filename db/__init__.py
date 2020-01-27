import psycopg2
from psycopg2 import extras
from utils.log import logger


class DB:
    def __init__(self, host='localhost', port='5432', user='postgres', password='', dbname='autosystem'):
        self.port = port
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.cur = None


    def conn(self):
        try:
            conn = psycopg2.connect(
                host=self.host, port=self.port, database=self.dbname, user=self.user, password=self.password
            )
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            conn.set_client_encoding('latin1')
            self.cur = cur
            return True
        except Exception as e:
            logger.warning(e)
            return False

    def get_pid(self):
        self.cur.execute("""
        SELECT pl.pid,
               pc.relname,
               psa.query_start,
               psa.client_addr,
               to_char(now() - psa.query_start, 'HH24:MI:SS') AS tempo_bloqueio
        FROM pg_locks pl
        JOIN pg_class pc ON pc.oid=pl.relation
        JOIN pg_stat_activity psa ON psa.pid=pl.pid
        WHERE pl.mode ILIKE '%exclusive%'
        ORDER BY 3;
        """)
        return self.cur.fetchall()

    def get_empresa(self):
        self.cur.execute("""
                SELECT *
                FROM empresa
                WHERE flag = 'A'
                ORDER BY nome;
                """)
        return self.cur.fetchall()

    def delete(self, data_movto, empresa=None):
        query = "delete from "
        msg = ""
        fields = [
            "estoque_lancto",
            "estoque_valor",
            "estoque_deposito"
        ]
        where = f" where data > '{data_movto}'"
        if empresa is not None:
            where += f" and empresa = {empresa[0]}"
            empresa = f"da empresa {empresa[1]}"
        else:
            empresa = "de todas as empresas"
        for f in fields:
            logger.info(f"Apagando {f} {empresa} na data {data_movto}")
            self.cur.execute(f"""
                    {query} {f} {where} ;
                    """)
            logger.info(f"Registros apagados em {f} : {self.cur.rowcount}")

    def update(self, data_movto, empresa=None):
        query = f"update estoque_invalida set data = '{data_movto}' "
        msg = "Atualizando "
        if empresa is not None:
            query += f"where empresa = {empresa[0]}"
            msg += empresa[1]
        else:
            msg += "todas as empresas"
        query += ";"
        logger.info(msg)
        self.cur.execute(query)
        logger.info(f"Registros atualizados : {self.cur.rowcount}")
