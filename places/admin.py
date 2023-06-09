from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from .models import Place, Image


admin.site.register(Image)


class ImagesInline(SortableStackedInline):
    model = Image
    extra = 1
    readonly_fields = ['preview_image']

    def preview_image(self, place_image):
        return format_html(
            '<img src="{url}" height="200" width="auto" />',
            url=place_image.image.url
        )

    fields = ('image', 'preview_image', 'sequence_number')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImagesInline]
