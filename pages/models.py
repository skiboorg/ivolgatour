from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from tour.models import Tour

class Banner(models.Model):
    order = models.IntegerField('Номер по порядку', default=1)
    bannerOffer = models.CharField('Категория баннера (20символов)', max_length=20, blank=True)
    bigTextColored = models.CharField('Заголовок на баннере выделенный цветом (10символов)', max_length=10, blank=True, null=True)
    bigText = models.CharField('Заголовок на баннере (30 символов)', max_length=30, blank=False, null=True)
    smallText = models.CharField('Описание на баннере (160 символов)', max_length=160, blank=True, null=True)
    image = models.ImageField('Картинка для баннера (1920 x (700-900))', upload_to='banners/', blank=False)
    buttonText = models.CharField('Надпись на кнопке', max_length=10, blank=True)
    buttonUrl = models.CharField('Произвольная сылка с кнопки', max_length=100, blank=True)
    tourUrl = models.ForeignKey(Tour, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Кнопка ссылается на тур')
    isActive = models.BooleanField('Отображать баннер?', default=True)

    def __str__(self):
        return f'Баннер № П/П {self.order}'

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"



class SeoTag(models.Model):
    indexTitle = models.CharField('Тег Title для главной', max_length=255, blank=True, null=True)
    indexDescription = models.CharField('Тег Description для главной', max_length=255, blank=True, null=True)
    indexKeywords = models.TextField('Тег Keywords для главной',  blank=True, null=True)
    servicesTitle = models.CharField('Тег Title для страницы со всеми услугами', max_length=255, blank=True, null=True)
    servicesDescription = models.CharField('Тег Description для страницы со всеми услугам', max_length=255, blank=True, null=True)
    servicesKeywords = models.TextField('Тег Keywords для страницы со всеми услугам', blank=True, null=True)
    postsTitle = models.CharField('Тег Title для страницы со всеми статьями', max_length=255, blank=True, null=True)
    postsDescription = models.CharField('Тег Description для страницы со всеми статьями', max_length=255, blank=True,
                                           null=True)
    postsKeywords = models.TextField('Тег Keywords для страницы со всеми статьями', blank=True, null=True)
    contactTitle = models.CharField('Тег Title для страницы контакты', max_length=255, blank=True, null=True)
    contactDescription = models.CharField('Тег Description для страницы контакты', max_length=255, blank=True,
                                        null=True)
    contactKeywords = models.TextField('Тег Keywords для страницы контакты', blank=True, null=True)

    indexSeoText = RichTextUploadingField('СЕО тектс для главной', blank=True, null=True)


    def __str__(self):
        return 'Теги и тексты для статических страниц'

    class Meta:
        verbose_name = "Теги и тексты для статических страниц"
        verbose_name_plural = "Теги и тексты для статических страниц"