from django.shortcuts import render, redirect
from .forms import GradeForm
from .models import Grade

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.teacher = request.user.teacher
            grade.save()
            return redirect('home')
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
            user = form.save(commit=False)
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



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
