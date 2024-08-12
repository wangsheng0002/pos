from datetime import datetime

import requests
import config.config_1

import logging


def logs(info,data):
    # 基本配置
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 创建logger
    logger = logging.getLogger(info)
    logger.setLevel(logging.DEBUG)

    # 创建文件handler，用于写入日志文件
    fh = logging.FileHandler("../log/输出日志"+datetime.now().strftime("%Y-%m-%d")+".log")
    fh.setLevel(logging.DEBUG)

    # 再创建一个handler，用于将日志输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 记录一些日志

    logger.info(data)




if __name__ == '__main__':
    logs("日志记录","test123")
    pass