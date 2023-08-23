from django.core.exceptions import ValidationError
from datetime import datetime


def validate_composite_title(value):
    list_title = value.split(' ')
    if len(list_title) <= 1:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')


def validate_date_format(value):
    try:
        datetime.strptime(str(value), "%Y-%m-%d")
    except ValueError:
        raise ValidationError(f'O valor {value} tem um formato de data inválido. Deve ser no formato YYYY-MM-DD.')

