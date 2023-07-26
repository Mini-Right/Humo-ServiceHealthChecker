#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/7/26 18:36
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : shc_service_config_table.py
# @Software    : PyCharm
# @Description :
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import LONGTEXT, INTEGER

from SHC.databases import Base


class SHCServiceConfigTable(Base):
    __tablename__ = "shc_service_config"
    __table_args__ = ({'comment': '服务配置'})
    service_name = Column(String(50), nullable=False, comment='服务名称')
    service_domain = Column(LONGTEXT, nullable=False, comment='服务完整域名 例:  https://aaa.bb.cc')
    service_headers = Column(LONGTEXT, comment='请求头')


class SHCServiceAPIConfigTable(Base):
    __tablename__ = "shc_service_api_config"
    __table_args__ = ({'comment': '服务API配置'})
    service_id = Column(String(50), nullable=False, comment='服务id')
    api_name = Column(String(50), nullable=False, comment='接口名称')
    api_method = Column(String(50), nullable=False, comment='接口请求方式')
    api_path = Column(LONGTEXT, comment='接口路径')
    api_body_type = Column(String(50), nullable=False, default='none', comment='接口请求报文类型 params/none/form-data/x-www-form-urlencoded/json/xml/raw')
    api_body = Column(LONGTEXT, comment='接口请求报文')
    api_headers = Column(LONGTEXT, comment='接口请求头')


class SHCServiceAPIAssertConfigTable(Base):
    __tablename__ = "shc_service_api_assert_config"
    __table_args__ = ({'comment': '服务API断言配置'})
    api_id = Column(String(50), nullable=False, comment='接口id')
    http_status_code = Column(INTEGER, comment='http status code')
    response_status_field = Column(String(50), comment='响应状态字段')
    response_status_code_type = Column(String(50), comment='响应状态值类型  string int')
    response_status_code = Column(String(50), comment='响应状态值')
    response_time = Column(INTEGER, comment='接口耗时 毫秒')
