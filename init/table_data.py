#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/7/26 19:10
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : table_data.py
# @Software    : PyCharm
# @Description :
import json

from SHC.databases.shc_service_config_table import SHCServiceConfigTable, SHCServiceAPIAssertConfigTable, SHCServiceAPIConfigTable
from SHC.plugins.curd import HumoTableCURD


def service_config():
    service_config_list = [
        {
            'service_name': '[测试] - Apifox Echo',
            'service_domain': 'https://echo.apifox.com',
        }
    ]

    HumoTableCURD().add_list(
        table_class_list=[
            SHCServiceConfigTable(**_)
            for _ in service_config_list
        ]
    )


def api_config():
    api_config_list = [
        {
            'service_id': '760bb934d0554f50838df0736b24f79f',
            'api_name': '使用Query参数',
            'api_method': 'GET',
            'api_path': '/get',
            'api_body_type': 'params',
            'api_body': json.dumps({
                'q1': 'v1',
                'q2': 'v2',
            })
        },
        {
            'service_id': '760bb934d0554f50838df0736b24f79f',
            'api_name': '使用POST参数',
            'api_method': 'POST',
            'api_path': '/post?q1=v1&q2=v2',
            'api_body_type': 'form-data',
            'api_body': json.dumps(
                {
                    "d": "deserunt",
                    "dd": "adipisicing enim deserunt Duis"
                }
            ),
            'api_headers': None,
        },
        {
            'service_id': '760bb934d0554f50838df0736b24f79f',
            'api_name': '使用DELETE参数',
            'api_method': 'DELETE',
            'api_path': '/delete?q1=v1',
            'api_body_type': 'form-data',
            'api_body': json.dumps({
                'q1': 'v1',
                'q2': 'v2',
            })
        },
        {
            'service_id': '760bb934d0554f50838df0736b24f79f',
            'api_name': '使用PUT参数',
            'api_method': 'PUT',
            'api_path': '/put?q1=v1',
            'api_body_type': 'raw',
            'api_body': 'test value'
        },
        {
            'service_id': '760bb934d0554f50838df0736b24f79f',
            'api_name': '使用patch参数',
            'api_method': 'PATCH',
            'api_path': '/patch?q1=v1',
            'api_body_type': 'json',
            'api_body': json.dumps(
                {
                    "b1": "adipisicing",
                    "b2": "officia quis magna"
                }
            )
        },
    ]

    HumoTableCURD().add_list(
        table_class_list=[
            SHCServiceAPIConfigTable(**_)
            for _ in api_config_list
        ]
    )


def assert_config():
    assert_config_list = [
        {
            'api_id': '72885729194b4da3a7a318918b1b4808',
            'http_status_code': 200,
            'response_status_field': 'code',
            'response_status_code_type': 'int',
            'response_status_code': '200',
            'response_time': '300',
        },
        {
            'api_id': '1223446b1d2b4807846bbaa442577bcf',
            'http_status_code': 200,
            'response_status_field': 'code',
            'response_status_code_type': 'int',
            'response_status_code': '200',
            'response_time': '300',
        },
        {
            'api_id': '8b23c404e2424ba98629c6c258a71e01',
            'http_status_code': 200,
            'response_status_field': 'code',
            'response_status_code_type': 'int',
            'response_status_code': '200',
            'response_time': '300',
        }
    ]

    HumoTableCURD().add_list(
        table_class_list=[
            SHCServiceAPIAssertConfigTable(**_)
            for _ in assert_config_list
        ]
    )

if __name__ == '__main__':
    api_config()