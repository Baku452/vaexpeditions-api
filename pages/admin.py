from django.contrib import admin
from .models import Page
from django.db.models import Value
from django.db.models.functions import Concat

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ("slug", "created", "URL")
    list_display = ("title", "created", "URL")
    model = Page
