#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/7/26 19:20
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : check.py
# @Software    : PyCharm
# @Description :
import json
import ssl
from asyncio import gather
from enum import Enum

import aiohttp as aiohttp
from aiohttp import ClientSession

from SHC.databases.shc_service_config_table import SHCServiceConfigTable, SHCServiceAPIConfigTable
from SHC.plugins.curd import HumoTableCURD


class RequestMethodEnum(Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'
    PATCH = 'PATCH'


class RequestBodyTypeEnum(Enum):
    NONE = 'NONE'
    X_WWW_FORM_URLENCODED = 'X_WWW_FORM_URLENCODED'
    PARAMS = 'PARAMS'
    FORM_DATA = 'FORM-DATA'
    RAW = 'RAW'
    JSON = 'JSON'
    XML = 'XML'


class SHCCheckService(object):

    async def main(self):
        table_curd = HumoTableCURD()
        service_list = table_curd.query_table_all(table_class=SHCServiceConfigTable)
        print(service_list)

        service_api_list = table_curd.query_table_all(
            table_class=SHCServiceAPIConfigTable,
            params=[SHCServiceConfigTable.id == SHCServiceAPIConfigTable.service_id]
        )

        sslcontext = ssl.create_default_context()
        sslcontext.check_hostname = False
        sslcontext.verify_mode = ssl.CERT_NONE
        conn = aiohttp.TCPConnector(ssl=sslcontext)
        async with aiohttp.ClientSession(connector=conn) as session:
            for service in service_list:
                tasks = []
                for service_api in filter(lambda x: x.service_id == service.id, service_api_list):
                    request_info = self.assembly_request_data(service, service_api)
                    tasks.append(self.invoke(session, request_info))
                await gather(*tasks)

    async def invoke(self, session, request_info: dict):
        print(f"{request_info=}")
        response_text, status_code = await self.fetch(
            session=session,
            url=request_info.get('url'),
            method=request_info.get('method'),
            headers=request_info.get('headers'),
            api_body_type=request_info.get('body_type'),
            body=request_info.get('body')
        )
        print(request_info.get('service_name'), request_info.get('api_name'), status_code, json.loads(response_text))

    async def fetch(self, session: ClientSession, url: str, method: str, headers: dict, api_body_type: str, body):
        api_body = self.handle_api_body(api_body_type=api_body_type, api_body=body)
        method = method.upper()
        if method in RequestMethodEnum._value2member_map_:
            func = getattr(session, method.lower(), None)
            if func:
                async with func(url, headers=headers, **api_body) as response:
                    return await response.text(), response.status
            else:
                raise ValueError(f'错误的Method: {method}')

    @staticmethod
    def handle_api_body(api_body_type: str, api_body):
        api_body_type = api_body_type.upper()

        def handle_json(api_body):
            return {'json': json.loads(api_body)}

        def handle_data(api_body):
            return {'data': api_body}

        def handle_params(api_body):
            return {'params': json.loads(api_body)}

        def handle_unimplemented(api_body):
            # TODO x-www-form-urlencoded 实现
            return {}

        handlers = {
            RequestBodyTypeEnum.NONE.value: lambda x: {},
            RequestBodyTypeEnum.PARAMS.value: handle_params,
            RequestBodyTypeEnum.FORM_DATA.value: handle_data,
            RequestBodyTypeEnum.RAW.value: handle_data,
            RequestBodyTypeEnum.JSON.value: handle_json,
            RequestBodyTypeEnum.XML.value: handle_data,
            RequestBodyTypeEnum.X_WWW_FORM_URLENCODED.value: handle_unimplemented,
        }

        if api_body is None or api_body_type not in handlers:
            return {}
        return handlers[api_body_type](api_body)

    @staticmethod
    def assembly_request_data(service_info: SHCServiceConfigTable, service_api_info: SHCServiceAPIConfigTable):
        def load_headers(header_str):
            return json.loads(header_str) if header_str is not None else {}

        headers = {**load_headers(service_info.service_headers), **load_headers(service_api_info.api_headers)}

        request_info = {
            'service_name': service_info.service_name,
            'api_name': service_api_info.api_name,
            'url': f"{service_info.service_domain}{service_api_info.api_path or ''}",
            'method': service_api_info.api_method,
            'headers': headers,
            'body': service_api_info.api_body,
            'body_type': service_api_info.api_body_type,
        }
        return request_info


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(SHCCheckService().main())
