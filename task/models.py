from django.db import models

class Task(models.Model):
    completed = models.BooleanField(default=False)
    createAt = models.DateTimeField(auto_now_add=True)
    issueAt = models.DateTimeField(auto_now=True, null=True)
    description = models.CharField(max_length=256,blank=True,null=True)
    
    def __str__(self):
        return self.description