from django.contrib.auth.models import User
from django.core.validators import validate_slug
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_slug
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Gender(models.Model):

    gender_name = models.CharField("Пол", max_length=10)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.gender_name

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Полы"


class Type(models.Model):

    type_name = models.CharField("Вид", max_length=20)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"


class Breed(models.Model):

    type_name = models.ForeignKey(Type, verbose_name='Вид', on_delete=models.CASCADE)
    breed_name = models.CharField("Порода", max_length=10, default="неизвестна")
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.breed_name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Color(models.Model):

    coloring = models.CharField("Окраска", max_length=50)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.coloring

    class Meta:
        verbose_name = "Окрас"
        verbose_name_plural = "Окрасы"


class Photo(models.Model):

    photo_url = models.URLField('Ссылка на фотографию')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Animal(models.Model):

    type_name = models.ForeignKey(Type, verbose_name='Вид', on_delete=models.CASCADE)
    breed_name = models.ForeignKey(Breed, verbose_name='Порода', on_delete=models.CASCADE)
    gender_name = models.ForeignKey(Gender, verbose_name='Пол', on_delete=models.CASCADE)
    coloring = models.ForeignKey(Color, verbose_name='Окрас', on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, verbose_name='Фотография', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"


class AnimalStatus(models.Model):

    animal_status = models.CharField("Статус животного", max_length=20)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.animal_status

    class Meta:
        verbose_name = "Статус животного"
        verbose_name_plural = "Статусы животного"


class Announcement(models.Model):

    animal_id = models.ForeignKey(Animal, verbose_name='Животное', on_delete=models.CASCADE)
    animal_status = models.ForeignKey(AnimalStatus, verbose_name='Статус животного', on_delete=models.CASCADE)
    is_published = models.BooleanField("Опубликовано")
    location = models.CharField("Адрес", max_length=200)
    date = models.DateField("Дата создания")
    creator_info = models.CharField("Контакты создателя", max_length=50)
    extra_info = models.TextField("Дополнительная информация", default='')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
