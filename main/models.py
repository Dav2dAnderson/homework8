from django.db import models

# Create your models here.


class SportType(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
    

class Team(models.Model):
    title = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    created_year = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.title
    

class Player(models.Model):
    fullname = models.CharField(max_length=250)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.fullname


class Game(models.Model):
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)
    first_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="first_team_games")
    second_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="second_team_games")
    date = models.DateTimeField()
    location = models.CharField(max_length=250)
    score_first_team = models.PositiveIntegerField(default=0)
    score_second_team = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.sport_type.title



