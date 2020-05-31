# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/29 1:43 PM
@Auth ： Minhang
@File ： data.py
@IDE  ： PyCharm
"""

from sqlalchemy_base import settings
from config import MysqlEnum, OracleEnum

class DataBase(object):

    def __init__(self):
        # engine = create_engine('oracle://username:password@192.168.1.6:1521/databasename', echo=True)
        # engine = create_engine("mysql+pymysql://root:123@172.16.153.160:3306/dbname?charset=utf8mb4",echo=True,max_overflow=5)
        # "oracle+cx_Oracle://USER:PASSWD@HOST:PORT/SID"
        if settings.DB_TYPE == "mysql":
            self.db_type = "mysql+pymysql"
            self.db_username = MysqlEnum.USERNAME.value
            self.db_password = MysqlEnum.PASSWORD.value
            self.db_host = MysqlEnum.HOST.value
            self.db_port = MysqlEnum.PORT.value
            self.db_name = MysqlEnum.NAME.value
        else:
            self.db_type = "oracle"
            self.db_username = OracleEnum.USERNAME.value
            self.db_password = OracleEnum.PASSWORD.value
            self.db_host = OracleEnum.HOST.value
            self.db_port = OracleEnum.PORT.value
            self.db_name = OracleEnum.NAME.value


data_obj = DataBase()