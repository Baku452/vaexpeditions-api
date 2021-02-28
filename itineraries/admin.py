from django.contrib import admin
from .models import Itinerary, ItineraryImage, ItineraryItems


class ItineraryImageAdmin(admin.StackedInline):
    model = ItineraryImage
    extra = 0


class ItineraryItemsAdmin(admin.StackedInline):
    model = ItineraryItems
    extra = 0


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'package','get_days', 'active')
    search_fields = ('subtitle', 'package__title', )
    inlines = [ItineraryImageAdmin, ItineraryItemsAdmin]
    def get_days(self, obj):
        return obj.package.days

    get_days.short_description = '# Days of Package'
    class Meta:
        model = Itinerary


@admin.register(ItineraryImage)
class ItineraryImageAdmin(admin.ModelAdmin):
    search_fields = ('itinerary__subtitle', 'itinerary__package__title',)
    list_display = ('package', 'itinerary', 'alt')

    def package(self, obj):
        return obj.itinerary.package

    pass

