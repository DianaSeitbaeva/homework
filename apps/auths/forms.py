from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from auths.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = (
            'email',
        )