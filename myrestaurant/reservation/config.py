import re
from django.db import models
from django.core.exceptions import ValidationError


def validate_contact_info(value):
    """
    Валидация наличие имени и телефона
    :param value:
    :return: ValidationError
    """
    pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z]+\s+\d+$')
    if not pattern.match(value):
        raise ValidationError(
            'Необходимо указать номер телефона и имя клиента.'
        )



