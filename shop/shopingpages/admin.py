from django import forms
from django.contrib import admin
from .models import Goods

class GoodsAdminForm(admin.ModelAdmin):
    list_display = ("name", "price", "color", "description", "image")
    list_display_links = ("name",)
admin.site.register(Goods, GoodsAdminForm)