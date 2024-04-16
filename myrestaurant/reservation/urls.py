from django.urls import path

from .views import (CRUDTableAPI,
                    delete_reservation,
                    get_reservations_by_date,
                    check_table_availability,
                    add_reservation
                    )

app_name = 'reservation'


urlpatterns = [
    path('CRUD_table/', CRUDTableAPI.as_view(), name='CRUD_table'),
    path('del_res/', delete_reservation, name='delete_reservation'),
    path('get_res/', get_reservations_by_date, name='get_reservations_by_date'),
    path('add_res/', add_reservation, name='add_reservation'),
    path('check_table/', check_table_availability, name='check_table_availability'),

]
