from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Courses(models.Model):
    name = models.CharField("Наименование курса", default='', max_length = 80)
    description = models.TextField("Описание")
    cost = models.CharField("Цена", default='', max_length = 180)
    hours = models.CharField("Часы", default='', max_length = 180)
    background = models.ImageField("Фон", upload_to="annex/img/%Y/%m/%d", default='')

    def __str__(self):
        return self.name

    class Meta:
      verbose_name = "Курсы"
      verbose_name_plural = "Курсы"

class GalleryAdmin(models.Model):
    name = models.CharField("Наименование картинки", default='', max_length = 80)
    background = models.ImageField("Изображение", upload_to="annex/img/%Y/%m/%d", default='')

    def __str__(self):
        return self.name

    class Meta:
      verbose_name = "Галерея"
      verbose_name_plural = "Галерея"

class News(models.Model):
    name = models.CharField("Наименование новости", default='', max_length = 80)
    description = models.TextField("Описание")
    background = models.ImageField("Фон", upload_to="annex/img/%Y/%m/%d", default='')

    def __str__(self):
        return self.name

    class Meta:
      verbose_name = "Новости"
      verbose_name_plural = "Новости"

class EventAdmin(models.Model):
    name = models.CharField("Наименование мероприятия", default='', max_length = 80)
    description = models.TextField("Описание")
    date_push = models.DateTimeField("Дата провендения")
    background = models.ImageField("Фон", upload_to="annex/img/%Y/%m/%d", default='')

    def __str__(self):
        return self.name

    class Meta:
      verbose_name = "Мероприятия"
      verbose_name_plural = "Мероприятия"

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Сотрудник', on_delete=models.CASCADE)
    #factory_associate = models.ForeignKey(Factory, blank=True,null=True,default=None, verbose_name=u'Завод', on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", upload_to="annex/img/%Y/%m/%d", default='annex/img/avatar_big.png', null=True)

    def __str__(self):
        return self.user.username

    class Meta:
      verbose_name = "Сотрудники"
      verbose_name_plural = "Сотрудники"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
