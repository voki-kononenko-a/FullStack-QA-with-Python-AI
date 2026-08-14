Изучение Python по Gemini
А также книга «Изучаем Python» — Марк Лутц

Ветка studies/develop
https://github.com/voki-kononenko-a/FullStack-QA-with-Python-AI/tree/studies/develop

Запуск файла (перед этим ОБЯЗАТЕЛЬНО сохранить):
python python/lesson_06_errors.py
python python/project/tests/test_data_cleaner.py

Команды для пушей:
git add .  - добавляет все
git commit -m "Название...."
git push -u origin studies/develop  

Переименовывание ветки:
git branch -M main

Пуш ветки:
git push -u origin main

Создание ветки и переключение на нее:
git checkout -b studies/develop

Переключение на существующую ветку:
git checkout studies/develop

Пул и возвращение на ветку:
git checkout main
git pull origin main
git checkout studies/develop

Ctrl + L - прикрепление файла (с привязкой к строкам) к промпту

Скачать главную библиотеку Python для отправки HTTP-запросов к API (GET, POST, PUT, DELETE). 
Создать файл requirements.txt в папке project (в начале работы с проектом)
pip install requests pytest
pip freeze > python/project/requirements.txt
