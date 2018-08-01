"""digiplayerservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from player import views
from tournament import tournamentviews
from playermapregistration import playermaptournament
router = routers.DefaultRouter()
router.register(r'addresses',views.AddressView)
router.register(r'players',views.PlayerView)
router.register(r'surfaceTypes',tournamentviews.SurfaceTypeView)
router.register(r'tournaments',tournamentviews.TournamentView)
router.register(r'tournamentTypes',tournamentviews.TournamentTypeView)
router.register(r'tournamentPlayingCategories',tournamentviews.TournamentPlayingCategoryView)
router.register(r'player-register',views.PlayerRegistrationView)
router.register(r'countries',views.CountryView)
router.register(r'player-tournaments',playermaptournament.PlayersmapsTournaments)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
