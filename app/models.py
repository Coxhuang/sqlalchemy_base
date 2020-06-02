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

class T_CRANE_INFO_4V_Model(Base):

    __tablename__ = 'T_CRANE_INFO_4V'
    ID = Column(Integer, primary_key=True, autoincrement = True)
    CRANE_ID = Column(String(12))
    LANE_NO = Column(String(2))
    INSERT_TIME = Column(String(16))
    UPDATE_TIME = Column(String(16))
    BAY1 = Column(String(16))
    BAY2 = Column(String(16))
    BAY3 = Column(String(16))
    VESSEL_DIRECTION = Column(String(16))
    BERTH = Column(String(16))




if __name__ == '__main__':
    # engine = create_engine("dialect+driver://username:password@host:port/database")
    engine = create_engine('oracle://cox:cox123456@127.0.0.1:49161/XE', echo=True)
    Database = sessionmaker(bind=engine)

    # 把当前的引擎绑定给这个会话
    Session = sessionmaker(bind=engine)

    # 实例化
    session = Session()
    # db = Database()
    # query = db.query(Teacher)
    # print(query)
    # session.add(Teacher(name='shark2',
    #                     age='18',
    #                     city='ZhengZhou'))
    # session.commit()
    Base.metadata.create_all(engine)



