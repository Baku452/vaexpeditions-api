from django.contrib import admin
from .models import OurPurpose
from adminsortable2.admin import SortableAdminMixin


@admin.register(OurPurpose)
class OurPurposeAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display= ('title', 'active')
    search_fields = ('title',)

# Register your models here.
