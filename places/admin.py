from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return format_html(
            '<img src="{url}" width="200" />'.format(
                url=obj.image.url
            )
        )
    fields = ('image', 'preview_image', 'sequence_number')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
