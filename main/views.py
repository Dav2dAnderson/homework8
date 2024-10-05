from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import SportTypeSerializer, TeamSerializer, PlayerSerializer, GameSerializer
# Create your views here.


class SportTypeViewSet(ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer

    permission_classes = [IsAuthenticated]


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    permission_classes = [IsAuthenticated]


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer











