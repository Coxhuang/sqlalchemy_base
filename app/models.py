# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/29 1:01 PM
@Auth ： Minhang
@File ： models.py
@IDE  ： PyCharm
"""
from sqlalchemy import Column, Integer, String, VARCHAR,DateTime,FLOAT, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class T_CRANE_INFO_4V(Base):
    __tablename__ = 'T_CRANE_INFO_4V'

    ID = Column(Integer, primary_key=True)
    CRANE_ID = Column(VARCHAR(4))
    LANE_NO = Column(VARCHAR(4))
    BAY1 = Column(VARCHAR(4))
    BAY2 = Column(VARCHAR(4))
    BAY3 = Column(VARCHAR(4))
    VESSEL_DIRECTION = Column(VARCHAR(1))
    BERTH = Column(VARCHAR(3))
    INSERT_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)


class T_WI_INFO_4V_TOS(Base):
    __tablename__ = 'T_WI_INFO_4V_TOS'

    ID = Column(Integer, primary_key=True)
    TRUCK_NO = Column(VARCHAR(12))
    WI_NO = Column(Integer)
    CTN_NO = Column(VARCHAR(12))
    CTN_WEIGHT = Column(Integer)
    FROM_POS = Column(VARCHAR(12))
    TO_POS = Column(VARCHAR(12))
    WI_TYPE = Column(VARCHAR(4))
    WI_ACT = Column(VARCHAR(12))
    WI_STATUS = Column(VARCHAR(12))
    TWIN_FLAG = Column(VARCHAR(1))
    DISPATCH_TIME = Column(DateTime)
    CANCEL_TIME = Column(DateTime)
    CONFIRMED_TIME = Column(DateTime)
    REMARK1 = Column(VARCHAR(12))
    REMARK2 = Column(VARCHAR(12))
    REMARK3 = Column(VARCHAR(12))
    INSERT_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    TWIN_WI_NO = Column(Integer)
    TWIN_CTN_NO = Column(VARCHAR(12))
    TRUCK_POS = Column(VARCHAR(1))
    EQUIT_TYPE = Column(VARCHAR(4))
    TEU = Column(Integer)
    TRUCK_SEQ = Column(Integer)
    VERSION = Column(Integer)


# tables needs update
class T_TRUCK_INFO_4V(Base):
    __tablename__ = 'T_TRUCK_INFO_4V'
    ID = Column(Integer, primary_key=True)
    TRUCK_NO = Column(VARCHAR(12))
    POS_X = Column(FLOAT)
    POS_Y = Column(FLOAT)
    CUR_POS = Column(VARCHAR(12))
    POWER_TYPE = Column(VARCHAR(12))
    REST_OIL = Column(FLOAT)
    REST_ELECTRIC = Column(FLOAT)
    SPEED = Column(FLOAT)
    SENSOR_STATUS = Column(VARCHAR(1))
    INSERT_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    TRUCK_MODE = Column(Integer)
    CUR_WIS = Column(VARCHAR(50))


class T_WI_INFO_4V_DC(Base):
    __tablename__ = 'T_WI_INFO_4V_DC'

    ID = Column(Integer, primary_key=True)
    TRUCK_NO = Column(VARCHAR(4))
    WI_NO = Column(Integer)
    CTN_NO = Column(Integer)
    CNT_WEIGHT = Column(Integer)
    FROM_POS = Column(VARCHAR(12))
    TO_POS = Column(VARCHAR(12))
    TOS_WI_NO = Column(Integer)
    TOS_WI_ACT = Column(VARCHAR(12))
    TOS_WI_TYPE = Column(VARCHAR(4))
    REMARK1 = Column(VARCHAR(12))
    REMARK2 = Column(VARCHAR(12))
    REMARK3 = Column(VARCHAR(12))
    TRUCK_STATUS = Column(VARCHAR(12))
    TWIN_FLAG = Column(VARCHAR(1))
    START_TIME = Column(DateTime)
    EST_TIM = Column(DateTime)
    ARRIVE_TIME = Column(DateTime)
    FINISH_TIME = Column(DateTime)
    INSERT_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    TWIN_WI_NO = Column(Integer)
    TWIN_CTN_NO = Column(VARCHAR(12))
    TRUCK_POS = Column(VARCHAR(1))
    VERSION = Column(Integer)





if __name__ == '__main__':
    engine = create_engine('oracle://cox:cox123456@127.0.0.1:49161/XE', echo=True)
    Database = sessionmaker(bind=engine)

    # 把当前的引擎绑定给这个会话
    Session = sessionmaker(bind=engine)

    # 实例化
    session = Session()
    Base.metadata.create_all(engine)



