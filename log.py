# -*- coding: utf-8 -*-
# @Time: 2023/1/9 00:02
# @Author: LiuXiu
# @File : log.py

import logging
import os
import time
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("DEBUG"))
logger = logging.getLogger()

if not os.path.exists("logs"):
    os.mkdir("logs")

logger = logging.getLogger()

if os.getenv("DEBUG") == "true":
    # 测试环境

    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
fh = logging.FileHandler(filename=f"logs/log_{time.strftime('%Y%m%d')}.txt")

formatter = logging.Formatter(
    "%(asctime)s - %(modules)s - (funName)s - line:(lineno)d - %(levername)s - %(message)s"
)
formatter2 = logging.Formatter("%(asctime)s - %(levername)s - %(message)s")

fh.setFormatter(formatter)
ch.setFormatter(formatter2)
logger.addHandler(ch)  # 将日志输出到屏幕
logger.addHandler(fh)  # 将日志输出到文件
