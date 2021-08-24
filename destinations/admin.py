from django.contrib import admin
from .models import Banner, Country, Destination, Reason, WeatherItems, FaqDest
from adminsortable2.admin import SortableAdminMixin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class WeatherItemsAdmin(NestedStackedInline):
    model = WeatherItems
    extra = 0

class FAQsItemsAdmin(NestedStackedInline):
    model = FaqDest
    extra = 0


@admin.register(Banner)
class BannerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ('name',)
    pass


@admin.register(Country)
class CountryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ('name',)
    pass


@admin.register(Destination)
class DestinationAdmin(SortableAdminMixin, NestedModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'country', 'active')
    search_fields = ('title', 'sub_title', 'country__name')
    inlines = [
        WeatherItemsAdmin,
        FAQsItemsAdmin
    ]
    save_as = True

    class Meta:
        model = Destination


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title',)
    pass

