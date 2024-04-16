from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Table, Reservation


class TestCRUDTableAPI(APITestCase):
    def setUp(self):
        self.table = Table.objects.create(number=1, place_count=4, free=True)
        self.reservation = Reservation.objects.create(date_time=timezone.now(),
                                                      duration=timedelta(seconds=3600),
                                                      table=self.table,
                                                      client_info='Jane 8888')

    def test_create_table(self):
        url = reverse('reservation:CRUD_table')
        data = {'number': 2, 'place_count': 4}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_table(self):
        url = reverse('reservation:CRUD_table')
        data = {'table_number': 1, 'place_count': 6}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_table(self):
        url = reverse('reservation:CRUD_table') + f'?table_number=1'
        data = {'table_number': '1'}
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_reservation(self):
        url = reverse('reservation:add_reservation')
        data = {'date_time': '2024-04-16T18:42:28+00:00',
                'duration': timedelta(seconds=3600),
                'table': self.table.pk,
                'client_info': 'John 8888'
                }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_reservation(self):
        url = reverse('reservation:delete_reservation')
        data = {'res_number': self.reservation.pk}
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_reservations_by_date(self):
        url = reverse('reservation:get_reservations_by_date')
        date = datetime.now().strftime('%Y-%m-%d')
        response = self.client.get(url, {'date': date})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_table_availability(self):
        url = reverse('reservation:check_table_availability')
        data = {'table_id': 1, 'date': datetime.now().strftime('%Y-%m-%d')}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
