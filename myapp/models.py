from django.db import models

class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название сайта")
    logo = models.ImageField(upload_to='static/images/', verbose_name="Логотип")
    description = models.TextField(verbose_name="Описание сайта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
