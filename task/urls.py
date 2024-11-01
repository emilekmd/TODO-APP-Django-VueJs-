from django.urls import path
from .views import CreateTask, GetTasks, GetTask, UpdateTask, DeleteTask
from .views import CreateCathegorie,DeleteCathegorie,UpdateCathegorie

urlpatterns = [
    path('createtask/',CreateTask.as_view(), name='createtask'),
    path('gettasks/',GetTasks.as_view(), name='gettasks'),
    path('gettask/',GetTask.as_view(), name='gettask'),
    path('updatetask/', UpdateTask.as_view(), name='updatetask'),
    path('deletetask/', DeleteTask.as_view(), name='deletetask'),
    
    path('createcathegorie/',CreateCathegorie.as_view(),name='createcathegorie'),
    path('updatecathegorie/',UpdateCathegorie.as_view(),name='updatecathegorie'),
    path('deletecathegorie/',DeleteCathegorie.as_view(),name='deletecathegorie'),
]
