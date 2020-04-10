import re
from django import forms
from useradmin.models import RgistrationModel

class RegistrationForm(forms.ModelForm):
    gen=(
        ('MALE','Male'),
        ('FEMALE','Female')
    )
    Gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    Password=forms.CharField(widget=forms.PasswordInput)
    def clean_First_Name(self):
        first=self.cleaned_data['First_Name']
        if len(first)>=4:
            return first
        else:
            return forms.ValidationError("invalid name")
    # def clean_First_Name(self):
    #     first_name=self.cleaned_data['First_Name']
    #     res=re.findall(r'[a-z,A-Z]*$',first_name)
    #     if res :
    #         return first_name
    #     else:
    #         raise  forms.ValidationError("name must be in upper or lower letters only and min charcters 4")
    #
    # def clean_Last_Name(self):
    #     last_name = self.cleaned_data['Last_Name']
    #     res=re.findall(r'[a-z,A-Z]*$',last_name)
    #     if res :
    #         return last_name
    #     else:
    #      raise forms.ValidationError("name must be in upper or lower letters only and min charcters 4 ")
    #
    # def clean_UserName(self):
    #     un = self.cleaned_data['UserName']
    #     res=re.findall(r'[a-z,A-Z]*$',un)
    #     if res:
    #         return un
    #     else:
    #         raise forms.ValidationError("name must be in upper or lower letters only and min charcters 4 ")
    #

    class Meta:
        model=RgistrationModel
        fields="__all__"
