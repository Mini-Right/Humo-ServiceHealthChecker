#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/7/26 18:23
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : main.py
# @Software    : PyCharm
# @Description :
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        'SHC:app',
        host="0.0.0.0",
        port=5002,
        workers=1
    )
