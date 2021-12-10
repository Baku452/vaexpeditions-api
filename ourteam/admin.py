from django.contrib import admin
from .models import Collaborator
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
@admin.register(Collaborator)
class CollaboratorAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
