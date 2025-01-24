from django import forms
from .models import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade', 'comments']  # Укажите нужные поля


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(
        choices=[('teacher', 'Учитель'), ('student', 'Ученик')],
        widget=forms.RadioSelect, 
        label="Роль"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
