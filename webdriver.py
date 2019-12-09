import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:

    def __init__(self):
        if os.getenv('DRIVER_MODE') == 'headless' or os.getenv('DRIVER_MODE') is None:
            chrome_options = Options()
            chrome_options.headless = True
            chrome_options.add_argument("--window-size=1920x1080")
            self.instance = webdriver.Chrome(options=chrome_options)
        elif os.getenv('DRIVER_MODE') == 'visual':
            self.instance = webdriver.Chrome()
        else:
            raise Exception("Invalid driver mode.")

    def get(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError('URL must be a string.')

    def add_cookie(self, cookie_dict):
        self.instance.add_cookie(cookie_dict)
