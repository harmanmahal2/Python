from django.forms import ModelForm
from .models import *

class PlayerForm(ModelForm):

    class Meta:
        model = Player
        fields = '__all__'


class CreateLeagueForm(ModelForm):

    class Meta:
        model = League
        fields = '__all__'


class CreateTeamForm(ModelForm):

    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            "league": "League/Cup"
        }