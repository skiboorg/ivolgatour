from django.contrib import admin
from .models import *
from comment.models import Comment


class GlobalRegionAdmin(admin.ModelAdmin):
    exclude = ['nameSlug', 'nameLower']

    class Meta:
        model = GlobalRegion


class TourVariantAdmin(admin.ModelAdmin):
    exclude = ['nameSlug', 'nameLower']

    class Meta:
        model = TourVariant


class CountryAdmin(admin.ModelAdmin):
    exclude = ['nameSlug', 'nameLower']

    class Meta:
        model = Country


class TownAdmin(admin.ModelAdmin):
    exclude = ['nameSlug', 'nameLower']

    class Meta:
        model = Town


class ResortAdmin(admin.ModelAdmin):
    exclude = ['nameSlug', 'nameLower']

    class Meta:
        model = Resort


class TourOptionAdmin(admin.ModelAdmin):
    exclude = ['nameSlug', 'nameLower']

    class Meta:
        model = TourOption


class TourFoodAdmin(admin.ModelAdmin):
    exclude = ['nameSlug', 'nameLower']

    class Meta:
        model = TourFood


class HotelAdmin(admin.ModelAdmin):
    exclude = ['nameSlug', 'nameLower']

    class Meta:
        model = Hotel


class ImagesInline (admin.TabularInline):
    model = TourImage
    readonly_fields = ('image_tag', )
    exclude = ('image_small',)
    extra = 0


class CommentsInline (admin.TabularInline):
    model = Comment
    extra = 0


class TourAdmin(admin.ModelAdmin):

    exclude = ['nameSlug', 'nameLower', 'created_at']
    inlines = [ImagesInline, CommentsInline]


    class Meta:
        model = Tour


admin.site.register(GlobalRegion, GlobalRegionAdmin)
admin.site.register(TourVariant, TourVariantAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(Resort, ResortAdmin)
admin.site.register(TourOption, TourOptionAdmin)
admin.site.register(TourFood, TourFoodAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(TourImage)







