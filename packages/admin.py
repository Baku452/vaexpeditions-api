from django.contrib import admin
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
from .models import Package, PackageImage, PackageType, Month, Experience, Interest, Notification
from itineraries.models import (
    Itinerary,
    Faq,
    OptionalRenting,
    DatesAndPrices,
    ItineraryImage,
)
from old_itinerario.models import (
    ItineraryOld
)
from adminsortable2.admin import SortableAdminMixin
from modelclone import ClonableModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class DatesAndPricesAdmin(NestedStackedInline):
    model = DatesAndPrices
    extra = 0


class OptionalRentingAdmin(NestedStackedInline):
    model = OptionalRenting
    extra = 0


class FaqAdmin(NestedStackedInline):
    model = Faq
    extra = 0


# class ItineraryAdmin(admin.StackedInline):
#     model = Itinerary
#     extra = 0
class ItineraryImageAdmin(NestedStackedInline):
    model = ItineraryImage
    extra = 0
    fk_name = 'itinerary'
class ItineraryAdmin(NestedStackedInline):
    model = Itinerary
    extra = 0
    fk_name = 'package'
    inlines = [ItineraryImageAdmin]

class ItineraryOldAdmin(NestedStackedInline):
    model = ItineraryOld
    extra = 0

class PackageImageAdmin(NestedStackedInline):
    model = PackageImage
    extra = 0
    fields = ['image', 'alt', 'image_tag']
    readonly_fields = ['image_tag']
    inlines = ""



@admin.register(Package)
class PackageAdmin(ClonableModelAdmin,NestedModelAdmin, admin.ModelAdmin):
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
    save_as = True
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