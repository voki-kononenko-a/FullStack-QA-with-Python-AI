#Представь, что переменная — это подписанная коробка, в которую мы кладем какие-то данные, чтобы использовать их позже в тестах. В Python есть 4 основных простых типа данных:

#1. str (String / Строка) — любой текст в кавычках
test_name = "Настя"

#2. int (Integer / Целое число) — счетчики, ID, количество элементов
user_age = 28
attempts_count = 3

#3. float (Число с плавающей точкой) — цены, время ответа сервера в секундах
response_time = 1.45

#4. bool (Boolean / Логический тип) — принимает только True (Истина) или False (Ложь)
is_automation_engineer = True
is_element_visible = False

print("Этот автотест писала " + test_name + "!")
print(is_automation_engineer)
print("Насте", user_age, "лет!")
print(f"Кто писал автотест? {test_name}!")


#Условные операторы
status_code = 200

if status_code == 200:
    print("Обучение прошло успешно!")
elif status_code == 404:
    print("Страница не найдена")
else:
    print("Получен неизвестный статус-код")

#Сравнение: == (равно), != (не равно), >, <, >=, <=
#Логика: and (и — оба условия должны быть True), or (или — хотя бы одно True), not (отрицание)

is_admin = True
is_active = True

if is_admin and is_active:
    print("Доступ к панели администратора разрешён")

Calculated_progress = int(input("Введите текущий прогресс игрока: "))

if Calculated_progress == 50:
    print(f"Normal {Calculated_progress}")
elif Calculated_progress >= 51:
    print(f"High_help {Calculated_progress}")
else:
    print(f"High_stop {Calculated_progress}")

level = input ("Введите уровень игрока:")

if level != "222":
    print(f"Уровень", level, "не бонусный уровень")
else:
    print (f"Уровень", level, "является бонусным")
