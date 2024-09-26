from mysql_connector import MysqlConnector
from db_config import get_db_config

class SearchData:
    def __init__(self):
        self.connector = None

    def set_connector(self):
        # 读取配置文件并转换成对象
        db_object = get_db_config()
        # 创建数据库实例
        self.connector = MysqlConnector(host=db_object.host, user=db_object.user, password=db_object.password,
                                   database=db_object.database)
        #注入对象
        self.connector.connect()
        return self.connector

    def get_number(self):
        self.connector = self.set_connector()
        # 语句
        query = "select count(1) as total from wsproduct where deleteStatus = 1"
        result = self.connector.execute_query(query)
        # 关闭连接
        self.connector.close()
        # 这里的结果是固定的
        return result[0][0]



