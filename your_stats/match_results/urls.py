from django.urls import path
from . import views

app_name = 'match_results'
urlpatterns = [
    path('', views.index, name='index'),
    path('matches/', views.matches , name='matches'),
    path('matches/<int:match_id>/', views.match, name='match'),
    path('players/', views.players , name='players'),
    path('players/<int:player_id>/', views.player, name='player'),
    path('teams/', views.teams, name='teams'),
    path('teams/<int:team_id>/', views.team, name='team'),

]