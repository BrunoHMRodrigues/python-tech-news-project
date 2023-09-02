from tech_news.database import find_news


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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
