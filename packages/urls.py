from django.urls import path
from . import views

urlpatterns = [
    path("", views.PackageSearchApi.as_view(), name="packages-search"),
    path("destination/<str:slug>/",views.PackageDestinationListApi.as_view(),name="packages-list-slug",),
    path("<str:slug>", views.PackageRetrieveApi.as_view(), name="packages-retrieve"),
    path("home/", views.PackageHomeListApi.as_view(), name="packages-search"),
    path("featured/<str:slug>",views.PackageFeaturedDestinationListApi.as_view(),name="packages-featured-destination",),
    path("destination/<str:slug_destination>/city/<str:slug>",views.PackageCitiesListApi.as_view(),name="packages-Cities",),
    path("titles/", views.PackageTitleApi.as_view(), name="packages-titles"),
    path("list/", views.PackageListApi.as_view(), name="packages-list"),
    path("optional/",views.PackageOptionalSearchApi.as_view(),name="packages-optional",),
    path("off-the-beaten/<str:slug>",views.PackageDestinationListApi.as_view(),name="packages-optional",),
    path("top/<int:id>",views.PackagesTop.as_view(),name="packages-top",),
    
    #Packages Types
    path("types/", views.PackageTypeListApi.as_view(), name="packages-type-list"),
    path("types/<str:slug>",views.PackageTypeRetrieve.as_view(),name="packages-type-retrieve"),
    path("types/home/", views.PackageTypeHomeApi.as_view(), name="packages-type-home"),
    path("types/nav/", views.PackageTypeNavApi.as_view(), name="packages-type-list"),

    #Interest
    path("interests/", views.InterestListApi.as_view(), name="interest-list"),

    #Cities inside Destinations
    path("<str:slug_destination>/city/<str:slug>",views.PackageCitiesListApi.as_view(),name="packages-Cities",),
]