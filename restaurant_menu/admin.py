from django.contrib import admin
from .models import Item


class MenuAdmin(admin.ModelAdmin):
    list_display = ("meal", "meal_type", "status")
    list_filter = ("status", "meal_type")
    search_fields = ("meal", )


admin.site.register(Item, MenuAdmin)

