from django.contrib import admin
from .models import Banner, Country, Destination, Reason, WeatherItems, FaqDest, DestinationImage, ContinentImage, WhereToGo, ItemWhere, TravelAdvice
from adminsortable2.admin import SortableAdminMixin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class WeatherItemsAdmin(NestedStackedInline):
    model = WeatherItems
    extra = 0

class FAQsItemsAdmin(NestedStackedInline):
    model = FaqDest
    extra = 0

class DestinationImages(NestedStackedInline):
    model = DestinationImage
    extra = 0

class ContinentImages(NestedStackedInline):
    model = ContinentImage
    extra = 0

class WheretoGo(NestedStackedInline):
    model = WhereToGo
    extra = 0

class ItemWheretoGo(NestedStackedInline):
    model = ItemWhere
    extra = 0

class TravelAdviceNested(NestedStackedInline):
    model = TravelAdvice
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
    inlines = [
        ContinentImages
    ]
    pass


@admin.register(Destination)
class DestinationAdmin(SortableAdminMixin, NestedModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'country', 'active')
    search_fields = ('title', 'sub_title', 'country__name')
    inlines = [
        WeatherItemsAdmin,
        FAQsItemsAdmin,
        DestinationImages,
        WheretoGo,
        TravelAdviceNested
    ]
    save_as = True

    class Meta:
        model = Destination


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title',)
    pass

@admin.register(WhereToGo)
class WhereToGoAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title',)
    inlines = [
        ItemWheretoGo,
    ]
    pass

@admin.register(TravelAdvice)
class TravelAdviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'active','destination')
    search_fields = ('title','destination')
    pass
