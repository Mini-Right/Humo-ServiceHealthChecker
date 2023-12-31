#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/4/18 02:09
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
from SHC.plugins.curd.mysql_curd import HumoTableCreate, HumoTableUpdate, HumoTableRead, HumoTableDelete
from SHC.plugins.session import MySQLSession


class HumoTableCURD(HumoTableCreate, HumoTableUpdate, HumoTableRead, HumoTableDelete):
    def __init__(self, session=MySQLSession.dmg_session):
        super().__init__(session)