from django.urls import path
from .views import CreateUser,CreateSuperUser
urlpatterns = [
    path('create_user/',CreateUser.as_view(),name='create_user'),
    path('create_super_user/',CreateSuperUser.as_view(),name='create_super_user')
]
