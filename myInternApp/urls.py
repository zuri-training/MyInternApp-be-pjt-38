from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    
    #backend url
    path('', include('backend.urls')),

    #rest framework url
    path('api-auth/', include('rest_framework.urls')),

    #register
    path('api/', include('api.urls')),
]
