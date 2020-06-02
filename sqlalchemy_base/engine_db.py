# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/29 1:36 PM
@Auth ： Minhang
@File ： engine_db.py
@IDE  ： PyCharm
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_base.data import data_obj

# engine = create_engine('oracle://username:password@192.168.1.6:1521/databasename', echo=True)
# engine = create_engine("mysql+pymysql://root:123@172.16.153.160:3306/dbname?charset=utf8mb4",echo=True,max_overflow=5)

engine = create_engine(
    "{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(
        data_obj.db_type,
        data_obj.db_username,
        data_obj.db_password,
        data_obj.db_host,
        data_obj.db_port,
        data_obj.db_name,
    ),
    echo=True,
    max_overflow=5)

# engine = create_engine("oracle://TEST:TEST123@127.0.0.1:49161/TEST")
# engine = create_engine("oracle://system:oracle@127.0.0.1/TEST",encoding='utf-8', echo=True)
# engine = create_engine('oracle://TEST:TEST123@127.0.0.1:1521/TEST', echo=True)



# 把当前的引擎绑定给这个会话
Session = sessionmaker(bind=engine)

# 实例化
session = Session()