from django.contrib import admin
from .models import Events, Gallery
from django.utils.html import format_html

# Register your models here.

admin.site.register(Events)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="70" style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Image'
    list_display = (
        'thumbnail',
        'id',
        'titlle_gallery', 
    )
    list_filter = (
        #'acheteur',
    )