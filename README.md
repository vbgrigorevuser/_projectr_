# \_projectr\_

## Шаги, сделанные для развертывания API

Справка: https://django.fun/articles/tutorials/sozdajte-rest-api-za-30-minut-s-pomoshyu-django-rest-framework/

1. Подготовка пространства venv ```python3 -m venv .venv```, активация ```source .venv/bin/activate```
2. Установка django и djangorestframework ```pip install django```, ```pip install djangorestframework```
3. Создание папки для проекта ```makedir projectr```, переход в папку ```cd projectr```
4. Создание проекта django ```django-admin startproject back```
5. Создание главного приложения api ```python3 manage.py startapp api```
6. Изменение файла back/settings.py
```
...
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'rest_framework',
...
```
7. Подключение стандартных моделей django ```python3 manage.py makemigrations```, ```python3 manage.py migrate```
8. Разработка моделей (схемы базы данных) в файле api/models.py
9. Создание аккаунта админа ```python3 manage.py createsuperuser```
10. Создание схемы базы данных (api/models)
11. Регистрация моделей в api/admin.py
12. Обновление схемы ```python3 manage.py makemigrations```, ```python3 manage.py migrate```
13. Создание сериализаторов в serilalizers.py
14. Создание отображений back/views.py
15. Добавление url'ов back/urls.py, api/urls.py
16. Решение проблемы no 'Access-Control-Allow-Origin' при работе ```pip install django-cors-headers```
17. Добавление в ```INSTALLED_APPS``` ```'corsheaders',```
18. Правка ```MIDDLEWARE```
```
MIDDLEWARE = [  
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```
19. Перед ```INSTALLED_APPS``` вставка ```CORS_ORIGIN_ALLOW_ALL=True```
