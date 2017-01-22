from django.shortcuts import render

from .models import Competition, Match, Team, Player


def index(request):
    context = {
        'num_competitions': Competition.objects.count(),
        'num_matches': Match.objects.count(),
        'num_teams': Team.objects.count(),
        'num_players': Player.objects.count(),
    }
    return render(request, 'index.html', context=context)
