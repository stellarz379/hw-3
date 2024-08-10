from django.db import models

from apps.base.contant import ICON

# Create your models here.

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка'

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    icon = models.CharField(
        choices=ICON,
        max_length=155,
        verbose_name='Иконка'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'О нас'