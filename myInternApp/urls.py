from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    
    #backend url
    path('', include('backend.urls')),

    #rest framework url
    path('api-auth/', include('rest_framework.urls')),

    #register
    path('api/', include('api.urls')),
]
