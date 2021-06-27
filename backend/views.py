from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "backend/index.html", context)


def signup_view(request):
    if request.POST:
        user_type = request.POST['user_type']
        user2 = request.POST + request.POST
        print(user2)
        
        if user_type == 'Student':
            pass
        else:
            pass
    context={}
    return render(request, "backend/signup.html", context)


def employer_signup_view(request):
    context = {}
    return render(request, "backend/employer-signup.html", context)

def student_signup_view(request):
    context = {}
    return render(request, "backend/student-signup.html", context)