from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . models import UserPredictModel

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserPredictDataForm(forms.ModelForm):
    
    class Meta:
        model = UserPredictModel
        fields = '__all__'