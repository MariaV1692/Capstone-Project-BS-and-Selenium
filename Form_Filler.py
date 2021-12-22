import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config

options = Options()
options.add_argument("window-size=1400,1200")


class FormFiller:
    FORM_URL = config.FORM_URL

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, options=options)
        self.driver.get(url=self.FORM_URL)

    def find_input(self, text, input_text):
        div_text = self.driver.find_element(f"//*[contains(text(), '{text}')]")
        div_text.find_element_by_xpath('..').find_element_by_xpath('..') \
            .find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_tag_name('input').send_keys(input_text)

    def fill_form(self, data_dic):
        time.sleep(2)
        for n, value in enumerate(data_dic['prices_list']):
            send_button = self.driver.find_element("div[role='button']")
            property_price = data_dic['prices_list'][n]
            property_address = data_dic['addresses_list'][n]
            property_link = data_dic["links_list"][n]
            self.find_input(text="the address of the property", input_text=property_address)
            self.find_input(text="the price per month", input_text=property_price)
            self.find_input(text="the link to the property", input_text=property_link)
            time.sleep(1)
            send_button.click()
            time.sleep(2)
            self.driver.find_element('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
            time.sleep(2)
