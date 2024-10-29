from django.urls import path
from .views import CreateTask, GetTasks, GetTask, UpdateTask, DeleteTask

urlpatterns = [
    path('create/',CreateTask.as_view(), name='createtask'),
    path('gettasks/',GetTasks.as_view(), name='gettasks'),
    path('gettask/',GetTask.as_view(), name='gettask'),
    path('update/', UpdateTask.as_view(), name='updatetask'),
    path('delete/', DeleteTask.as_view(), name='deletetask'),
]
