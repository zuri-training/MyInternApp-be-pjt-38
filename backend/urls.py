from django.urls import path, include

from .views import *
urlpatterns = [
    path("", home_view, name="homepage"),
    path("employer-signup/", employer_signup_view, name="employer-signup-url"),
    path("student-signup/", student_signup_view, name="student-signup-url"),
    path("login/", login_view, name="login-url"),
    path("logout/", logout_view, name="logout-url"),
    path("employer-homepage/", employer_homepage_view, name="employer-homepage-url"),
    path("student-homepage/", student_homepage_view, name="student-homepage-url"),
]

