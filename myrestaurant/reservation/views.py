import datetime

from django.db.models import DateField
from django.db.models.functions import TruncDate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Table, Reservation
from .serializers import ReservationSerializer


class CRUDTableAPI(APIView):
    def post(self, request: Request) -> Response:
        """
        API для добавления стола через POST запрос
        :param request
        :return: Response
        """
        number = request.data.get('number')
        place_count = request.data.get('place_count')

        if not number or not place_count:
            return Response("Необходимо указать номер стола и количество мест",
                            status=status.HTTP_400_BAD_REQUEST)

        table_exists = Table.objects.filter(number=number).exists()
        if table_exists:
            return Response(f"Стол с номером {number} уже существует в базе данных",
                            status=status.HTTP_400_BAD_REQUEST)

        table = Table.objects.create(number=number, place_count=place_count, free=True)

        return Response(f"Стол №{number}({place_count} мест(о)) успешно создан",
                        status=status.HTTP_201_CREATED)

    def put(self, request: Request) -> Response:
        """
        API для изменения данных стола по его ID
        :param request
        :return: Response
        """
        try:
            table_number = request.data.get('table_number')
            place_count = request.data.get('place_count')
            table = Table.objects.get(number=table_number)
            if place_count is not None:
                table.place_count = place_count
                table.save()
                return Response(f"Количество мест у стола №{table_number} успешно изменено на {place_count}",
                                status=status.HTTP_200_OK)
            else:
                return Response("Необходимо указать новое количество мест для изменения",
                                status=status.HTTP_400_BAD_REQUEST)
        except Table.DoesNotExist:
            return Response("Стол с указанным номером не найден", status=status.HTTP_404_NOT_FOUND)

    def delete(self, table_number) -> Response:
        """
        API для удаления стола по его ID
        :param table_number
        :return: Response
        """
        try:
            table_number = self.request.query_params.get('table_number')
            table = Table.objects.get(number=str(table_number))
            table.delete()
            return Response(f"Стол №{table_number} успешно удален", status=status.HTTP_200_OK)
        except Table.DoesNotExist:
            return Response(f"Стол №{table_number} не найден", status=status.HTTP_404_NOT_FOUND)


# второй способ реализации метода DELETE для столов
# @api_view(['DELETE'])
# def delete_table(request, pk):
#     """
#     API для удаления стола
#     :param request, pk
#     :return: Response
#     """
#     try:
#         table = Table.objects.get(pk=pk)
#     except Table.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if table.free:
#         table.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response("Стол не может быть удален, т.к. занят гостями", status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_reservation(request: Request) -> Response:
    """
     API для удаления бронирования
    :param request
    :return: Response
    """
    try:
        pk = request.data.get('res_number')
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(f'Бронь с номером {pk} не найдена в системе', status=status.HTTP_404_NOT_FOUND)

    reservation.delete()
    return Response(f'Бронь №{pk} успешно удалена', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_reservation(request: Request) -> Response:
    """
     API для добавления новой брони
    :param request
    :return: Response
    """
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_reservations_by_date(request: Request) -> Response:
    """
     API для получения списка всех бронирований на указанную дату
    :param request
    :return: Response
    """
    date = request.GET.get('date')
    try:
        date_time = datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return Response({'error': 'Некорректный формат даты. Укажите в формате YYYY-MM-DD'},
                        status=status.HTTP_400_BAD_REQUEST)

    reservations = Reservation.objects.filter(date_time__date=date_time)
    serialized_reservations = ReservationSerializer(reservations, many=True)

    return Response(serialized_reservations.data, status=status.HTTP_200_OK)


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

    table_exists = Table.objects.filter(number=table_id).exists()

    if not table_exists:
        return Response("Стол с указанным ID не существует")

    reservations = Reservation.objects.annotate(date=TruncDate('date_time', output_field=DateField())).filter(date=date)
    print(reservations)
    for reservation in reservations:
        if str(reservation.table) == table_id:
            return Response("Стол забронирован на указанную дату")

    return Response("Стол свободен для бронирования")

