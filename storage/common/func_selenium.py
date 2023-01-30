# Seleniumをimport
from common.func_selenium import webdriver
import chromedriver_binary
import os
import signal

class SeleniumTools:
# data
    vue_localhost_path = "http://localhost:8080/"
    react_localhost_path = "http://localhost:3000/"

# methods
    def __init__(self):
        pass

    def __del__(self):
        pass
    
    # @brief Vue localhostにアクセス
    def connect_vue_localhost(self):
        driver = webdriver.Chrome()
        try:
            driver.get(self.vue_localhost_path)
        finally:
            # chromedriverプロセスのIDに終了シグナルを送ることで
            # python処理を修了しても、Chromeを立ち上げておける
            os.kill(driver.service.process.pid,signal.SIGTERM)
            
    # @brief React localhostにアクセス
    def connect_react_localhost(self):
        driver = webdriver.Chrome()
        try:
            driver.get(self.react_localhost_path)
        finally:
            # chromedriverプロセスのIDに終了シグナルを送ることで
            # python処理を修了しても、Chromeを立ち上げておける
            os.kill(driver.service.process.pid,signal.SIGTERM)
    