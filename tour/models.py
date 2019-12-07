from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from pytils.translit import slugify
from random import choices
import string


class Tag(models.Model):
    name = models.CharField('Тег', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = Tag.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class TourVariant(models.Model):
    name = models.CharField('Вид тура', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)
    imageHeader = models.ImageField('Картинка для шапки', upload_to='country_img/', blank=False, null=True)
    pageH1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    pageTitle = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    pageDescription = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    pageKeywords = models.TextField('Keywords SEO', blank=True, null=True)
    pageSeoText = RichTextUploadingField('Полное описание вида тура', blank=True, null=True)


    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = TourVariant.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(TourVariant, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Вид тура"
        verbose_name_plural = "Виды туров"


class GlobalRegion(models.Model):
    name = models.CharField('Глобальный регион (например, Америка, Азия)', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = GlobalRegion.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(GlobalRegion, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Глобальный регион "
        verbose_name_plural = "Глобальные регионы "


class Country(models.Model):
    globalRegion = models.ForeignKey(GlobalRegion, blank=False, null=True, on_delete=models.CASCADE,
                                     verbose_name='Глобальный регион', related_name='global_region')
    image = models.ImageField('Картинка превью', upload_to='country_img/', blank=False)
    imageHeader = models.ImageField('Картинка для шапки', upload_to='country_img/', blank=False, null=True)
    name = models.CharField('Страна', max_length=100, blank=False, null=True)
    isPopular = models.BooleanField('Показывать в популярных направлениях ?', default=False)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)
    shortDescription = models.CharField('Короткое описание (80 символов)', max_length=80, blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = Country.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Town(models.Model):
    name = models.CharField('Город', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = Town.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(Town, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Resort(models.Model):
    name = models.CharField('Курорт', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = Resort.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(Resort, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Курорт"
        verbose_name_plural = "Курорты"


class TourOption(models.Model):
    name = models.CharField('Опция', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = TourOption.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(TourOption, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Опция"
        verbose_name_plural = "Опции"


class TourFood(models.Model):
    name = models.CharField('Питание', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = TourFood.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(TourFood, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Вариант питания"
        verbose_name_plural = "Варианты питания"


class Hotel(models.Model):
    name = models.CharField('Отель', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=255, blank=True, null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True)
    category = models.IntegerField('Категория (1-5), если указано 0, то категория не отображается', default=0)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = Hotel.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(Hotel, self).save(*args, **kwargs)

    def __str__(self):
        return '{} '.format(self.name)

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


class Tour(models.Model):
    name = models.CharField('Название тура', max_length=100, blank=False, null=True)
    nameLower = models.CharField(max_length=100, blank=False, null=True, db_index=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True, db_index=True)

    short_description = models.TextField('Краткое описание для главной', blank=False)
    description = RichTextUploadingField('Полное описание тура', blank=False, null=True)
    date = models.DateTimeField('Дата', blank=True, null=True)

    variant = models.ManyToManyField(TourVariant, verbose_name='Вид тура')
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Тег')
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Страна')
    hotel = models.ForeignKey(Hotel, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Отель')
    flyFrom = models.ForeignKey(Town, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Вылет из',
                                related_name='flyfrom')
    flyTo = models.ForeignKey(Town, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Прилет в',
                              related_name='flyto')
    food = models.ForeignKey(TourFood, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Питание')
    includedOptions = models.ManyToManyField(TourOption, verbose_name='Входит в стоимость',
                                             related_name='includedOptions')
    excludedOptions = models.ManyToManyField(TourOption, verbose_name='Не входит в стоимость',
                                             related_name='excludedOptions')

    personCount = models.IntegerField('Кол-во человек', default=0)
    previewImage = models.ImageField('Изображение превью (270 x 220)', upload_to='tour_img/', blank=False)
    headerImage = models.ImageField('Изображение шапки страницы полного описания тура (1920x210)', upload_to='tour_img/', blank=False)

    pageH1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    pageTitle = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    pageDescription = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    pageKeywords = models.TextField('Keywords SEO', blank=True, null=True)

    priceDollar = models.IntegerField('Стоимость в долларах', default=0)
    discountPriceDollar = models.IntegerField('Стоимость со скидкой в долларах', default=0)
    priceEuro = models.IntegerField('Стоимость в евро', default=0)
    discountPriceEuro = models.IntegerField('Стоимость со скидкой в евро', default=0)
    priceRub = models.IntegerField('Стоимость в рублях', default=0)
    discountPriceRub = models.IntegerField('Стоимость со скидкой в рублях', default=0)

    length = models.IntegerField('Продолжительность тура', default=0)
    isSpecial = models.BooleanField('Показывать в специальных турах на главной ?', default=False)
    isPopular = models.BooleanField('Показывать в популярных турах на главной?', default=False)
    badge = models.CharField('Бейдж тура (выводится на карточке специального или популярного тура)', max_length=10, blank=True, null=True)
    isActive = models.BooleanField('Отображать в списке туров?', default=True)
    views = models.IntegerField('Просмотров', default=0)
    rating = models.IntegerField('Рейтинг тура (в звездочках) от 1 до 5, если 0 - не отображается', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = Tour.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        self.nameLower = self.name.lower()
        super(Tour, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/tour/{self.nameSlug}/'

    def __str__(self):
        return 'Тур : {} '.format(self.name)

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, blank=False, null=True, on_delete=models.CASCADE, verbose_name='Изображение для')
    image = models.ImageField('Изображение', upload_to='tour_img', blank=False)

    def __str__(self):
        return 'Изображение для тура : {} '.format(self.tour.name)

    class Meta:
        verbose_name = "Изображение для тура"
        verbose_name_plural = "Изображения для туров"

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.image:
            return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Картинка'