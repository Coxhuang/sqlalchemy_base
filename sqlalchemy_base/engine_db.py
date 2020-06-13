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

engine = create_engine(
    "{}://{}:{}@{}:{}/{}".format(
        data_obj.db_type,
        data_obj.db_username,
        data_obj.db_password,
        data_obj.db_host,
        data_obj.db_port,
        data_obj.db_name,
    ),
    echo=True,
    max_overflow=5)

# 把当前的引擎绑定给这个会话
Session = sessionmaker(bind=engine)
# 实例化
session = Session()