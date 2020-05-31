# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/29 1:01 PM
@Auth ： Minhang
@File ： models.py
@IDE  ： PyCharm
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    name = Column(String(12))
    age = Column(String(2))
    city = Column(String(16))

# Base.metadata.create_all(engine)
# engine = create_engine('oracle://system:oracle@192.168.3.195:1521/TEST', echo=True)
engine = create_engine("oracle://scott:tiger@192.168.3.195:1521/XE")
Database= sessionmaker(bind=engine)

# 把当前的引擎绑定给这个会话
Session = sessionmaker(bind=engine)

# 实例化
session = Session()


if __name__ == '__main__':
    # db = Database()
    # query = db.query(Teacher)
    # print(query)
    # session.add(Teacher(name='shark2',
    #                     age='18',
    #                     city='ZhengZhou'))
    # session.commit()
    Base.metadata.create_all(engine)



