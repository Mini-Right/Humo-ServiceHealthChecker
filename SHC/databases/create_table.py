#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/6/12 17:57
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : create_table.py
# @Software    : PyCharm
# @Description :
from SHC.databases.shc_service_config_table import Base

if __name__ == "__main__":
    from urllib import parse

    from sqlalchemy import create_engine

    from SHC.config import config

    DB = config.DB.DMG.dict()
    print(DB)
    engine = create_engine(
        f"mysql+pymysql://{DB.get('user')}:{parse.quote_plus(DB.get('password'))}@{DB.get('host')}:{DB.get('port')}/{DB.get('database')}?charset=utf8mb4",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1,  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)
