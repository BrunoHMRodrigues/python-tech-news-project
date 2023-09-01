# Requisito 1
from parsel import Selector
from urllib.parse import urlparse
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
    selector = Selector(text=html_content)

    next_page_element = selector.css(
        'nav.navigation.pagination a.next.page-numbers'
    )

    if next_page_element:
        # Use o método .attrib para acessar o valor do atributo 'href'
        next_page_url = next_page_element.attrib.get('href')
        return next_page_url

    return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    news_data = {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css('h1.entry-title::text').get().strip(),
        "timestamp": selector.css('li.meta-date::text').get().strip(),
        "writer": selector.css('span.author a::text').get(),
        "reading_time": int(selector.css(
            'li.meta-reading-time::text').re_first(r'\d+')
        ),
        "summary": "".join(selector.css(
            ".entry-content > p:first-of-type *::text"
        ).getall()).strip(),
        "category": selector.css('a.category-style span.label::text').get()

    }

    return news_data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
