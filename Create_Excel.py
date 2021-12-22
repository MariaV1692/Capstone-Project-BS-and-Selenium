import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

import config

options = Options()
options.add_argument("window-size=1400,1200")
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'


class ExcelMaker:
    URL = config.EXCEL_SHEET_URL

    def __init__(self):
        self.driver = Firefox(executable_path=config.FIREFOX_DRIVER_PATH, options=options)
        self.driver.get(url=self.URL)

    def login(self):
        pass

