from django.contrib import admin
from .models import ItineraryOld



@admin.register(ItineraryOld)
class ItineraryOldAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'package','get_days', 'active')
    search_fields = ('subtitle', 'package__title', )
    def get_days(self, obj):
        return obj.package.days

    get_days.short_description = '# Days of Package'
    class Meta:
        model = ItineraryOld
