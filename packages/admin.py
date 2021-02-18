from django.contrib import admin
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
from .models import Package, PackageImage, PackageType, Month, Experience, Interest, Notification
from itineraries.models import (
    Itinerary,
    Faq,
    OptionalRenting,
    DatesAndPrices,
)
from old_itinerario.models import (
    ItineraryOld
)
from adminsortable2.admin import SortableAdminMixin


class DatesAndPricesAdmin(admin.StackedInline):
    model = DatesAndPrices
    extra = 0


class OptionalRentingAdmin(admin.StackedInline):
    model = OptionalRenting
    extra = 0


class FaqAdmin(admin.StackedInline):
    model = Faq
    extra = 0


class ItineraryAdmin(admin.StackedInline):
    model = Itinerary
    extra = 0

class ItineraryOldAdmin(admin.StackedInline):
    model = ItineraryOld
    extra = 0

class PackageImageAdmin(admin.TabularInline):
    model = PackageImage
    extra = 0
    fields = ['image', 'alt', 'image_tag']
    readonly_fields = ['image_tag']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'days','destination', 'published', 'optional')
    search_fields = ('title', 'destination__title', 'optional')
    inlines = [
        PackageImageAdmin,
        ItineraryAdmin,
        ItineraryOldAdmin,
        FaqAdmin,
        OptionalRentingAdmin,
        DatesAndPricesAdmin
    ]

    class Meta:
        model = Package


@admin.register(PackageType)
class PackageTypeAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Interest)
class InterestAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass




# Register your models here.
# admin.site.register(Package)