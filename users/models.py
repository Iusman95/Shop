from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('Ж', 'Женский'),
    )


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete = models.CASCADE)
    image = models.ImageField(upload_to='profile/', default='default.jpg')
    discription = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    tiktok = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user 

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
