from django.db import models

# Create your models here.

class Studen(models.Model):
    name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.name} {self.last_name} | email: {self.email}'
    