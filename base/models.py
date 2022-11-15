from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null= True, blank=True)
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    created  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
        
    class Meta:
        order_with_respect_to = 'user'
    
    def clean(self):
        if not len(self.title) > 10:
            raise ValidationError(
                {'title': "Title should have at least 10 letters"})