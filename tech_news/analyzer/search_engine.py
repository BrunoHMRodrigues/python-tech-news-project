from tech_news.database import find_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news_data = find_news()

    news_found = []

    for news in news_data:
        if title.lower() in news["title"].lower():
            response = (news["title"], news["url"])
            news_found.append(response)

    return news_found


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(
            date, "%Y-%m-%d").strftime("%d/%m/%Y")

    except ValueError:
        raise ValueError("Data inválida")

    news_data = find_news()
    news_found = []

    for news in news_data:
        if formatted_date == news["timestamp"]:
            response = (news["title"], news["url"])

            news_found.append(response)

    return news_found


# Requisito 9
def search_by_category(category):
    news_data = find_news()

    news_found = []

    for news in news_data:
        if category.lower() in news["category"].lower():
            response = (news["title"], news["url"])
            news_found.append(response)

    return news_found
