import pytest

# Это главный служебный файл pytest. 
# Всё, что написано в conftest.py, автоматически становится доступно во всех тестовых файлах в той же папке и её подпапках.

@pytest.fixture(scope="session")
def base_url() -> str:
    """Фикстура уровня всей тестовой сессии (scope='session').
    Выполняется 1 раз за весь прогон тестов.
    """
    return "https://jsonplaceholder.typicode.com"
