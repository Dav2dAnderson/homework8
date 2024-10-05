from django.contrib import admin

from .models import SportType, Team, Game, Player
# Register your models here.


@admin.register(SportType)
class SportTypeAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'created_year')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('sport_type', 'first_team', 'second_team', 'date', 'location')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'team', 'age')

