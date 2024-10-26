# Настройки для UI тестов
UI_BASE_URL = "https://www.chitai-gorod.ru/"

# Тестовые данные
SEARCH_TERMS = {
    "cyrillic": "книга",
    "latin": "book",
    "numbers": "1984",
    "dash": "книга-приключение",
    "exclamation": "книга!",
    "question": "книга?",
}

# Настройки окружения для API тестов
API_BASE_URL = "https://web-gate.chitai-gorod.ru/api/v2/search/facet-search?customerCityId=213&phrase="
AUTH_TOKEN = "Bearer <токен>"
HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Cookie": "__ddg10_=1729943037; __ddg1_=mame6X9a1pLTeHyrFYbg; __ddg8_=h7W4ODJdCn3wH3fg; __ddg9_=217.15.57.162",
    "Cache-Control": "no-cache",
    "User-Agent": "PostmanRuntime/7.42.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"}
