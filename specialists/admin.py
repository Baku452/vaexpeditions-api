from django.contrib import admin
from .models import Specialist, ContactUs, Newsletter, ContactUsB2C

# Register your models here.


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "country",
        "destination_interest",
        "message",
        "typeClient",
        "company",
        "is_newsletter",
    )
    pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "package_type",
    )
    pass


@admin.register(ContactUsB2C)
class ContactUsB2CAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created")
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "country",
        "state",
        "phone",
        "city",
        "message",
        "typeClient",
        "company",
        "is_newsletter",
    )
    pass
