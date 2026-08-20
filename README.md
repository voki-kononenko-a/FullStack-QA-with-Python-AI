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

Запуск теста через pytest с ключами подробного вывода -v (verbose — подробный лог) и -s (показывать print в консоли):
pytest python/project/tests/test_api_store.py -v

Запуск проверок после выноса фикстуры в conftest.py(запускает все тесты):
cd python/project
pytest

Шпаргалка для перемещения по уровням через терминал:
cd .. — подняться на один уровень вверх (назад).
cd ../.. — подняться на два уровня вверх.
cd name_of_folder — зайти в папку name_of_folder.
cd / или cd ~ — перейти в корневую или домашнюю директорию.

Установка плагина для генерации файла с отчётом:
pip install pytest-html

Обновление requirements.txt после установки плагинов:
pip freeze > python/project/requirements.txt

Запуск тестов по маркировкам:
pytest -m smoke - smoke можно менять на любую другую маркировку, и запустится фикстура с этим маркером

Генерация HTML-файла с отчетом:
pytest --html=report.html
Запустить только smoke и сгенерировать отчёт:
pytest -m smoke --html=report.html
Запустить всё, КРОМЕ smoke (через not):
pytest -m "not smoke"
Запустить тесты, у которых есть И smoke, И api:
pytest -m "smoke and api"

Запуск теста с параметрами из командной строки - файл conftest.py:
pytest - обычный запуск. По умолчанию будет выбран qa
pytest --env=qa - запуск qa окружения
pytest --env=dev - запуск dev окружения. Сейчас падает с ошибкой, т.к. нет такой ссылки в инете