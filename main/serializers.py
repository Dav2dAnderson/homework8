from rest_framework import serializers

from .models import SportType, Team, Player, Game


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

