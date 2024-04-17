# Тестовое задание для компании RusIT

## Условие
Необходимо написать 2 модели в Django(стол и бронь) и для них API с 7 ендпоинтами. БД через PosgreSQL, развернутое через Docker + Redis для кеширования.


## Как запустить проект
1. Клонировать репозиторий:
```
git clone https://github.com/skolbasin/test_RusIT.git
```
2. Подключите PosgreSQL:
```
docker-compose up -d
```
P.S. для успешной сборки контейнеров у Вас должен быть установлен Docker, docker-compose. Для подключения к БД необходимо установить PosgreSQL и создать БД в pgAdmin, введя хост - localhost, порт - 5432, имя базы данных, имя пользователя и пароль
3. Создайте виртуальное окружение и активируйте его:
- на Windows
```
python -m venv venv
venv/Scripts/activate
```
- на Linux
```
python -m venv venv
source venv/bin/activate
```
4. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
5. Выполнить миграции:
- на Windows
```
python manage.py migrate
```
- на Linux:
```
make migrate
```
5. Создайте суперюзера
- на Windows
```
python manage.py createsuperuser
```
- на Linux:
```
make superuser
```
6. Запустить сервер:
- на Windows
```
python manage.py runserver
```
- на Linux:
```
make run
```
7. После запуска сервера перейдите по адресу http://localhost:8000/admin и введи логин и пароль от суперюзера, чтобы попасть в административную панель
### Автотесты
Для запуска тестов необходимо перейти в директорию с проектом и выполнить команду 
```
python manage.py test
```
## Админка
В проекте настроена админка для удобства работы с моделями(admin.py)

### Главная страница админки
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/2b8b0ba8-1fdb-45fa-be9b-81e395b58bc5)
### Модель стола 
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/4fb8e8e7-b4ec-4dec-b5f4-8df50f829efd)
### Модель брони 
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/1382a81e-23fe-4b4a-bdfa-9b5443981644)

## Работа API через POSTMAN

### API для добавления стола через POST запрос
Чтобы добавить стол, нужно в форму внести данные для поля "number" и "place_count"
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/f93f58db-9b5a-4e65-92e3-2b9b20266470)
Примечание: Добавлена проверка на наличие даного объекта в БД
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/54b4567b-0575-47ed-938d-862e976962f2)

### API для изменения данных о столе
Для внесения изменений нужно указать "table_number" и "place_count"
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/d8316640-9050-487d-87d9-ac6398f2cb50)
Примечание: добавлена проверка на наличие стола в базе и корректность внесения всех данных в форму
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/c137c814-e725-4b16-8753-215453d090ff)
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/a656e836-d774-4b5a-9728-0606fa4a4686)

### API для удаления стола
Реализован через метод класса, но в комментариях есть вариант с использованием отдельным классом. 
Чтобы удалить стол, нужно в методе DELETE В URL через query-параметры указать номер стола 
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/0023fe1d-9a3b-45c2-948a-c8455e1f70ce)
Примечание: добавлена проверка на наличие стола в базе
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/ecc24bfc-bc1f-4597-93c3-112387cb9d05)

### API для создания бронирования
Для добавления брони нужно внести в форму необходимые поля. Ендпоинт отдаст новую запись
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/8bfeb48e-4463-443c-abea-bbf1342052df)
Примечание: добавлена валидация за счет сериализатора
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/f7f16dca-9e61-4fa6-9ee0-6a46e4d2329e)
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/100045d1-9a37-431e-80f8-9026b45c4ec8)

### API для удаления бронирования
Для удаления брони достаточно внести pk в форму
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/9a2af540-ef3f-42ec-a1c2-63b058245cf7)

### API для получения списка всех бронирований на указанную дату
Для получения списка необходимо указать в query-параметрах дату в корректном формате(YYYY-MM-DD)
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/54858592-faab-439e-b78e-944b60a31294)

Примечание: при ошибке в форме даты выдасть ошибку 
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/9538eed0-e3d0-4fd2-acc4-79a376bca90c)

### API для проверки стола на возможность бронирования на конкретную дату
Для проверки необходимо указать в query-параметрах table_id(номер стола) и date в формате(YYYY-MM-DD)
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/1bd4cc0c-c851-4824-a448-68f1ca813775)
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/f2d8312d-0176-49cd-b321-c65ca05e34f0)

Примечание: при отсутствии какого либо из query-параметров выдаст ошибку + отсутсивии стола в БД
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/8546eec2-67d5-48d3-8d66-a9822fce8e50)
![image](https://github.com/skolbasin/test_RusIT/assets/111511890/82530ede-7ba2-4e02-9119-b4c081793e08)

### Redis
В данноим проекте кеширование реализовано для endpoint с информацией о свободных столиках на конкретную дату на 1 час
```
@api_view(['GET'])
def check_table_availability(request: Request) -> Response:
    """
     API для проверки стола на возможность бронирования на конкретную дату
    :param request
    :return: Response
    """
    table_id = request.GET.get('table_id')
    date = request.GET.get('date')

    if not table_id or not date:
        return Response("Не указаны необходимые параметры", status=status.HTTP_400_BAD_REQUEST)

    cache_key = f'table_availability_{table_id}_{date}'
    cached_result = cache.get(cache_key)
    if cached_result is not None:
        return Response(cached_result)

    table_exists = Table.objects.filter(number=table_id).exists()

    if not table_exists:
        return Response("Стол с указанным ID не существует")

    reservations = Reservation.objects.annotate(date=TruncDate('date_time', output_field=DateField())).filter(date=date)
    for reservation in reservations:
        if str(reservation.table) == table_id:
            response = "Стол забронирован на указанную дату"
            cache.set(cache_key, response, timeout=3600) 
            return Response(response)

    response = "Стол свободен для бронирования"
    cache.set(cache_key, response, timeout=3600)  
    return Response(response)
```
