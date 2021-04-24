#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import base64
import time
import platform

# 如果想要在浏览器上访问base64格式图片，需要在前面加上：data:image/jpeg;base64


def encode_base64(file):
    with open(file, 'rb') as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        print(type(base64_data))
        base64_str = str(base64_data, 'utf-8')
        print(base64_str)
        return base64_data


def decode_base64(base64_data):
    ticks = time.time()
    with open('./images/' + str(ticks) + '.jpg', 'wb') as f:
        img = base64.b64decode(base64_data)
        f.write(img)


def read_img(file_url):
    with open(file_url, 'r') as f:
        file_data = f.read()
        return file_data.replace('data:image/png;base64,', '')


def showinfo(tip, info):
    print("{}:{}".format(tip, info))

def printosinfo():
    showinfo("操作系统及版本信息", platform.platform())
    showinfo('获取系统版本号', platform.version())
    showinfo('获取系统名称', platform.system())
    showinfo('系统位数', platform.architecture())
    showinfo('计算机类型', platform.machine())
    showinfo('计算机名称', platform.node())
    showinfo('处理器类型', platform.processor())
    showinfo('计算机相关信息', platform.uname())
