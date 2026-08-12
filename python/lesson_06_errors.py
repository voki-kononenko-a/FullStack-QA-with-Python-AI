import json
from pathlib import Path
import pytest

try:
    # Пробуем выполнить опасный код
    with open("config.json", "r", encoding="utf-8") as f:  # ошибка, поскольку такого файла нет. НО при этом тест не упадет, а выведет сообщение
        data = f.read()
except FileNotFoundError:
    # Этот блок сработает ТОЛЬКО если файла не существует
    print("Файл не найден! Используем дефолтные настройки.")

# Определяем путь к файлу
config_path = Path(__file__).resolve().parent.parent / "test_config.json"

try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    print("Файл конфигурации успешно загружен!")
except FileNotFoundError:
    print("[WARNING] Файл не найден! Используем тестовые настройки по умолчанию.")
    config = {"base_url": "https://default-stage.com", "timeout": 5}

# Дальше автотест работает с переменной config независимо от того, был файл или нет
assert config["timeout"] > 0, "Ошибка: timeout должен быть больше 0"

raw_response_code = "200_OK"  # Имитация некорректного ответа от API 

try:
# Пробуем перевести строку в целое число
    status_code = int(raw_response_code)
except (ValueError, TypeError) as e:
# Не маскируем ошибку, а явно роняем тест с информативным сообщением
    pytest.fail(f"БАК API: Сервер прислал валидационный код в неверном формате '{raw_response_code}'. Ошибка: {e}")

# До этой строки код дойдёт ТОЛЬКО если конвертация прошла успешно
assert status_code == 200, f"Тест упал: ожидался код 200, но получили {status_code}"

# Пробуем выполнить код
try:
    print("1. Подключаемся к базе данных автотестов...")
    connection_status = True
    assert connection_status is True, "Ошибка соединения!"
# except — срабатывает ТОЛЬКО при возникновении ошибки.
except AssertionError as err:
    print(f"2. Произошла ошибка: {err}")
# else — срабатывает ТОЛЬКО если код в try прошёл БЕЗ ошибок.
else:
    print("2. Подключение прошло успешно, выполняем SQL-запрос.")
# finally — срабатывает ВСЕГДА (была ошибка или нет). В QA используется для очистки тестовых данных (teardown).
finally:
    print("3. Закрываем соединение с базой данных (выполняется всегда).")
