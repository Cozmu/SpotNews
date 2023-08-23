from django.core.exceptions import ValidationError


def validate_composite_title(value):
    list_title = value.split(' ')
    if len(list_title) <= 1:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')


# def validate_date_format(value):
#     if not value or len(value) != 10 or not value[4] == value[7] == '-':
#         raise ValidationError("A data deve estar no formato AAAA-MM-DD.")


