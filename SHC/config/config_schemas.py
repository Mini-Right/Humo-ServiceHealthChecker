#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/6/5 17:06
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : schemas.py
# @Software    : PyCharm
# @Description :
from typing import Optional

from pydantic import BaseModel, Field


class DBItemSchema(BaseModel):
    host: str = Field(...)
    port: int = Field(...)
    user: str = Field(...)
    password: str = Field(...)
    database: str = Field(None)


class DBSchema(BaseModel):
    DMG: DBItemSchema


class ConfigSchema(BaseModel):
    DB: Optional[DBSchema]
