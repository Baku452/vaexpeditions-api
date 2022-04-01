from django.urls import path
from . import views

urlpatterns = [
    
    #Destinations
    path("", views.DestinationListApi.as_view(), name="destination-list"),
    path("home/",views.DestinationTitleBannerApi.as_view(),name="destination-list",),
    path("everyone/",views.EveryoneDestinationApi.as_view(),name="destination-everyone",),
    path("<str:slug>",views.DestinationRetrieveApi.as_view(),name="destination-retrieve",),
    #Banners
    path("banners/", views.BannerListApi.as_view(), name="banners-list"),
    #Continent
    path("continents/home/", views.ContinentHomeApi.as_view(), name="countries-list"),
    path("continents/<str:slug>", views.ContinentRetrieveApi.as_view(), name="countries-retrieve"),
    path("continents/", views.ContinentListApi.as_view(), name="countries-list"),
    #Cities
    path("cities/", views.CitiesApi.as_view(), name="cities-all"),
    path("city/<str:slug_destination>/<str:slug>",views.CityRetrieveApi.as_view(),name="city-retrieve",),
]