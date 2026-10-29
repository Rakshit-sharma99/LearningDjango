from django import forms
from .models import Emp

class InputForm1(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class InputForm2(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    age= forms.IntegerField()
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    address = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField()


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'