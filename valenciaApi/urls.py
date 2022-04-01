"""valenciaApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

from blog.views import (
    BlogTypeListApi,
    BlogRetrieveApi,
    BlogSearchApi,
    BlogListApi,
    BlogPopular,
    BloggerListApi,
    BloggerRetrieveApi,

)

from packages.views import (
    NotificationListApi,
    NotificationRetrieveApi,
)

from itineraries.views import ItineraryRetrieveApi

from specialists.views import ContactCreateApi, NewsletterCreateApi, ContactB2CCreateApi

from tailors.views import (
    TailorListApi,
)
from ourPurpose.views import (
    OurPurposeListApi,
)

from history.views import (
    HistoryApi,
)
from ourteam.views import CollaboratorsListApi, CollaboratorRetrieveApi

from popUp.views import PopUpListApi

from pages.views import PageApi, PageListApi

schema_view = get_schema_view(
    openapi.Info(
        title="Valencia Travel API",
        default_version="v1",
        description="Api valencia travel",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

admin.site.site_header = "Va Expeditions"
admin.site.site_title = "Va Expeditions"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    url(r"^chaining/", include("smart_selects.urls")),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
  
    #Destinations
    path('destinations/', include('destinations.urls')),   

    #Packages
    path('packages/', include('packages.urls')),

    path("notification/", NotificationListApi.as_view(), name="notification-list"),
    path(
        "notification/<str:slug>",
        NotificationRetrieveApi.as_view(),
        name="notification-retrieve",
    ),
    
    path("contact_us/", ContactCreateApi.as_view(), name="contact_us-create"),
    path("newsletter/", NewsletterCreateApi.as_view(), name="newsletter-create"),
   
    path(
        "itineraries/<int:pk>",
        ItineraryRetrieveApi.as_view(),
        name="itineraries-retrieve",
    ),
    path("tailors/list/", TailorListApi.as_view(), name="tailors-retrieve"),
    path("ourpurpose/list/", OurPurposeListApi.as_view(), name="ourpurpose-retrieve"),
    path("history/", HistoryApi.as_view(), name="history-retrieve"),
    path("popup/", PopUpListApi.as_view(), name="popup-retrieve"),
    path("blog/<str:slug>", BlogRetrieveApi.as_view(), name="blog-retrieve"),
    path("blogtypes/", BlogTypeListApi.as_view(), name="blog-types"),
    path("blog/", BlogSearchApi.as_view(), name="blog-search"),
    path("blog/popular/", BlogPopular.as_view(), name="blog-popular"),
    path("blog/list/", BlogListApi.as_view(), name="blog-list"),
    path("blogger/list/", BloggerListApi.as_view(), name="blogger-list"),
    path("blogger/<int:user>", BloggerRetrieveApi.as_view(), name="blog-list"),
    path("collaborators/", CollaboratorsListApi.as_view(), name="collaborators-list"),
    path(
        "collaborators/<str:slug>",
        CollaboratorRetrieveApi.as_view(),
        name="collaborators-retrievet",
    ),
    path("pages/list/", PageListApi.as_view(), name="page-SLUG"),
    path("pages/<str:slug>", PageApi.as_view(), name="page-list"),
    path("contact_b2c/", ContactB2CCreateApi.as_view(), name="contact_b2c-create"),
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
