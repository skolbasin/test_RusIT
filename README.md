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
Чтобы добавить стол, нужно в форму внести данные для поля "number" и "place_count"
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/f93f58db-9b5a-4e65-92e3-2b9b20266470)
Примечание: Добавлена проверка на наличие даного объекта в БД
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/54b4567b-0575-47ed-938d-862e976962f2)

## API для изменения данных о столе
Для внесения изменений нужно указать "table_number" и "place_count"
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/d8316640-9050-487d-87d9-ac6398f2cb50)
Примечание: добавлена проверка на наличие стола в базе и корректность внесения всех данных в форму
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/c137c814-e725-4b16-8753-215453d090ff)
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/a656e836-d774-4b5a-9728-0606fa4a4686)

## API для удаления стола
Реализован через метод класса, но в комментариях есть вариант с использованием отдельным классом. 
Чтобы удалить стол, нужно в методе DELETE В URL через query-параметры указать номер стола 
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/0023fe1d-9a3b-45c2-948a-c8455e1f70ce)
Примечание: добавлена проверка на наличие стола в базе
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/ecc24bfc-bc1f-4597-93c3-112387cb9d05)


## API для создания бронирования
## API для удаления бронирования
## API для получения списка всех бронирований на указанную дату
## API для проверки стола на возможность бронирования на конкретную дату
