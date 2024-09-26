import mysql.connector

print(2)

class MysqlConnector:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(host = self.host,user = self.user,password = self.password,database = self.database)
        self.cursor = self.conn.cursor()

    def execute_query(self,sql_query):
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()


