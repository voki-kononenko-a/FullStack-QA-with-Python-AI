expected_bv_damage = 200
actual_bv_damage = 200

# Синтаксис: assert условие, "Сообщение при ошибке"
assert expected_bv_damage == actual_bv_damage, (
f"Ожидался урон {expected_bv_damage}," 
f"но получен урон {actual_bv_damage}"
)

# Список уровней от нескольких эндпоинтов
level_ids = [589, 14587, 222, 365]

# Проверяем каждый уровень в цикле
for level in level_ids:
    assert level in [589, 3, 222, 365], f"Обнаружен лишний уровень: {status}"

# --- Тест 1: Проверка времени открытия окна ЛП ---
window_load_times = [0.8, 1.2, 0.5, 1.9, 2.3]  # в секундах
max_allowed_time = 2.0  # допустимый порог по SLA

for load_time in window_load_times:
    assert load_time <= max_allowed_time, (
        f"Тест упал! Окно ЛП загружалось {load_time} сек. "
        f"(Превышен лимит в {max_allowed_time} сек.)"
    )

print("Все окна загрузились в пределах нормы SLA!")
