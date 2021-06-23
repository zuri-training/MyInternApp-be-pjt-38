from django.shortcuts import render

# Create your views here.
def home(request):
    params = {}
    return render(request, "backend/index.html", params)

