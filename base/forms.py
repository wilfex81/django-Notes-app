from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['data-toggle'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password1'].widget.attrs['data-toggle'] = 'Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small><br>Enter the same password as before, for verification.</small></span>'	


