from django.contrib import admin
from .models import Blog, BlogType
from adminsortable2.admin import SortableAdminMixin
from modelclone import ClonableModelAdmin

# Register your models here.


@admin.register(Blog)
class BlogAdmin(ClonableModelAdmin):
    # exclude = ('author',)
    list_display = ("title", "published", "destination", "interest", "blog_type")
    search_fields = ("title", "destination__title")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    # save_as = True
    class Meta:
        model = Blog


@admin.register(BlogType)
class BlogTypeAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
