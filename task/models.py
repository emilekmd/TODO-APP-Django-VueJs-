from django.db import models
from django.conf import settings

class Task(models.Model):
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    issue_at = models.DateTimeField(auto_now=True, null=True)
    description = models.CharField(max_length=256,blank=True,null=True, unique=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.description}____(id : {self.id})"