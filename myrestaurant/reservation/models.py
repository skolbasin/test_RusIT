from django.core.validators import MaxValueValidator
from django.db.models import (Model,
                              CharField,
                              PositiveIntegerField,
                              ForeignKey,
                              DateTimeField,
                              DurationField,
                              BooleanField,
                              )
from django.db import models
from django.utils.translation import gettext_lazy as _
from .config import validate_contact_info


class Table(Model):
    """
    Модель стола
    """

    class Meta:
        verbose_name = _("Стол")
        verbose_name_plural = _("Столы")

    number = PositiveIntegerField(blank=False, verbose_name=_("Номер стола"))
    place_count = PositiveIntegerField(blank=False,
                                       validators=[MaxValueValidator(10)],
                                       verbose_name=_("Количество мест"))
    free = BooleanField(default=True, verbose_name=_("Свободен"))

    def __str__(self):
        return str(self.number)


class Reservation(Model):
    """
    Модель брони
    """

    class Meta:
        verbose_name = _("Бронь")
        verbose_name_plural = _("Брони")

    date_time = DateTimeField(verbose_name=_("Дата и время"))
    duration = DurationField(verbose_name=_("Продолжительность"))
    table = ForeignKey(Table, on_delete=models.CASCADE, verbose_name=_("Стол"))
    client_info = CharField(max_length=100,
                            validators=[validate_contact_info],
                            verbose_name=_("Контактная информация"))

    def __str__(self):
        return str(self.client_info)


