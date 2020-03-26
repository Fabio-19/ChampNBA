from .models import *
from django.shortcuts import render
from django import views


class TeamListView(views.generic.ListView):
    model = Team


class PlayerListView(views.generic.ListView):
    model = Player


def player_import_view(*args, **kwargs):
    import_players()

# Create your views here.
