from .models import Task, User
from django.forms import ModelForm, TextInput, Textarea


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": TextInput(attrs={
                'id': 'username',
                'name': 'username',
                'required': 'required',
                'type': 'text',
                'placeholder': 'myusername or mymail@mail.com'
                }),
            "password": TextInput(attrs={
                'id': 'password',
                'name': 'password',
                'required': 'required',
                'type': 'password',
                'placeholder': 'eg. X8df!90EO'
            }),
        }
        pass
    pass


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
        pass
    pass