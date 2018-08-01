from rest_framework import serializers
from .models import Address, Player, Country, PlayerRegistration

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('url','country_code','country_name')

class AddressSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField()
    class Meta:
        model = Address
        fields = ('url','player_ref','entity_type','company_name','city','state','country','email','address_line','address_line2')
        # extra_kwargs = {'country': 'view_name': 'countries:country'}

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('url','player_ref','first_name','last_name','gender','date_of_birth','country')
    
class PlayerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRegistration
        fields = ('url','player')
    