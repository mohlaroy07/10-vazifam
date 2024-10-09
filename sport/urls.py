from django.urls import path
from .views import teams_page, players_page

urlpatterns = [
    path("", teams_page, name="team_page"),
    path('players/', players_page, name='players_page')
]
