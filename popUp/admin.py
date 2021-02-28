from django.contrib import admin
from .models import PopUp

@admin.register(PopUp)
class PopUpAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title',)

# Register your models here.
