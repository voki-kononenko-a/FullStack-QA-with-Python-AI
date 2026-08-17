# --- 1. Обработка строк и очистка тестовых данных ---

def clean_authorization_token(raw_header: str) -> str:
    """Очищает заголовок авторизации от лишних пробелов и префиксов.
    Использует методы .strip() и .replace()
    """
    # .strip() удаляет пробелы, табы и переносы '\n' в начале и конце строки
    cleaned = raw_header.strip()
    
    # .replace("Bearer ", "") удаляет подстроку "Bearer "
    token = cleaned.replace("Bearer ", "")
    return token


def parse_csv_test_data(csv_line: str) -> list[str]:
    """Разбивает строку из CSV-файла с тестовыми данными в список.
    Использует метод .split()
    """
    # .split(",") режет строку по запятой и делает из нее список ['user1', 'pass123', 'admin']
    return csv_line.strip().split(",")


def format_endpoint_path(path_parts: list[str]) -> str:
    """Собирает URL-путь из списка частей.
    Использует метод .join()
    """
    # "/".join(...) склеивает элементы списка через слэш
    return "/" + "/".join(path_parts)


# --- 2. Кортежи (Tuple) и Арифметика ---

def get_screen_resolution() -> tuple[int, int]:
    """Возвращает неизменяемый кортеж (tuple) с разрешением экрана для UI-тестов."""
    # Кортеж создается в круглых скобках (). Поменять значения внутри нельзя!
    resolution = (1920, 1080)
    return resolution


def calculate_pagination(total_items: int, page_size: int) -> dict:
    """Считает количество страниц на основе арифметических операций."""
    # Целочисленное деление //
    full_pages = total_items // page_size
    
    # Остаток от деления %
    remaining_items = total_items % page_size
    
    return {
        "full_pages": full_pages,
        "has_extra_page": remaining_items > 0
    }


# --- 3. Цикл while (Ожидание статуса готовности) ---

def wait_for_job_completion(max_checks: int) -> bool:
    """Имитирует ожидание готовности задачи на сервере через цикл while."""
    checks_count = 0
    job_status = "PROCESSING"
    
    # Цикл выполняется ПОКА checks_count < max_checks И статус НЕ "SUCCESS"
    while checks_count < max_checks and job_status != "SUCCESS":
        checks_count += 1
        print(f"Проверка №{checks_count}: Статус задачи = '{job_status}'...")
        
        # На 3-й попытке имитируем, что сервер закончил обработку
        if checks_count == 3: 
            job_status = "SUCCESS"
            
    assert job_status == "SUCCESS", f"Задача не завершилась за {max_checks} попыток!"
    return True
