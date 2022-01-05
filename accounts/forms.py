from django import forms
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth import login,authenticate
from  django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse,reverse_lazy





class RegisterForm(UserCreationForm):
    username =forms.CharField(min_length=3 ,max_length=50)
    email =forms.EmailField()
    password1 =forms.CharField(min_length=8 ,max_length=100,widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8,max_length=100, widget=forms.PasswordInput)
    
    class Meta:
        model =User
        fields =["username","email","password1","password2"]


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        username_objects  =User.objects.filter(username=username)

        if username_objects.count():
            print(username)
            raise ValidationError ("Username already exist. ")

        return  username


    def clean_password2(self):
        password2 =self.cleaned_data['password1']
        password1 =self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError( "Passwords do not match.")

        return password2



