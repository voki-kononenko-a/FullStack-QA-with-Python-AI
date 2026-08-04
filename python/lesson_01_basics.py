#Представь, что переменная — это подписанная коробка, в которую мы кладем какие-то данные, чтобы использовать их позже в тестах. В Python есть 4 основных простых типа данных:

# 1. str (String / Строка) — любой текст в кавычках
test_name = "Настя"

# 2. int (Integer / Целое число) — счетчики, ID, количество элементов
user_age = 28
attempts_count = 3

# 3. float (Число с плавающей точкой) — цены, время ответа сервера в секундах
response_time = 1.45

# 4. bool (Boolean / Логический тип) — принимает только True (Истина) или False (Ложь)
is_automation_engineer = True
is_element_visible = False

print("Этот автотест писала " + test_name + "!")
print(is_automation_engineer)
print("Насте", user_age, "лет!")
print(f"кто писал автотест? {test_name}!")