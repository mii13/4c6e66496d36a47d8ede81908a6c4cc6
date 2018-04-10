import re
from django.core.exceptions import ValidationError


def validate_function(value):
    if not re.match("^[t\d\+\-\*\/]+$", value):
        raise ValidationError('%(value)s bad function',
            params={'value': value},
        )
