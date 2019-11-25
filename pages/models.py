from django.db import models

class Banner(models.Model):
    order = models.IntegerField('Номер по порядку', default=1)
    bannerOffer = models.CharField('Категория баннера (20символов)', max_length=20, blank=False)
    bigTextColored = models.CharField('Заголовок на баннере выделенный цветом (10символов)', max_length=10, blank=False, null=True)
    bigText = models.CharField('Заголовок на баннере (30 символов)', max_length=30, blank=False, null=True)
    smallText = models.CharField('Описание на баннере (160 символов)', max_length=160, blank=False, null=True)
    image = models.ImageField('Картинка для баннера (1920 x (700-900))', upload_to='banners/', blank=True)
    buttonText = models.CharField('Надпись на кнопке', max_length=10, blank=False)
    buttonUrl = models.CharField('Ссылка с кнопки', max_length=100, blank=False)
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


    def __str__(self):
        return 'Теги для статических страниц'

    class Meta:
        verbose_name = "Теги для статических страниц"
        verbose_name_plural = "Теги для статических страниц"