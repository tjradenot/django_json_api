#### Подготовка проекта
- Создание директории
- Создание виртуального окружения
- python3 -m venv venv

#### Установка пакетов
pip install django psycopg2 djangorestframework django-filter

#### Создание проекта Django
```
django-admin startproject books
cd books
```

#### Создание приложения store
./manage.py startapp store
добавить в settings.py

#### Создать пользователя и базу:
```
sudo -u postgres createuser books_db_user
sudo -u postgres createdb books_db -Obooks_db_user
```

#### Проверить соединение с базой
Внести данные соединения с базой в settings.py
./manage.py migrate

#### Модель
title, author, price
./manage.py makemigrations
./manage.py migrate

#### Serializer
ModelSerializer

#### Представление
ModelViewSet
- фильтрация
- поиск
- сортировка

#### URLs
include, SimpleRouter()

#### Заполнить базу
./manage.py shell
```
from store.models import Book
Book.objects.create(title='Алгоритмы Теория и практическое применение', author='Род Стивенс', price=1000)
Book.objects.create(title='Грокаем алгоритмы', author='Адитья Бхаргава', price=500)
Book.objects.create(title='Внутреннее устройство Linux', author='Брайан Уорд', price=350)
Book.objects.create(title='Изучаем Python', author='Эрик Мэтиз', price=750)
```

#### Проверить API
```
http -b http://127.0.0.1:8000/api/book/?format=json
http -b http://127.0.0.1:8000/api/book/?format=json&title=%D0%93%D1%80%D0%BE%D0%BA%D0%B0%D0%B5%D0%BC%20%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B
http -b http://127.0.0.1:8000/api/book/?format=json&search=python
http -b http://127.0.0.1:8000/api/book/?format=json&search=алгоритм
http -b http://127.0.0.1:8000/api/book/?format=json&ordering=title
```
