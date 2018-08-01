# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SurfaceType(models.Model):
    surface_type_ref = models.AutoField(primary_key=True)
    surface_type = models.CharField(max_length=150)
    active = models.BooleanField(default=False)

    class Meta:
        # indexes = [
        #    models.Index(fields=['update_date'], name='udpate_date_idx'),
        # ]
        db_table ='SurfaceType'
    
    def __str__(self):
        return (self.surface_type)

class TournamentType(models.Model):
    tournament_type_ref = models.AutoField(primary_key=True)
    tournament_type = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    class Meta:
        # indexes = [
        #    models.Index(fields=['update_date'], name='udpate_date_idx'),
        # ]
        db_table ='TournamentType'
    
    def __str__(self):
        return (self.tournament_type)

class Tournament(models.Model):
    tournament_ref = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    start_date = models.DateTimeField(auto_now=True)
    end_date =  models.DateTimeField(auto_now=True)
    number_of_rounds = models.IntegerField()
    tournament_type_ref = models.OneToOneField(TournamentType,on_delete=models.CASCADE)
    surface_type_ref = models.OneToOneField(SurfaceType,on_delete=models.CASCADE)

    class Meta:
        # indexes = [
        #    models.Index(fields=['update_date'], name='udpate_date_idx'),
        # ]
        db_table ='Tournament'

    def __str__(self):
        return "%s is at %s" % (self.tournament_name, self.location)

class TournamentPlayingCategory(models.Model):
    tournament_pc_ref = models.AutoField(primary_key=True)
    tournament_ref = models.OneToOneField(Tournament,on_delete=models.CASCADE)
    #It's a foriegn key to Playing Category
    playing_category_ref = models.CharField(max_length=150)

    class Meta:
        # indexes = [
        #    models.Index(fields=['update_date'], name='udpate_date_idx'),
        # ]
        db_table ='TournamentPlayingCategory'
        verbose_name_plural = 'Tournament Playing Category'

