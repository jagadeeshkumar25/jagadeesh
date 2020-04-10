from django import forms
from HealthAdmin.models import AdminLogin,Disease,Medicine

class AdminForm(forms.ModelForm):
    PASSWORD=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=AdminLogin
        fields="__all__"


class DiseaseForm(forms.ModelForm):
    class Meta:
        model=Disease
        fields="__all__"


class MedicineForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields="__all__"

