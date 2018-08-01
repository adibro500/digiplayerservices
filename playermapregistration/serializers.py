from models import PlayerMapsTournament
from rest_framework import viewsets
from rest_framework import serializers

class PlayerMapsTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerMapsTournament
        fields = ('url','tr_ref')
