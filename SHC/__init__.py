#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/7/26 18:24
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py
# @Software    : PyCharm
# @Description :
import uuid
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from SHC.plugins.logger.request_id import set_request_id, set_request_sub_id
from SHC.plugins.middlewares import middlewares
from root_path import ROOT_PATH

app = FastAPI(
    title='Firefly AI ServiceHealthChecker',
    version='0.0.1',
    docs_url=None,
    redoc_url=None,
)

app.mount(path='/static', app=StaticFiles(directory=f"{ROOT_PATH}/static"), name='static')


@app.get("/api/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Firefly AI 服务监控检查",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url='/static/favicon.jpeg',
    )


middlewares(app)


@app.middleware('http')
async def process_timer(request: Request, call_next):
    request_id = request.headers.get('X-Request-ID') or uuid.uuid4().hex
    request_sub_id = request.headers.get('X-Request-Sub-ID') or ''
    set_request_id(request_id)
    set_request_sub_id(request_sub_id)

    # 计算请求时长
    start_time = datetime.utcnow()
    response = await call_next(request)
    end_time = datetime.utcnow()
    process_time = (end_time - start_time).total_seconds() * 1000

    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Request-ID"] = request_id
    return response
