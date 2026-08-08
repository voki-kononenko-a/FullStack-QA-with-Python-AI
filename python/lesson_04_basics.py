# --- 1. Объявление функций-хелперов ---

def validate_response_time(response_time: float, max_limit: float = 2.0):
# Хелпер проверяет, не превышает ли время ответа допустимый SLA.
    assert response_time <= max_limit, f"Ошибка SLA: {response_time}s превышает лимит {max_limit}s"


def is_user_active(user_data: dict) -> bool:
# Хелпер проверяет активен ли пользователь, возвращая True или False.
    return user_data.get("is_active", False)


def get_user_id(user_data: dict) -> int:
# Хелпер безопасно достает ID пользователя из словаря.
    return user_data.get("id", 0)  # Если ключа "id" нет, вернет 0


# --- 2. Вызов функций (Автотесты) ---

# Вызов 1: Передаем 1.4 секунды. Так как 1.4 <= 2.0, assert пропустит код дальше.
validate_response_time(1.4)

# Вызов 2: Готовим тестовые данные (словарь)
test_user = {
    "id": 101,
    "email": "qa_lead@test.com",
    "is_active": True  # для фикса автотеста необходимо поставить True
}

# Функция вернет True, результат запишется в переменную status
status = is_user_active(test_user)
user_id = get_user_id(test_user)
goal_user_id = 101

# Проверяем через assert, что status действительно равен True
assert status is True, f"Ожидался активный пользователь, но получили {status}"
assert user_id == goal_user_id, f"Ожидался {test_user['id']}, но получили {goal_user_id}"

print("Все проверки функций успешно пройдены!")



def get_user_role(response_data: dict) -> str:
# Безопасно достает роль из вложенного ответа API. Если роли нет, возвращает 'GUEST'.
    return response_data.get("data", {}).get("role", "GUEST")


# --- Автотест ---

# Case 1: Успешный ответ от сервера
auth_response = {
    "status": 200,
    "data": {
        "user_id": 777,
        "role": "ADMIN"
    }
}
role_1 = get_user_role(auth_response)
assert role_1 == "ADMIN", f"Ожидалась роль ADMIN, но получили {role_1}"

# Case 2: Неавторизованный пользователь (нет объекта data)
guest_response = {
    "status": 401,
    "message": "Unauthorized"
}
role_2 = get_user_role(guest_response)
assert role_2 == "GUEST", f"Ожидалась роль GUEST, но получили {role_2}"

print("Тест безопасности извлечения роли пройден успешно!")