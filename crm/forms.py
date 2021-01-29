from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class SaleCreateForm(ModelForm):
    class Meta():
        model = Sale
        fields = ('product', 'quantity', 'total_amount')



class SaleUpdateForm(ModelForm):
    class Meta():
        model = Sale
        fields = '__all__'

class CustomerCraeteForm(ModelForm):
    class Meta():
        model = Customer
        exclude = ('owner',)

class UpdateCustomerForm(ModelForm):
    class Meta():
        model = Customer
        fields = '__all__'

class CraeteUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    class Meta():
        model = User
        fields = ('username','email',)

class TargetForm(ModelForm):
    class Meta():
        model = Profile
        fields = ('target',)