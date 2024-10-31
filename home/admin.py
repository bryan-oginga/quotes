from django.contrib import admin
from django.utils.html import format_html
from .models import Quotes

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote_text', 'author_name', 'image_preview', 'created_at')
    list_filter = ('author_name', 'created_at')
    search_fields = ('quote_text', 'author_name')

    def image_preview(self, obj):
        return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image_url)
    image_preview.short_description = 'Image Preview'

admin.site.register(Quotes, QuoteAdmin)
