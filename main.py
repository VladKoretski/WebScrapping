import json
from pprint import pprint
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import config.config as cfg
import tools.tools as tools
# import requests
# import bs4

service = Service(ChromeDriverManager().install())
options = ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)
driver_article = webdriver.Chrome(service=service, options=options) # для сб = webdriver.Chrome(service=service, options=options)

driver.get(cfg.URL)
content_block = tools.wait_element(driver, value=cfg.CONTENT_BLOCK)
article_list = content_block.find_elements(By.CSS_SELECTOR, cfg.ARTICLE_BLOCK)

parsed_pages = list()
parsed_pages_final = list()
parsed_page = dict()

for article in article_list:
    title_element = tools.wait_element(article, value=cfg.ARTICLE_TITLE)

    link = title_element.get_attribute('href')
    print(link)
    title = title_element.text.strip()
    time_element = tools.wait_element(article, value='time')
    data_and_time = time_element.get_attribute('title')

# --- собираем тексты через риквест
#     response = requests.get(link)
#     article_soup = bs4.BeautifulSoup(response.text, 'lxml')
#     text_body = article_soup.select_one('div.article-formatted-body').text.strip()
#     print(f'{text_body[:100]}... первые 100 символов')

# --- cобираем тексты через селениум
    driver_article.get(link)
    article_body = tools.wait_element(driver_article, value="div.article-formatted-body")
    text_body = tools.wait_element(driver_article, value='div.article-formatted-body').text.strip()
#    print(text_body[:100])

    parsed_page = {
        'title': title,
        'data_and_time': data_and_time,
        'text': text_body,
        'link': link,
    }

    for keyword in cfg.KEYWORDS:
        if (keyword.lower() in title.lower()) or (keyword.lower() in text_body.lower()):
            if parsed_page not in parsed_pages:
                parsed_pages.append(parsed_page)
                parsed_pages_final.append({
                    'title': title,
                    'data_and_time': data_and_time,
                    'text': text_body,
                    'link': link,
                    'keyword': keyword
                })
                break

pprint(parsed_pages_final)
print(len(parsed_pages_final))

with open('parsed_pages.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_pages_final, f, ensure_ascii=False, indent=2)

driver_article.quit()
driver.quit()
