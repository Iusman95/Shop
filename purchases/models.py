from tabnanny import verbose
from django.db import models



class Posts(models.Model):
    user = models.ForeignKey('users.User', verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='photo/', verbose_name="Фото")
    title = models.CharField(max_length=60, blank=False, null = False, verbose_name="Заголовок")
    body = models.TextField(null = True, verbose_name="Описание")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")
    avtor_informations = models.TextField(null = True, verbose_name="Информация о пользователе")
    

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

