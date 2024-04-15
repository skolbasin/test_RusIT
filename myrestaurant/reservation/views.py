from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer


@api_view(['POST'])
def add_table(request):
    """
    API для добавления стола через POST запрос
    :param request
    :return: Response
    """
    serializer = TableSerializer(data=request.data)
    if serializer.is_valid():
        table = serializer.save()
        table.free = False
        table.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_table(request, pk):
    """
    API для изменения данных о столе
    :param request, pk
    :return: Response
    """
    try:
        table = Table.objects.get(pk=pk)
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TableSerializer(table, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_table(request, pk):
    """
    API для удаления стола
    :param request, pk
    :return: Response
    """
    try:
        table = Table.objects.get(pk=pk)
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if table.free:
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("Стол не может быть удален, т.к. занят гостями", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_reservation(request):
    """
    API для создания бронирования
    :param request
    :return: Response
    """
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_reservation(request, pk):
    """
     API для удаления бронирования
    :param request, pk
    :return: Response
    """
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    reservation.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_reservations_by_date(request, date):
    """
     API для получения списка всех бронирований на указанную дату
    :param request, date
    :return: Response
    """
    reservations = Reservation.objects.filter(date_time__date=date)
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def check_table_availability(request, table_id, date):
    """
     API для проверки стола на возможность бронирования на конкретную дату
    :param request, table_id, date
    :return: Response
    """
    try:
        table = Table.objects.get(pk=table_id)
    except Table.DoesNotExist:
        return Response("Стол не найден", status=status.HTTP_404_NOT_FOUND)

    reservations = Reservation.objects.filter(table=table, date_time__date=date)
    if reservations.exists():
        return Response("Стол занят на указанную дату", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Стол доступен для бронирования на указанную дату")