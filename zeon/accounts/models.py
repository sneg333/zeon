from django.db import models
from django.contrib.auth.models import User
from datetime import date
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

class Autor(models.Model):
    title_autor = models.CharField(max_length=100, verbose_name='автор')

    def __str__(self):
        return self.title_autor

    class Meta:
        verbose_name = 'авторы'
        verbose_name_plural = 'автор'

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='название книги')
    iden = models.DecimalField(max_digits=10, decimal_places=0, blank=True, verbose_name='артикль')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='цена')
    autor = models.ManyToManyField(Autor, blank=True, verbose_name='автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

class BookInstance(models.Model):

    LOAN_STATUS = (
        ('m', 'Поддержка'),
        ('o', 'Взаймы'),
        ('a', 'Доступный'),
        ('r', 'Зарезервированна'),
    )
    title = models.CharField(max_length=100, verbose_name='имя пользователя')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='пользователь1')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, verbose_name='книга')
    imprint = models.CharField(max_length=200, verbose_name='отпечаток')
    due_back = models.DateField(null=True, blank=True, verbose_name='должен вернуть')
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

class Pol(models.Model):
    title_pol = models.CharField(max_length=100, verbose_name='пол')

    def __str__(self):
        return self.title_pol

    class Meta:
        verbose_name = 'пол'
        verbose_name_plural = 'пол'

#пользователь
class Profile(models.Model):

    LOAN_STATUS2 = (
        ('мужской', 'мужской'),
        ('женский', 'женский'),
    )

    LOAN_STATUS = (
        ('в отношениях', 'в отношениях'),
        ('свободен', 'свободен'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True, verbose_name='о себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='дата рождения')
    pol = models.CharField(blank=True,choices=LOAN_STATUS2, max_length=100, verbose_name='пол')
    statstar = models.CharField(blank=True, choices=LOAN_STATUS, max_length=100, verbose_name='статус')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профиль пользователя'
