from cgitb import html
import csv
from dataclasses import field
import json
from string import capwords
import requests
from bs4 import BeautifulSoup as BS
from url import URL


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

response = requests.get(URL, headers=headers)

def get_html_card():
    html = requests.get(URL)
    soup = BS(html.text, 'lxml')
    cards = soup.find_all('div', class_='item product_listbox oh')
    return cards

def parse_cards(cards):
    obj_list = []
    for i in cards:
        obj = {
            'title': i.find('div', class_='listbox_title oh').find('a').text,
            'price': i.find('div', class_='listbox_price text-center').text,
            'image': i.find('div', class_='listbox_img pull-left').find('img').get('src')
        }
        obj_list.append(obj)
    with open('csvDB.csv', 'w') as file:
        fieldnames = obj_list[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(obj_list)

cards = get_html_card()
parse_cards(cards)



















