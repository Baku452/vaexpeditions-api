from django.contrib import admin
from .models import Tailor

# Register your models here.
@admin.register(Tailor)
class TailorAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title',)


