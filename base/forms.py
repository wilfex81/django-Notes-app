from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()


def validate_password_strength(value):
    """Validates that the password is at leats 7 charcters long 
    and has atleats 1 digit and 1 letter
    """
    min_length = 7

    if len(value) < min_length:
        raise ValidationError('Password must be at least {0} characters '
                            'long.').format(min_length)

    # check for digit
    if not any(char.isdigit() for char in value):
        raise ValidationError('Password must contain at least 1 digit.')

    #check for letter
    if not any(char.isalpha() for char in value):
        raise ValidationError('Password must contain at least 1 letter.')

class MySetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MySetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].validators.append(validate_password_strength)

