from django.db import models


class Muser(models.Model):
    user_name = models.CharField(max_length=100)
    user_mail = models.EmailField(max_length=100)
    user_content = models.TextField()
    password = models.DecimalField(max_digits=10, decimal_places=0, blank=True, verbose_name='пароль')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
