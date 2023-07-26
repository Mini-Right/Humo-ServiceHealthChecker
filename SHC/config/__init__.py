#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/6/5 15:33
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
import os
from pathlib import Path
from typing import Optional

import yaml

from SHC.config.config_schemas import ConfigSchema
from SHC.plugins.logger import logger

BASE_DIR = Path(__file__).resolve().parent.parent


class Singleton:
    _instance: Optional[ConfigSchema] = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            env = os.environ.get('ENVIRONMENT')
            # 开发环境处理
            if env is None or env == 'dev':
                env = 'dev'
            logger.info(f"启动环境: {env}")
            with open(f'{BASE_DIR}/config/{env}.yaml', 'r', encoding='utf-8') as f:
                database_config: dict = yaml.safe_load(f)
            cls._instance = ConfigSchema(**database_config)
        return cls._instance


def dmg_config() -> ConfigSchema:
    return Singleton.get_instance()


config: ConfigSchema = dmg_config()


if __name__ == '__main__':
    print(config)