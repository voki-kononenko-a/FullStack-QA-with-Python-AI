import json
from pathlib import Path

# --- 1. Подготовка тестовых данных (Конфиг для тестов) ---
data_to_save = {
    "base_url": "https://stage.example.com/api/v1",
    "timeout": 10,
    "retries": 3,
    "debug_mode": True
}

# file_name = "test_config.json"
# .parent.parent — поднимется на уровень выше, чем python и положит файл в корень проекта qa-automation-course/
file_name = Path(__file__).resolve().parent.parent / "test_config.json"

# --- 2. Запись тестовых данных в JSON-файл ---
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(data_to_save, file, indent=4)


# --- 3. Чтение тестовых данных из JSON-файла ---
with open(file_name, "r", encoding="utf-8") as file:
    loaded_config = json.load(file)


# --- 4. Проверки (Автотест) ---

# Убеждаемся, что запись и чтение совпали
assert loaded_config == data_to_save

# Проверяем, что считались корректные данные (более обширный вариант ассерта выше)
assert loaded_config["base_url"] == "https://stage.example.com/api/v", (
    f"Ошибка: Неверный base_url! Должно быть: {loaded_config['base_url']}"
)

assert loaded_config["timeout"] == 10, (
    f"Ошибка: Неверный timeout! Должно быть: {loaded_config['timeout']}"
)

assert loaded_config["debug_mode"] is True, "Ошибка: debug_mode должен быть True!"

print("Тест чтения и записи JSON-конфига пройден успешно!")
