import pytest

# Это главный служебный файл pytest. 
# Всё, что написано в conftest.py, автоматически становится доступно во всех тестовых файлах в той же папке и её подпапках.

@pytest.fixture(scope="session")
def base_url() -> str:
    """Фикстура уровня всей тестовой сессии (scope='session').
    Выполняется 1 раз за весь прогон тестов.
    """
    return "https://jsonplaceholder.typicode.com"

# 1. Регистрируем новый флаг командной строки --env - детально в README
def pytest_addoption(parser):
    """pytest_addoption(parser) — служебная функция Pytest. Она говорит фреймворку: 
    Добавь в список команд терминала новый аргумент --env
    """
    parser.addoption(
        "--env",
        action="store",
        # если инженер просто введёт pytest без параметров, автоматически выберется окружение qa
        default="qa",
        help="Окружение для запуска тестов: dev, qa, prod"
    )

# 2. Фикстура динамически выбирает base_url на основе флага --env
@pytest.fixture(scope="session")
def base_url(request) -> str:
    # Получаем значение флага --env из командной строки
    env = request.config.getoption("--env")

    # Словарь со ссылками на разные окружения
    env_urls = {
        "dev": "https://dev-jsonplaceholder.typicode.com",
        "qa": "https://jsonplaceholder.typicode.com",  # Наш рабочий тестовый стенд
        "prod": "https://prod-jsonplaceholder.typicode.com"
    }

    # Возвращаем URL для выбранного env (по умолчанию qa)
    return env_urls.get(env, env_urls["qa"])
