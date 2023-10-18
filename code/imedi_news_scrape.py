import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os
from openpyxl import load_workbook

base_url = 'https://imedinews.ge/ge/archive'

response = requests.get(base_url)

def clean(text: str):
    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    cleaned_text = re.sub(r'<(.*?)>', ' ', cleaned_text).strip()
    return cleaned_text



html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

titles = soup.find_all('p',class_ = 'description js-trunk8' )
links = soup.find_all('a',class_ = 'single-item' )
links = [i['href'] for i in links]
dic = []
for i in range(min(len(links), len(titles))):
    text = requests.get(links[i])
    text = text.content
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.find_all('div', class_ = 'news-text')
    if len(text) != 0:
        dic.append([clean(str(titles[i])), clean(str(text[0]))])
for i in range(0, 20):
    base_url = 'https://imedinews.ge/ge/archive?p=' + str(i + 1)

    response = requests.get(base_url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    titles = soup.find_all('p',class_ = 'description js-trunk8' )
    links = soup.find_all('a',class_ = 'single-item' )
    links = [i['href'] for i in links]
    for i in range(min(len(links), len(titles))):
        text = requests.get(links[i])
        text = text.content
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.find_all('div', class_ = 'news-text')
        if len(text) != 0:
            dic.append([clean(str(titles[i])), clean(str(text[0]))])


df = pd.DataFrame(dic, columns=['სათაური', 'ტექსტი'])
df.to_excel('Book12.xlsx', index=False)
