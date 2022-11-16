from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(verbose_name='username',max_length=255)
    email = models.EmailField(verbose_name='email',max_length=255)
    password = models.CharField(verbose_name='password',max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']