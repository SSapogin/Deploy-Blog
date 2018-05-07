from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Company(models.Model):
    user = models.ForeignKey(User, verbose_name=u"Директор", blank=True, null=True, on_delete=models.CASCADE)
    full_name = models.CharField("Полное наименование компании", default='ООО СТРОИТЕЛЬНАЯ КОМПАНИЯ «Дома в Оренбурге»', max_length = 180)
    name = models.CharField("Краткое название компании", default='Тимфорт', max_length = 80)
    adress = models.CharField("Адрес", default='г. Оренбург, Россия, 460006', max_length = 180)
    phone = models.CharField("Телефон", default='(3532) 37-62-97', max_length = 180)
    email = models.CharField("Электронная почта", default='manager@doma-v-orenburge.ru', max_length = 180)
    background = models.ImageField("Фон", upload_to="annex/img/%Y/%m/%d", default='')

    def __str__(self):
        return self.name
        return self.city

    class Meta:
      verbose_name = "Все компании"
      verbose_name_plural = "Все компании"

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Сотрудник', on_delete=models.CASCADE)
    associate = models.ForeignKey(Company,blank=True,null=True,default=None, verbose_name=u'Компания', on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", upload_to="annex/img/%Y/%m/%d", default='annex/img/avatar_big.png', null=True)
    choices_role = (
        ('M', 'Менеджер'),
        ('P', 'Директор - партнер'),
        ('D', 'Директор'),
    )
    role = models.CharField('Роль', max_length=1, choices=choices_role, default=choices_role[1][1])

    def __str__(self):
        return self.user.username

    class Meta:
      verbose_name = "Сотрудники"
      verbose_name_plural = "Сотрудники"

class Work(models.Model):
    associate = models.ForeignKey(Company,blank=True,null=True,default=None, verbose_name=u'Компания', on_delete=models.CASCADE)
    name = models.CharField("Наименование", default='', max_length = 180)
    composition = models.TextField("Состав работ и затрат")
    unit = models.CharField("Ед. изм", default='', max_length = 30)
    price = models.CharField("Цена за ед.", default='', max_length = 20)

    def __str__(self):
        return self.associate.name + " - " + self.name

    class Meta:
      verbose_name = "Виды работ компании"
      verbose_name_plural = "Виды работ компании"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
