from django.contrib import admin

from quotefetch.models import Quote


# Register your models here.

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author', 'user', 'created_at', 'updated_at']
    # search_fields = ['quote', 'author']
    # list_filter = ['user', '