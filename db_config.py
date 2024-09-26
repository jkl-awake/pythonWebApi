import json
from marshmallow import Schema, fields, post_load

print(1)

class DbConfig:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

# 使用第三方库将json字典转换成对象
class DbConfigSchema(Schema):
    host = fields.Str()
    user = fields.Str()
    password = fields.Str()
    database = fields.Str()

    @post_load
    def make(self,data,**kwargs):
        return DbConfig(**data)

# 读取配置文件转换成json字典
def get_connection_json():
    with open('appsettions.json') as f:
        config_json = json.load(f)
    return config_json

def get_db_config():
    db_config_json = get_connection_json()
    # 转换成对象的具体实现方法
    config = DbConfigSchema().load(db_config_json['SkuDbConnection'])
    return config