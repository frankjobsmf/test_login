from django.urls import path, include

#api.py
from .api import (
    ListAparcamientoAPI,
    ListUserAPI,
    LoginAPI,
    RegisterAPI
)

#knox
from knox import views as knox_views


urlpatterns = [
    path('api/auth', include('knox.urls')),

    #usuario
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view()),
    path('api/auth/user', ListUserAPI.as_view()),

    #aparcamiento
    path('api/auth/aparcamiento', ListAparcamientoAPI.as_view()),

]
