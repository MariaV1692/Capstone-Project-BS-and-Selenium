from bs4 import BeautifulSoup
import requests
import config
import time


class DataFinder:
    def __init__(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                          "like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
            "accept-language": "en-US,en;q=0.9",
            "authority": "collector-pxhyx10rg3.px-cloud.net"
        }
        self.response = requests.get(url=config.houses_url, headers=headers)
        self.rentals_response = self.response.text
        self.soup = BeautifulSoup(self.rentals_response, "html.parser")

    def data_scraping(self):
        time.sleep(3)
        property_anchor_tags = self.soup.find_all(name="a", class_="list-card-link")
        property_price_divs = self.soup.find_all(name="div", class_="list-card-price")

        data_dic = {
            'links_list': [],
            'addresses_list': [],
            'prices_list': []
        }

        for anchor_tag in property_anchor_tags[:3]:
            property_link = anchor_tag.get("href")
            property_address = anchor_tag.getText()
            data_dic['links_list'].append(property_link)
            data_dic['addresses_list'].append(property_address)

        for div in property_price_divs:
            property_price = div.getText().split("/")[0]
            data_dic['prices_list'].append(property_price)

        return data_dic
