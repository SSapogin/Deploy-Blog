from django.db import models

class posts(models.Model):
    title = models.CharField("Название тура", max_length = 80)
    star = models.IntegerField("Количество звезд", default='5')
    city = models.CharField("Город", max_length = 50, default='Оренбург')
    country = models.CharField("Страна", max_length = 50, default='Россия')
    first_cena = models.IntegerField("Цена без учета скидки", default='')
    last_cena = models.IntegerField("Цена с учетом скидки")
    skidka = models.IntegerField("Процент скидки", default='')
    date_night = models.CharField("Дата вылета/кол-во ночей", max_length = 50, default='16 янв, 6 ночей')
    vilet = models.CharField("Город вылета", max_length = 50, default='Оренбурга')
    photo = models.ImageField("Обложка", upload_to="posts/img", default="")
    date = models.DateTimeField("Дата публикации")

    program_tura = models.CharField("Программа тура", max_length = 150, default='Краснодарский край (а/п Адлер)')
    persons = models.CharField("Кол-во человек", max_length = 50, default='2 взрослых')
    tour_room = models.CharField("Описание номера в отеле", max_length = 150, default='2-местный стандарт 2 категории')
    tour_meal = models.CharField("Тип питания в отеле", max_length = 150, default='RO - Без питания')
    type_otdyh = models.CharField("Тип отдыха", max_length = 100, default='Активный отдых')
    comments = models.TextField("Комментарии наших менеджеров", blank=True)
    common_info = models.TextField("Общая информация", blank=True)
    territory = models.TextField("Территория отеля", blank=True)
    in_hotel = models.TextField("В номере", blank=True)
    services = models.TextField("Услуги", blank=True)
    free_services = models.TextField("Бесплатные услуги", blank=True)
    pay_services = models.TextField("Платные услуги", blank=True)
    for_children = models.TextField("Для детей", blank=True)
    type_hotel = models.TextField("Типы номеров", blank=True)
    beach = models.TextField("Пляж", blank=True)
    concept_food = models.TextField("Концепция питания", blank=True)

    def __str__(self):
        return self.title
        return self.city
        return self.country
        return self.vilet
        return self.date_night

        return self.program_tura
        return self.persons
        return self.tour_room
        return self.type_otdyh

    class Meta:
      verbose_name = "Тур"
      verbose_name_plural = "Туры"

class ImagePosts(models.Model):
    imageposts = models.ForeignKey(posts,blank=True,null=True,default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/img',null=True, blank=True)

    class Meta:
      verbose_name = "Картинки к записи"
      verbose_name_plural = "Картинки к записи"
