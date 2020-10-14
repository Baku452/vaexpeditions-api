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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from destinations.views import (
    DestinationListApi,
    BannerListApi
)

from packages.views import (
    PackageTypeListApi,
    PackageSearchApi,
    PackageRetrieveApi,
    PackageTypeDetailApi,
    PackageHomeListApi,
    PackageListApi,
    ExperienceListApi
)

from itineraries.views import (
    ItineraryRetrieveApi
)

from specialists.views import (
    ContactCreateApi,
    NewsletterCreateApi
)

schema_view = get_schema_view(
   openapi.Info(
      title="Valencia Travel API",
      default_version='v1',
      description="Api valencia travel",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

admin.site.site_header = 'Valencia Travel'
admin.site.site_title = 'Valencia Travel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('destinations/', DestinationListApi.as_view(), name='destination-list'),
    path('banners/', BannerListApi.as_view(), name='banners-list'),

    path('packagestype/', PackageTypeListApi.as_view(), name='packages-type-list'),
    path('packagestype/<int:pk>', PackageTypeDetailApi.as_view(), name='packages-type-list'),

    path('contact_us/', ContactCreateApi.as_view(), name='contact_us-create'),
    path('newsletter/', NewsletterCreateApi.as_view(), name='newsletter-create'),

    path('packages/home/', PackageHomeListApi.as_view(), name='packages-search'),
    path('packages/', PackageSearchApi.as_view(), name='packages-search'),
    path('packages/list/', PackageListApi.as_view(), name='packages-list'),

    path('experiences/list/', ExperienceListApi.as_view(), name='experiences-list'),

    path('package/<str:slug>', PackageRetrieveApi.as_view(), name='packages-retrieve'),
    path('itineraries/<int:pk>', ItineraryRetrieveApi.as_view(), name='itineraries-retrieve'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)