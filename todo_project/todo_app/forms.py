from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs): #constructor basic class
        super().__init__(*args, **kwargs) # auto actions
        self.fields['cat'].empty_label = "День/Неделя/Месяц" # empty field in list

    class Meta:
        model = Task
        fields = ('title','description','cat')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class EditForm(ModelForm):
    def __init__(self, *args, **kwargs): #constructor basic class
        super().__init__(*args, **kwargs) # auto actions
        self.fields['cat'].empty_label = "День/Неделя/Месяц" # empty field in list
    class Meta:
        model = Task
        fields = ('title', 'description', 'cat', 'complete')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }



class Register(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(Register, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
