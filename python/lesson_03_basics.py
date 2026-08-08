# ПРАКТИКА

# 1. Объявление словаря (JSON ответа от сервера)
api_response = {
    "status": "success",
    "data": {
        "user_id": 108,
        "email": "test_qa@example.com",
        "role": "QA_ENGINEER",
        "permissions": ["READ_LOGS", "RUN_TESTS", "CREATE_BUG"]
    }
}

# 2. Получение значений по ключу
is_success = api_response['status'][0] 
# В квадратных скобках [] вы указываете название ключа (название поля), значение которого хотите достать из словаря, а НЕ само значение.
qa_role = api_response['data']['role']
permissions = api_response['data']['permissions'][1]

# 3. Безопасное получение через .get() (не падает с KeyError, если ключа нет)
token = api_response.get("token", None)

# --- ПРОВЕРКИ (ASSERTIONS) ---

# 1. Проверяем, что поле "status" равно "success"
actual_status = 'success' # sucess
assert api_response['status'] == actual_status, f"Ожидался {api_response['status']}, но получен {actual_status}"
# assert api_response["status"] == "sucess", f"Ожидался status 'success', но получен '{api_response['status']}'"

# 2. Проверяем роль: заходим в "data", а затем в "role"
actual_role = api_response["data"]["role"]
assert actual_role == "QA_ENGINEER", f"Ожидалась роль 'QA_ENGINER', но получена '{actual_role}'"

# 3. Проверяем права: заходим в "data", берем список "permissions" и проверяем наличие элемента
permissions_list = api_response["data"]["permissions"]
assert "RUN_TEST" in permissions_list, f"Право 'RUN_TESTS' отсутствует в списке {permissions_list}"
# для починки нужно написать "RUN_TESTS" in perm....

print("Все проверки успешно пройдены!")