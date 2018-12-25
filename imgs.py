#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import time

import requests
from api_sdk import *

def get_captcha_image():

    url = "http://www.miitbeian.gov.cn/getVerifyCode?70"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Cookie": "__jsluid=6bb1c0b8a4eec4de11a908f4447310aa; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1545719668; Hm_lpvt_d7682ab43891c68a00de46e9ce5b76aa=1545719668; JSESSIONID=iWLkKGA9GAOB0TM_3EeomiGbTWBc26vUd1Ai0BpskTc8JjZkGC9f!2144121308; __jsl_clearance=1545724394.449|0|qchHtV8Lfj5Gk3Oho8oH5FD4YrA%3D",
        "Host": "www.miitbeian.gov.cn",
        "Pragma": "no-cache",
        "Proxy-Authorization": "Basic Y2o3MTdrOmNqNzE3aw==",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://www.miitbeian.gov.cn/icp/publish/query/icpMemoInfo_showPage.action",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    }

    for i in range(999,2000):

        proxies = {'http': 'http://cj717k:cj717k@123.249.76.202:888'}

        response = requests.get(url, headers=headers, proxies=proxies)

        status = response.status_code
        print(status)
        if status == 200:
            with open("./word_num_captcha/{}.jpg".format(i),"wb") as f:
                f.write(response.content)
            print("----抓取数量:{}".format(i))
        else:
            break
        time.sleep(5)


def get_captcha_result():
    sucess = 0
    erro = 0
    for i in range(5,105):
        options = {}
        options["detect_direction"] = "true"
        image = get_file_content("./word_num_captcha/{}.jpg".format(i))
        response = client.basicAccurate(image, options)
        print(response)

        result = input("请确认结果:sucess:1,error:0----:")
        if result=="1":
            sucess+=1
        else:
            erro +=1
        print("total{},sucess_num:{},error_num:{}".format(i,sucess,erro))
        time.sleep(1)

if __name__ == '__main__':

    get_captcha_image()  #获取验证码

    # get_captcha_result()  #获取验证码破解结果
