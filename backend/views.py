from backend.models import GeneralRegistration, StudentRegistration
from django.shortcuts import render, redirect
from .forms import GeneralRegistrationForm, StudentRegistrationForm, EmployerRegistrationForm, CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home_view(request):
    context = {}
    return render(request, "backend/index.html", context)


def signup_view(request):
    if request.POST:
        general_user_info = request.POST
        form = GeneralRegistrationForm(general_user_info)
        if form.is_valid():
            form.save()
            print('user saved')
        else:
            print(form.errors)
            print('There was an error')
        print('View finished')

        if request.POST['user_type'] == 'Student':
            return redirect('student-signup-url')
        else:
            return redirect('employer-signup-url')
        

    context={}
    return render(request, "backend/signup.html", context)


def student_signup_view(request):
    if request.POST:
        general_info=GeneralRegistration.objects.all().last()
        # general_info_first_name = general_info.first_name
        # general_info_last_name = general_info.last_name
        updated_request = request.POST.copy()
        updated_request.update({'general_info' : general_info})
        print(request.POST)
        form = StudentRegistrationForm(updated_request)
        
        print('this is the last' + str(general_info))
        user_form = CreateUserForm()
        if form.is_valid():
            form.save()
            print('Student Saved')

            user_details = {
                'username': request.POST['email'],
                'email': request.POST['email'],
                # 'first_name': general_info_first_name,
                # 'last_name': general_info_last_name,
                'password1': request.POST['password1'],
                'password2': request.POST['password2'],
            }

            user_form = CreateUserForm(user_details)

            if user_form.is_valid():
                user_form.save()
                print('A user has been created')

                user = User.objects.get(email = user_details['email'])
                student_group = Group.objects.get(name='student')
                
                user.groups.add(student_group)
                
                print('User has been added to group')
                return redirect('login-url')
            else:
                print(user_form.errors)

        else:
            print(form.errors)
            print('Student not saved')
    context = {
    }
    return render(request, "backend/student-signup.html", context)

def employer_signup_view(request):
    if request.POST:

        general_info=GeneralRegistration.objects.all().last()
        updated_request = request.POST.copy()
        updated_request.update({'general_info' : general_info})
        print(request.POST)
        form = EmployerRegistrationForm(updated_request)
        
        print('this is the last' + str(general_info))
        user_form = CreateUserForm()
        if form.is_valid():
            form.save()
            print('New User saved')

            user_details = {
                'username': request.POST['email'],
                'email': request.POST['email'],
                'password1': request.POST['password1'],
                'password2': request.POST['password2'],
            }

            user_form = CreateUserForm(user_details)

            if user_form.is_valid():
                user_form.save()
                print('A user has been created')

                user = User.objects.get(email = user_details['email'])
                employer_group = Group.objects.get(name='employer')
                
                user.groups.add(employer_group)
                
                print('User has been added to group')
                return redirect('login-url')
            else:
                print(user_form.errors)

        else:
            employer_form_errors = form.errors
            print(employer_form_errors)
            print('Student not saved')
    
    context = {
        # 'employer_form_errors':employer_form_errors,
    }
    return render(request, "backend/employer-signup.html", context)

def login_view(request):
    if request.method == "POST":
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

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
    user = request.user
    user_detail = User.objects.get(email = user.email)
    print(user_detail)
    context= {
        'user':user_detail,
    }
    return render(request, "backend/student-homepage.html", context)

def employer_homepage_view(request):
    user = request.user
    user_detail = User.objects.get(email = user.email)
    context= {
        'user':user_detail,
    }
    return render(request, "backend/employer-homepage.html", context)


def logout_view(request):
    logout(request)
    return redirect('login-url')