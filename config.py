# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/29 11:42 AM
@Auth ： Minhang
@File ： config.py
@IDE  ： PyCharm
"""

from enum import Enum

class EnumBase(Enum):
    pass

class MysqlEnum(EnumBase):

    NAME = "oracle_sd"
    USERNAME = "root"
    PASSWORD = "root"
    HOST = "127.0.0.1"
    PORT = 3306

class OracleEnum(EnumBase):

    NAME = "XE"
    USERNAME = "cox"
    PASSWORD = "cox123456"
    HOST = "127.0.0.1"
    PORT = 49161
