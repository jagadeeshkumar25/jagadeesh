
from django.db import models

class RgistrationModel(models.Model):
    First_Name=models.CharField(max_length=30,unique=True)
    Last_Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    UserName=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)


class UserAdmin(models.Model):
    USERNAME=models.CharField(max_length=30,unique=True)
    PASSWORD=models.CharField(max_length=30)


from  django import forms

class UserLoginForm(forms.ModelForm):
    PASSWORD=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=UserAdmin
        fields="__all__"

