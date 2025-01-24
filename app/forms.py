from django import forms
from .models import Grade, Student

class GradeForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label="Ученик")
    grade = forms.IntegerField(label="Оценка")
    comments = forms.CharField(widget=forms.Textarea, label="Комментарии")

    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade', 'comments']



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
