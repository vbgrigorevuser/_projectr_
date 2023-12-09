# _projectr_

## Шаги, сделанные для развертывания API

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
7. Разработка моделей (схемы базы данных) в файле api/models.py
