#!/usr/bin/env python
# -*- coding=UTF-8 -*-

import time
import re
import random
from lxml import etree
from api_sdk import get_baidu_api

from selenium import webdriver
from selenium.webdriver import ActionChains
from chrome_add_proxy import create_proxyauth_extension


class QichachaLogin():
    def get_captcha(self):

        proxyauth_plugin_path = create_proxyauth_extension(
            proxy_host="117.41.186.201",
            proxy_port=888,
            proxy_username="cj717k",
            proxy_password="cj717k"
        )
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_extension(proxyauth_plugin_path)
        # 设置代理
        # chromeOptions.add_argument("--proxy-server=http://{}:{}".format(self.host, self.port))
        # chromeOptions.add_argument('--headless')
        # chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
        driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path="./chromedriver.exe")
        try:
            driver.get("https://www.qichacha.com/")
            time.sleep(3)
            driver.find_element_by_xpath("//a[text()='登录']").click()
            time.sleep(3)
            driver.find_element_by_xpath("//a[text()='密码登录']").click()
            time.sleep(3)
            driver.maximize_window()
            time.sleep(1)
            element = driver.find_element_by_xpath("//div[@id='nc_1__bg']")
            ActionChains(driver).click_and_hold(on_element=element).perform()
            ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=400,
                                                             yoffset=random.choice(range(10, 15))).perform()
            time.sleep(10)
            location = (1, 2)
            for i in range(1, 6):
                print("---进行第{}次尝试---".format(i))
                page_source = driver.page_source
                html = etree.HTML(page_source)
                img = html.xpath("//div[@class='clickCaptcha_img']/img/@src")
                itext = html.xpath("//div[@id='dom_id_one']//text()")
                itext = ''.join([i.strip() for i in itext])
                word = re.compile(r".*“(.*?)”.*").findall(itext)[0]
                img = img[0].split(",")[-1]
                print(img, word)
                location = get_baidu_api(img, word)
                if not location:
                    driver.find_element_by_xpath("//div[@class='clickCaptcha_text']/i").click()
                    time.sleep(10)
                    continue
                x = location[0]
                y = location[1]
                print(x, y)

                for i in range(50):
                    el = driver.find_element_by_xpath("//div[@class='clickCaptcha_img']/img")
                    # 左上角为0，0，向右向下移动为正数字，向左向上移动为负数值
                    x_move = random.choice(list(range(x-20,x+20)))
                    y_move = random.choice(list(range(y-20,y+20)))
                    ActionChains(driver).move_to_element_with_offset(to_element=el,
                                                                     xoffset=x_move,
                                                                     yoffset=y_move).perform()
                    time.sleep(0.1 / random.choice(list(range(1, 10))))

                el = driver.find_element_by_xpath("//div[@class='clickCaptcha_img']/img")
                # 左上角为0，0，向右向下移动为正数字，向左向上移动为负数值
                ActionChains(driver).move_to_element_with_offset(to_element=el, xoffset=x+8,
                                                                 yoffset=y+10).click().perform()
                time.sleep(5)
                if "验证码点击错误，请重试" in driver.page_source:
                    driver.find_element_by_xpath("//div[@class='clickCaptcha_text']/i").click()
                    time.sleep(10)
                    continue
                elif "验证通过" in driver.page_source:
                    print("---点击验证成功!---")
                    time.sleep(10)
                    return
        except Exception as e:
            print(e)
        finally:
            time.sleep(10)
            driver.close()


if __name__ == '__main__':

    for i in range(10):
        qichacha = QichachaLogin()
        qichacha.get_captcha()
