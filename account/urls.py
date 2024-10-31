from django.urls import path
from .views import CreateUser,CreateSuperUser,LoginUser,LogoutUser

urlpatterns = [
    path('create_user/',CreateUser.as_view(),name='create_user'),
    path('create_super_user/',CreateSuperUser.as_view(),name='create_super_user'),
    path('login/',LoginUser.as_view(),name='loginUser'),
    path('logout/', LogoutUser.as_view(), name='LogoutUser')
]
