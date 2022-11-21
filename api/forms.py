from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email','firstName', 'lastName','password')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email','firstName', 'lastName','password')