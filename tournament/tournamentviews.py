# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from serializers import SurfaceTypeSerializer,TournamentSerializer,TournamentPlayingCategorySerializer,TournamentTypeSerializer
from models import SurfaceType,Tournament,TournamentPlayingCategory,TournamentType
# Create your views here.

class SurfaceTypeView(viewsets.ModelViewSet):
    queryset = SurfaceType.objects.all()
    serializer_class = SurfaceTypeSerializer

class TournamentView(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class TournamentPlayingCategoryView(viewsets.ModelViewSet):
    queryset = TournamentPlayingCategory.objects.all()
    serializer_class = TournamentPlayingCategorySerializer

class TournamentTypeView(viewsets.ModelViewSet):
    queryset = TournamentType.objects.all()
    serializer_class = TournamentTypeSerializer