import psycopg2 as db
from Env_Vars import Env_Vars



class Configs:
    def __init__(self):
        dbs = Env_Vars()
        self.config = dbs.DB_MK

class Connection(Configs):
    def __init__(self):
        Configs.__init__(self)
        try:
            self.conn = db.connect(**self.config['postgres'])
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Ocorreu um erro na conexão: ', e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    
    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        return self.connetion.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql):
        self.cursor.execute(str(sql))
        return self.fetchall()

class Person(Connection):
    def __init__(self):
        Connection.__init__(self)
