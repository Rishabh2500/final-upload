from django.db import models

# Create your models here.

class hello(models.model1):
    name=models.Charfield(max_length=100)
    city=models.Charfield(max_length=100)

  
class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content