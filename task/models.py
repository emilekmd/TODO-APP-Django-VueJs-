from django.db import models
from django.conf import settings

class Cathegorie(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    issue_at = models.DateTimeField(auto_now=True, null=True)
    description = models.CharField(max_length=256,blank=True,null=True, unique=True)
    
    cathegorie = models.ForeignKey(Cathegorie,on_delete=models.CASCADE,null=True,default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.description}____(id : {self.id})"