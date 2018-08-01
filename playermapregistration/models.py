# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from player.models import Player
# Create your models here.
from tournament.models import Tournament


class PlayerMapsTournament(models.Model):
    tr_ref = models.ForeignKey(Tournament, default="")
    class Meta:
        db_table ='PlayerTournament'