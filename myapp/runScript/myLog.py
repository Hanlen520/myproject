# encoding:utf-8
import sys
import logging
import time
import datetime


def writeLog(message):
    logger = logging.getLogger()
    filename = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    handler = logging.FileHandler("./log/" + filename + ".log")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.info(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ':' + message)

    #  添加下面一句，在记录日志之后移除句柄
    logger.removeHandler(handler)


if __name__ == '__main__':
    writeLog("hello")
