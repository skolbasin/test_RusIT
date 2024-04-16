# Тестовое задание для компании RusIT

## Условие
Необходимо написать 2 модели в Django(стол и бронь) и для них 7 API. БД через PosgreSQL, развернутое через Docker + Redis для кеширования.

## Как запустить проект
1. Клонировать репозиторий:
```
git clone https://github.com/skolbasin/test_RusIT.git
```
2. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
3. Выполнить миграции для создания структуры базы данных:
```
python manage.py makemigrations
python manage.py migrate
```
либо на Linux:
```
make migrate
```

4. Запустить сервер :
```
python manage.py runserver
```
либо на Linux:
```
make run
```
5. Создайте суперюзера
```
python manage.py createsuperuser
```
либо на Linux:
```
make superuser
```
6. После запуска сервера перейдите по адресу http://localhost:8000/admin и введи логин и пароль от суперюзера
## Админка
В проекте настроена админка для удобства работы с моделями(admin.py)

### Главная страница админки
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/2b8b0ba8-1fdb-45fa-be9b-81e395b58bc5)
### Модель стола 
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/4fb8e8e7-b4ec-4dec-b5f4-8df50f829efd)
### Модель брони 
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/1382a81e-23fe-4b4a-bdfa-9b5443981644)

## Работа API через POSTMAN

## API для добавления стола через POST запрос
## API для изменения данных о столе
## API для удаления стола
## API для создания бронирования
## API для удаления бронирования
## API для получения списка всех бронирований на указанную дату
## API для проверки стола на возможность бронирования на конкретную дату
