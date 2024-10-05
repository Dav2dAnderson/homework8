from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import SportTypeViewSet, TeamViewSet, PlayerViewSet, GameViewSet


router = DefaultRouter()

router.register('sport_types', SportTypeViewSet)
router.register('team', TeamViewSet)
router.register('player', PlayerViewSet)
router.register('game', GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]