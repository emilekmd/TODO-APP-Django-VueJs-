from django.urls import path
from .views import CreateTask,GetAllTask

urlpatterns = [
    path('create/',CreateTask.as_view(),name='createtask'),
    path('get/',GetAllTask.as_view(),name='gettasks')
]
