from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/",include("task.urls")),
    path("account/",include("account.urls")),
]