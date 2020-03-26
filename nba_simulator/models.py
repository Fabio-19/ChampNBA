from datetime import date

from django.db import models
from django import conf

class Player(models.Model):
    PLAYER_POSITION = (
        ('PG', 'Point Guard'),
        ('SG', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center')
    )

    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    photo = models.FileField(blank=True, upload_to='nba_simulator/static/nba_simulator/images/photos/')
    date_of_birth = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    team = models.ForeignKey("Team", on_delete=models.CASCADE, blank=True, null=True)
    position = models.CharField(max_length=2, choices=PLAYER_POSITION, null=True)
    scoring = models.IntegerField(null=True)
    ataque = models.IntegerField(null=True)
    defesa = models.IntegerField(null=True)
    passe = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    three_pts = models.IntegerField(null=True)
    drible = models.IntegerField(null=True)
    bloco = models.IntegerField(null=True)
    steal = models.IntegerField(null=True)
    forca = models.IntegerField(null=True)
    ressaltos = models.IntegerField(null=True)
    cultura_tatica = models.IntegerField(null=True)
    potencial = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    CONFERENCE = (
        ('EC', 'Eastern Conference'),
        ('WC', 'Western Conference'),
    )

    DIVISION = (
        ('NWD', 'Northwest Division'),
        ('PAD', 'Pacific Division'),
        ('SWD', 'Southwest Division'),
        ('ATD', 'Atlantic Division'),
        ('SED', 'Southeast Division'),
        ('CED', 'Central Division')
    )

    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    logo = models.CharField(default="", max_length=8)
    general_manager = models.CharField(max_length=50)
    general_manager_nick = models.CharField(max_length=50)
    conference = models.CharField(max_length=2, choices=CONFERENCE)
    division = models.CharField(max_length=3, choices=DIVISION)
    draft_pick_season10_1stround = models.CharField(max_length=20, blank=True)
    draft_pick_season10_2ndround = models.CharField(max_length=20, blank=True)
    draft_pick_season11_1stround = models.CharField(max_length=20, blank=True)
    draft_pick_season11_2ndround = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Matchup(models.Model):
    game_date = models.IntegerField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team")
    home_team_score = models.IntegerField(null=True, blank=True)
    away_team_score = models.IntegerField(null=True, blank=True)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team")
    player_of_the_game = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)


class Contract(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    season = models.PositiveIntegerField(default=conf.settings.CHAMP_SEASON)
    value = models.PositiveIntegerField()
    is_option = models.BooleanField(default=False)


def import_players():
    # abrir ficheiro
    import json
    with open("nba_simulator\players.json") as f:
        objs = json.load(f)
        for player_dict in objs["league"]["standard"]:
            print(player_dict)
            name = player_dict["firstName"] + " " + player_dict["lastName"]
            short_name = player_dict["firstName"][0] + ". " + player_dict["lastName"]
            date_of_birth_str = player_dict["dateOfBirthUTC"]
            if date_of_birth_str == "":
                continue
            date_of_birth = date(
                year=int(date_of_birth_str[0:4]),
                month=int(date_of_birth_str[5:7]),
                day=int(date_of_birth_str[8:])
            )
            defaults = {
                "short_name": short_name,
                "date_of_birth": date_of_birth,
                "height": float(player_dict["heightMeters"]),
                "weight": float(player_dict["weightKilograms"]),
            }
            player_obj = Player.objects.update_or_create(name=name, defaults=defaults)

    # iterar objectos
    # preparar e criar Players