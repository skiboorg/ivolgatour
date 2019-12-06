from django.contrib import admin
from .models import *

class BannerAdmin(admin.ModelAdmin):
    exclude = ['smallOfferReplaced']

    class Meta:
        model = Banner

admin.site.register(Banner, BannerAdmin)
admin.site.register(SeoTag)