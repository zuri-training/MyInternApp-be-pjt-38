from backend.models import GeneralRegistration
from django.shortcuts import render, redirect
from .forms import GeneralRegistrationForm, StudentRegistrationForm, EmployerRegistrationForm, CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


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
            else:
                print(user_form.errors)

        else:
            print(form.errors)
            print('Student not saved')
    context = {
    }
    return render(request, "backend/student-signup.html", context)

def employer_signup_view(request):
    print('i am outside the request')
    if request.POST:
        print('i am now inside the request')
        print(request.POST)
    print('Done')
    # if request.POST:

    #     general_info=GeneralRegistration.objects.all().last()
    #     updated_request = request.POST.copy()
    #     updated_request.update({'general_info' : general_info})
    #     print(request.POST)
    #     form = EmployerRegistrationForm(updated_request)
        
    #     print('this is the last' + str(general_info))
    #     user_form = CreateUserForm()
    #     if form.is_valid():
    #         form.save()
    #         print('New User saved')

    #         user_details = {
    #             'username': request.POST['email'],
    #             'email': request.POST['email'],
    #             'password1': request.POST['password1'],
    #             'password2': request.POST['password2'],
    #         }

    #         user_form = CreateUserForm(user_details)

    #         if user_form.is_valid():
    #             user_form.save()
    #             print('A user has been created')

    #             user = User.objects.get(email = user_details['email'])
    #             student_group = Group.objects.get(name='student')
                
    #             user.groups.add(student_group)
                
    #             print('User has been added to group')
    #         else:
    #             print(user_form.errors)

    #     else:

    #         print(form.errors)
    #         print('Student not saved')
    
    context = {}
    return render(request, "backend/employer-signup.html", context)

