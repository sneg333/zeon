from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

############################# СОБЫТИЕ #################################
class Sobitie(models.Model):
    title = models.CharField(max_length=150, blank=True)
    body = RichTextUploadingField(blank=True, default='', verbose_name='текст события')
    vrem_sobitie = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'события'
        verbose_name_plural = 'события'