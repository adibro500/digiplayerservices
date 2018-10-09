from .models import SurfaceType, TournamentType, Tournament, TournamentPlayingCategory
from rest_framework import serializers

class SurfaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurfaceType
        fields = ('url','active','surface_type_ref','surface_type','active')

class TournamentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentType
        fields = ('url','tournament_type_ref','tournament_type','active')

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('url','tournament_ref','tournament_name','location','start_date','end_date','number_of_rounds','tournament_type_ref','surface_type_ref') 

class TournamentPlayingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentPlayingCategory
        fields = ('url','tournament_pc_ref','tournament_ref','playing_category_ref') 
