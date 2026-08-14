import sys
from pathlib import Path

# Добавляем папку project в пути поиска модулей Python
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Импортируем из папки python.project.utils
from utils.data_cleaner import (
    clean_authorization_token,
    parse_csv_test_data,
    format_endpoint_path,
    get_screen_resolution,
    calculate_pagination,
    wait_for_job_completion
)

# --- Автотесты утилит фреймворка ---

# 1. Тест очистки строки
raw_token = "  Bearer eyJhbGciOiJIUzI1NiIsIn... \n"
cleaned_token = clean_authorization_token(raw_token)
assert cleaned_token == "eyJhbGciOiJIUzI1NiIsIn...", f"Ошибка очистки! Получили: '{cleaned_token}'"

# 2. Тест split и join
csv_row = "admin,secret_pass,active\n"
parsed_data = parse_csv_test_data(csv_row)
assert parsed_data == ["admin", "secret_pass", "active"], f"Ошибка split: {parsed_data}"

path = format_endpoint_path(["api", "v1", "users"])
assert path == "/api/v1/users", f"Ошибка join: {path}"

# 3. Тест tuple и математики
res = get_screen_resolution()
# Проверяем, что res это именно tuple (кортеж)
assert isinstance(res, tuple), "Ожидался тип tuple!"
assert res[0] == 1920 and res[1] == 1080

pages = calculate_pagination(total_items=25, page_size=10)
assert pages["full_pages"] == 2, f"Ожидалось 2 полных страницы, но получили {pages['full_pages']}"
assert pages["has_extra_page"] is True

# 4. Тест цикла while
is_job_ok = wait_for_job_completion(max_checks=5)
assert is_job_ok is True

print("Все утилиты проекта прошли тесты!")