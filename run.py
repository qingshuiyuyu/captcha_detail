#!/usr/bin/env python
# -*- coding=UTF-8 -*-

import requests, base64
import json
# from imgs  import logo
logo = """
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
"""
class BaiduImagesApi(object):

    headers = {
        "Content-Type":"application/x-www-form-urlencoded"
    }

    client_id = "cwSaqMSrNSlu92KfMNT4ZjGv"
    client_secret = "U3V06Me8ytIlYLZAiPduG9eIVIE3UoB0"

    def __init__(self):

        self.access_token = self.get_access_token()
        self.image_data = {
            "image":logo,
            "recognize_granularity":"big",  #是否定位单字符位置
            "detect_direction":"true",  #是否检测图像朝向
            "vertexes_location":"false",
            "probability":"false",
        }

    def get_url_result(self):

        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=" + self.access_token
        try:
            response = requests.get(url=url, headers=self.headers, timeout=20, json=self.image_data)
            print(response.status_code)
            print(response.text)
        except Exception as e:
            print(e)

    def get_access_token(self):

        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(self.client_id,self.client_secret)

        data = {
            "grant_type":"client_credentials",
            "client_id":self.client_id,
            "client_secret":self.client_secret
        }

        try:
            response = requests.get(url=host, headers=self.headers, timeout=20,data=data)
            jdata = json.loads(response.text)
            access_token = jdata.get("access_token")
            return access_token

        except Exception as e:
            print(e)
        finally:
            pass



if __name__ == '__main__':

    api = BaiduImagesApi()
    api.get_url_result()