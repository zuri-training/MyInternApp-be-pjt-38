from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.api import error
from backend.models import StudentRegistration, EmployerRegistration
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, EmployerRegistrationForm, CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home_view(request):
    context = {}
    return render(request, "backend/index.html", context)


def student_signup_view(request):
    if request.POST:
        data = request.POST
        form = StudentRegistrationForm(data)
        if form.is_valid():
            

            user_creation_details = {
                'username'  : data.get('email'),
                'email'     : data.get('email'),
                'password1' : data.get('password1'),
                'password2' : data.get('password2')
            }

            user_creation_form = CreateUserForm(user_creation_details)
            if user_creation_form.is_valid():
                user_creation_form.save()
                print('New User Created')

                form.save()
                print('New student registered')

                user = User.objects.get(username=user_creation_details['username'])
                student_group = Group.objects.get(name='student')
                user.groups.add(student_group)
                print('Student added to student group')

                messages.success(request, 'Account created, please login in')
                return redirect('login-url')
            else:
                print(user_creation_form.errors)
        else:
            print(form.errors)

    context = {
    }
    return render(request, "backend/student-signup.html", context)

def employer_signup_view(request):
    if request.POST:
        data = request.POST
        form = EmployerRegistrationForm(data)
        if form.is_valid():
            

            user_creation_details = {
                'username'  : data.get('email'),
                'email'     : data.get('email'),
                'password1' : data.get('password1'),
                'password2' : data.get('password2')
            }

            user_creation_form = CreateUserForm(user_creation_details)
            if user_creation_form.is_valid():
                user_creation_form.save()
                print('New User Created')

                form.save()
                print('New Employer registered')

                user = User.objects.get(username=user_creation_details['username'])
                employer_group = Group.objects.get(name='employer')
                user.groups.add(employer_group)
                print('Employer added to employer group')

                messages.success(request, 'Account created, please login in')
                return redirect('login-url')
            else:
                print(user_creation_form.errors)
        else:
            print(form.errors)       
    
    context = {
        # 'employer_form_errors':employer_form_errors,
    }
    return render(request, "backend/employer-signup.html", context)

def login_view(request):
    if request.method == "POST":
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        print(user_email)
        print(user_password)

        user = authenticate(request, username=user_email, password=user_password)
        
        if user is not None:
            login(request, user)
            if user.groups.filter(name = 'student').exists():
                return redirect("student-homepage-url")
            else:
                return redirect("employer-homepage-url")
        else: 
            messages.info(request, "Username or password is incorrect")
            print(messages)

    context = {

    }
    return render(request, "backend/login.html", context)


def student_homepage_view(request):
    # Get the logged in in student email
    student_email = request.user.email
    
    # use the email to search for student details in the StudentRegistration
    student_detail = StudentRegistration.objects.get(email = student_email)
    
    context= {
        'student_detail': student_detail,
    }
    return render(request, "backend/student-homepage.html", context)

def employer_homepage_view(request):
    # Get the logged in Employer email
    employer_email = request.user.email
    
    # use the email to search for student details in the StudentRegistration
    employer_detail = EmployerRegistration.objects.get(email = employer_email)

    context= {
        'employer_detail':employer_detail,
    }
    return render(request, "backend/employer-homepage.html", context)


def logout_view(request):
    logout(request)
    return redirect('login-url')