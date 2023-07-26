#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/4/18 02:05
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
from SHC.config import config
from SHC.plugins.session._mysql import MySQLSessionGenerate


class MySQLSession(object):
    dmg_session = MySQLSessionGenerate(config.DB.DMG).session
