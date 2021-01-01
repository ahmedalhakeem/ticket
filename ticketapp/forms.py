from django import forms
from ticketapp.models import User, Department, Section, Problems, ProblemType


class UserForm(forms.Form):
    first_name=forms.CharField(title="", required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}))
    last_name = forms.CharField(title="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}))
    email = forms.EmailField(title="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placrholder':'Email' ,}))
    password = forms.PasswordInput(title="", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Password',}))
    pc-code = forms.CharField(title="", required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your PC code',}))
    deptartment = forms.ModelChoiceField(queryset=Department.objects.all(), required=True)
    section = forms.ModelChoiceField(queryset=Section.objects.all(), required=True)



