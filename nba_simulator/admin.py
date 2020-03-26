from django.contrib import admin

from .models import Player, Team, Contract, Matchup


class ContractInLine(admin.TabularInline):
    model = Contract
    extra = 3


class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['conference', 'division']
    list_display = ['name', 'general_manager']
    ordering = ['name']


class PlayerAdmin(admin.ModelAdmin):
    inlines = [ContractInLine]
    list_display = ['name', 'position', 'team']
    ordering = ['name']
    list_filter = ['team']
    search_fields = ['name']
    fieldsets = [
        (None, {
            'fields': (('name', 'short_name'), ('photo', 'date_of_birth'), ('height', 'weight'), 'team',
                       'position', 'scoring', 'ataque', 'defesa', 'passe', 'speed', 'three_pts', 'drible',
                       'bloco', 'steal', 'forca', 'ressaltos', 'cultura_tatica', 'potencial'
                       )
        })
    ]


class MatchupAdmin (admin.ModelAdmin):
    list_display = ['game_date', 'home_team', 'away_team', 'home_team_score', 'away_team_score']
    ordering = ['game_date']
    search_fields = ['game_date']


admin.site.register(Team, TeamAdmin)

admin.site.register(Player, PlayerAdmin)

admin.site.register(Matchup, MatchupAdmin)
