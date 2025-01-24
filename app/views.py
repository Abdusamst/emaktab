from django.shortcuts import render, redirect
from .forms import GradeForm
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades_list')  
    else:
        form = GradeForm()
    return render(request, 'add_grade.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            if role == 'teacher':
                user.is_teacher = True
            elif role == 'student':
                user.is_student = True
            user.save()

            login(request, user)

            return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return render(request, 'home_teacher.html')
        elif request.user.is_student:
            return render(request, 'home_student.html')
    else:
        return redirect('login')


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'  
