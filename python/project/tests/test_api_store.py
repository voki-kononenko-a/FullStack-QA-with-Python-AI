import pytest
import requests

# Помечаем тест маркерами smoke и api
@pytest.mark.smoke
@pytest.mark.api
def test_get_single_post_status(base_url):
    """Smoke-тест: быстро проверяет доступность эндпоинта /posts/1."""
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200


# Этот тест временно пропускаем с причиной
@pytest.mark.skip(reason="Баг на бэкенде #BUG-102, ждем фикса")
def test_future_feature():
    """Тест новой фичи, которая еще не готова."""
    assert False

# Выведет список ВСЕХ доступных полей и методов объекта response
# Запускать через python python/project/tests/test_api_store.py
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(dir(response))

# --- 2. Параметризованный автотест ---
# Регрессионный тест с параметризацией

@pytest.mark.regression
@pytest.mark.api
@pytest.mark.parametrize("post_id, expected_title_keyword", [
    (1, "sunt"),
    (2, "qu"),
    (3, "ea")
])
def test_get_posts_parametrized(base_url, post_id, expected_title_keyword):
    """Тест проверяет сразу 3 разных поста с использованием фикстуры и параметризации. base_url из conftest.py"""
    url = f"{base_url}/posts/{post_id}"
    
    response = requests.get(url)
    assert response.status_code == 200, f"Ошибка при получении поста {post_id}"
    
    # Превращаем JSON-ответ от сервера в обычный Python-словарь.  
    data = response.json()
    assert data["id"] == post_id
    # Проверяем, что в заголовке поста есть ожидаемое ключевое слово с помощью in
    assert expected_title_keyword in data["title"], (
        f"Слово '{expected_title_keyword}' не найдено в title поста №{post_id}"
    )
    