from django.urls import path, include

from .views import home_view, employer_signup_view, student_signup_view, signup_view

urlpatterns = [
    path("", home_view, name="home"),
    path("employer-signup/", employer_signup_view, name="employer-signup-url"),
    path("student-signup/", student_signup_view, name="student-signup-url"),
    path("signup/", signup_view, name="signup-url"),
]
