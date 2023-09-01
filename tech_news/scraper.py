# Requisito 1
from parsel import Selector
import time
import requests


def fetch(url):
    time.sleep(1)
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)

        if response.status_code == 200:
            return response.text
        else:
            return None

    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    urls = []
    selector = Selector(text=html_content)

    links = selector.css('a.cs-overlay-link')

    for link in links:
        href = link.attrib['href']
        urls.append(href)
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
