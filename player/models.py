# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.country_name

    class Meta:
        db_table ='Country'

class Player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not Specified'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N', verbose_name=('Gender'))
    date_of_birth = models.DateTimeField(verbose_name=("Date of Birth"),auto_now=True)
    country =  models.OneToOneField(Country);
    player_ref = models.AutoField(primary_key=True)
    class Meta:
        db_table ='Player'
    def __str__(self):
        return self.first_name + ' ' +self.last_name

class Address(models.Model):
    entity_type = models.CharField(max_length=100)
    company_name =  models.CharField(max_length=100)  
    city =  models.CharField(max_length=50)  
    state =  models.CharField(max_length=50)  
    country = models.OneToOneField(Country); 
    email = models.EmailField(max_length=100)
    address_line =  models.CharField(max_length=250)  
    address_line2=  models.CharField(max_length=250)  
    update_date=  models.DateTimeField(verbose_name=("Update Date"),auto_now=True)
    player_ref = models.ForeignKey(Player, default='');
    address_ref = models.AutoField(primary_key=True)

    class Meta:
        db_table ='Address'






class PlayerRegistration(models.Model):
    player_ref = models.AutoField(primary_key=True)
    player = models.OneToOneField(Player);
    class Meta:
        db_table ='PlayerRegistration'

