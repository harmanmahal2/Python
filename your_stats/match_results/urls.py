from django.urls import path
from . import views

app_name = 'match_results'
urlpatterns = [
    path('', views.index, name='index'),
    path('matches/', views.matches , name='matches'),
    path('search_matches/', views.search_matches, name='search_matches'),
    path('matches/<int:match_id>/', views.match, name='match'),
    path('leagues/', views.leagues , name='leagues'),
    path('league/<int:league_id>/', views.league , name='league'),
    path('players/', views.players, name='players'),
    path('search_players/', views.search_players, name='search_players'),
    path('players/<int:player_id>/', views.player, name='player'),
    path('teams/', views.teams, name='teams'),
    path('search_teams/', views.search_teams, name='search_teams'),
    path('teams/<int:team_id>/', views.team, name='team'),

]