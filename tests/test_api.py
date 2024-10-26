import sys
import os
import pytest
import requests
import allure
from config.config import API_BASE_URL, HEADERS

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def log_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print("Response content is not JSON")


@pytest.fixture
def session():
    """Фикстура для создания сессии, которая будет использоваться в тестах."""
    with requests.Session() as session:
        session.headers.update(HEADERS)
        yield session


@pytest.mark.parametrize("title",
                         ["Война и мир",
                          "Гарри Поттер",
                          "книга-приключение"])
@allure.story("Поиск книг по названию")
def test_search_by_title(session, title):
    with allure.step(f"Поиск книги с названием '{title}'"):
        response = session.get(f"{API_BASE_URL}{title}")
        log_response(response)
        assert response.status_code == 200, f"Expected 200, but got {
            response.status_code}"
        json_response = response.json()
        assert "data" in json_response, f"No 'data' key found for title: {title}"
        assert len(json_response["data"]
                   ) > 0, f"No books found for title: {title}"


@pytest.mark.parametrize("author", ["Толстой", "Роулинг", "Пушкин"])
@allure.story("Поиск книг по автору")
def test_search_by_author(session, author):
    with allure.step(f"Поиск книги с автором '{author}'"):
        response = session.get(f"{API_BASE_URL}{author}")
        log_response(response)
        assert response.status_code == 200, f"Expected 200, but got {
            response.status_code}"
        json_response = response.json()
        assert "data" in json_response, f"No 'data' key found for author: {author}"
        assert len(json_response["data"]
                   ) > 0, f"No books found for author: {author}"


@pytest.mark.parametrize("genre", ["фантастика", "классика", "приключения"])
@allure.story("Поиск книг по жанру")
def test_search_by_genre(session, genre):
    with allure.step(f"Поиск книги по жанру '{genre}'"):
        response = session.get(f"{API_BASE_URL}{genre}")
        log_response(response)
        assert response.status_code == 200, f"Expected 200, but got {
            response.status_code}"
        json_response = response.json()
        assert "data" in json_response, f"No 'data' key found for genre: {genre}"
        assert len(json_response["data"]
                   ) > 0, f"No books found for genre: {genre}"


@allure.story("Поиск книг с пустым запросом")
def test_search_with_empty_query(session):
    with allure.step("Выполнение поиска с пустым запросом"):
        response = session.get(API_BASE_URL)
        log_response(response)
        assert response.status_code == 400, f"Expected 400, but got {
            response.status_code}"


@allure.story("Поиск книг с неверным методом запроса")
def test_search_with_wrong_method(session):
    with allure.step("Выполнение поиска методом POST"):
        response = session.post(f"{API_BASE_URL}Гарри Поттер")
        log_response(response)
        assert response.status_code == 405, f"Expected 405, but got {
            response.status_code}"
