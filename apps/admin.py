from django.contrib import admin

from apps.models import ClothingPreference


# Register your models here.

@admin.register(ClothingPreference)
class ClothingPreferenceModelAdmin(admin.ModelAdmin):
    pass
