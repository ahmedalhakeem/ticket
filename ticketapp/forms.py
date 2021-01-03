from django import forms
from django.forms import ModelForm
from ticketapp.models import User, Department, Section, Problems, ProblemType

#class UserForm(ModelForm):
 #   class meta:
  #      model = User
   #     fields = ('first_name', 'last_name', 'email', 'password', 'pc_code', 'deptartment', 'section' )


class UserForm(forms.Form):
    first_name=forms.CharField(label="", required=True,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'First Name',}))
    last_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Last Name',}))
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Email' ,}))
    password = forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'})
    pc_code = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'enter your PC code',}))
    deptartment = forms.ModelChoiceField(label="",queryset=Department.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control form-control-lg', 'placeholder':'Select Department' }))
    section = forms.ModelChoiceField(label="",queryset=Section.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control form-control-lg', }))



