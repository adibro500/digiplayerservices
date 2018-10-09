# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Country,Address,Player,PlayerRegistration
from .serializers import CountrySerializer, PlayerSerializer, PlayerRegistrationSerializer, AddressSerializer
# Create your views here.

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PlayerView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerRegistrationView(viewsets.ModelViewSet):
    queryset = PlayerRegistration.objects.all()
    serializer_class = PlayerRegistrationSerializer