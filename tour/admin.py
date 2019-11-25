from django.contrib import admin
from .models import *

class ImagesInline (admin.TabularInline):
    model = TourImage
    readonly_fields = ('image_tag', )
    exclude = ('image_small',)
    extra = 0

class TourAdmin(admin.ModelAdmin):

    exclude = ['nameSlug', 'nameLower', 'created_at']
    inlines = [ImagesInline]
    class Meta:
        model = Tour


admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Resort)
admin.site.register(TourOption)
admin.site.register(TourFood)
admin.site.register(Hotel)
admin.site.register(Tour,TourAdmin)
admin.site.register(TourImage)







