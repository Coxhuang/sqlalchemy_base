# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/29 11:42 AM
@Auth ： Minhang
@File ： main.py
@IDE  ： PyCharm
"""
from app.models import Base
from sqlalchemy_base.engine_db import engine, session
from app.models import Teacher

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session.add(Teacher(name='shark2',
                        age='18',
                        city='ZhengZhou'))
    session.commit()


