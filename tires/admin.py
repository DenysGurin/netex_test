from django.contrib import admin

from .models import Tire


class TireAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Tire._meta.fields]
    fields = [field.name for field in Tire._meta.fields if field.name not in ["id"]]

admin.site.register(Tire, TireAdmin)
