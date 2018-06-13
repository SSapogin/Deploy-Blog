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

class Factory(models.Model):
    name = models.CharField("Наименование завода", default='Тимфорт', max_length = 80)
    adress = models.CharField("Адрес", default='г. Оренбург, Россия, 460006', max_length = 180)
    background = models.ImageField("Фон", upload_to="annex/img/%Y/%m/%d", default='')

    def __str__(self):
        return self.name

    class Meta:
      verbose_name = "Все заводы"
      verbose_name_plural = "Все заводы"

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Сотрудник', on_delete=models.CASCADE)
    associate = models.ForeignKey(Company,blank=True,null=True,default=None, verbose_name=u'Компания', on_delete=models.CASCADE)
    factory_associate = models.ForeignKey(Factory, blank=True,null=True,default=None, verbose_name=u'Завод', on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", upload_to="annex/img/%Y/%m/%d", default='annex/img/avatar_big.png', null=True)
    choices_role = (
        ('M', 'Менеджер'),
        ('L', 'Логист'),
        ('Z', 'Завод'),
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

class Specification(models.Model):
    user = models.ForeignKey(User, verbose_name=u"Пользователь", blank=True, null=True, on_delete=models.CASCADE)
    associate = models.ForeignKey(Company, verbose_name=u'Компания', on_delete=models.CASCADE)
    factory_associate = models.ForeignKey(Factory, verbose_name=u'Завод', on_delete=models.CASCADE)
    name = models.CharField("Наименование спецификации проекта", default='', max_length = 180)
    etash = models.CharField("Этаж", default='', max_length = 10)
    date_push = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.associate.name + " - " + self.factory_associate.name + " / " + self.name

    class Meta:
      verbose_name = "Спецификации"
      verbose_name_plural = "Спецификации"

class Materials(models.Model):
    specification = models.ForeignKey(Specification, verbose_name=u'Спецификация', on_delete=models.CASCADE)
    markirovka = models.CharField("Маркировка изделия", default='', max_length = 180)
    count = models.CharField("Кол-во", default='', max_length = 10)
    width = models.CharField("Ширина", default='', max_length = 10)
    height = models.CharField("Высота", default='', max_length = 10)
    weight = models.CharField("Толщина", default='', max_length = 10)
    amount = models.CharField("Объем изделия, м3", default='', max_length = 10)
    area = models.CharField("Площадь штукатурки, м2", default='', max_length = 10)

    def __str__(self):
        return self.specification.name + " - " + self.markirovka

    class Meta:
      verbose_name = "Данные по спецификации"
      verbose_name_plural = "Данные по спецификации"

class Editmaterials(models.Model):
    associate = models.ForeignKey(Materials, verbose_name=u'Материал', on_delete=models.CASCADE)
    count = models.CharField("Кол-во выполненных", default='', max_length = 80)

    def __str__(self):
        return self.associate.specification.name + ' || ' + self.associate.markirovka

    class Meta:
      verbose_name = "Выполненные материалы"
      verbose_name_plural = "Выполненные материалы"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
