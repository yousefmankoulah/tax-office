from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_file(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=300)
    file_upload = models.FileField()
    
    class Meta:
        ordering = ('user',)

    def __str__(self):
        return '{}'.format(self.user)