from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

# For User Registration
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# ✅ For Adding/Editing Tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']
