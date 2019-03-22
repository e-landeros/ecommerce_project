from django.contrib import admin
from django.utils.html import format_html

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title',)
    list_display_links = ('id', 'title',)

    # def image_tag(self, obj):
    #     return format_html('<img src="{}" />'.format(obj.image.url))

    # image_tag.short_description = 'Image'


admin.site.register(Product, ProductAdmin)