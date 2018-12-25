#!/usr/bin/env python
# -*- coding=UTF-8 -*-

import base64
import jsonpath
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = "15123439"
API_KEY = "cwSaqMSrNSlu92KfMNT4ZjGv"
SECRET_KEY = "U3V06Me8ytIlYLZAiPduG9eIVIE3UoB0"

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



def get_baidu_api(image,word):
    """ 如果有可选参数 """

    img = base64.b64decode(image)

    with open("test1.jpg","wb") as f:
        f.write(img)
    image = get_file_content("./test1.jpg")

    options = {}
    options["recognize_granularity"] = "small"
    options["detect_direction"] = "true"
    options["vertexes_location"] = "true"
    options["probability"] = "true"
    """ 带参数调用通用文字识别（含位置高精度版） """
    response = client.accurate(image, options)
    # response = client.general(image, options)
    print("要匹配的值为:"+word)
    try:
        result = jsonpath.jsonpath(response, "$..chars")
        for each in result:
            for i in each:
                char = i.get("char")
                if char == word:
                    location = i.get("location")
                    x = location.get("left")
                    y = location.get("top")
                    return x,y
    except Exception as e:
        print(e)

def get_word():

    options = {}

    options["detect_direction"] = "true"
    image = get_file_content("./4SUC6G.jpg")
    response = client.basicAccurate(image, options)
    print(response)


if __name__ == '__main__':
    get_word()