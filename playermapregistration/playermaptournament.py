# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import PlayerMapsTournament
from .serializers import PlayerMapsTournamentSerializer
# Create your views here.

class PlayersmapsTournaments(viewsets.ModelViewSet):
    queryset = PlayerMapsTournament.objects.all()
    serializer_class = PlayerMapsTournamentSerializer
