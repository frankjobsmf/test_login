from django.urls import path, include

#api.py
from .api import (
    RegisterAPI
)

#knox
from knox import views as knox_views


urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view()),

]
