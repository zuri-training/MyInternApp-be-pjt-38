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


    # profile
    path("student-profile/", student_profile_view, name="student-profile-url"),
    path("employer-profile/", employer_profile_view, name="employer-profile-url"),

    #explore-student
    path('explore-student/', explore_student_view, name='explore-student-url'),

    #explore-job
    path('explore-job/', explore_job_view, name='explore-job-url'),

    path("upload-job/", upload_job_view, name="upload-job-url"),
    path("student-upload-work/", upload_work_view, name="student-upload-work-url"),
]

