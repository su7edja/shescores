from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .models import Competition, Match, Team, Player


def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    #  http://stackoverflow.com/questions/1317714/how-can-i-filter-a-date-of-a-datetimefield-in-django
    today = datetime.today()
    context = {
        'todays_matches': Match.objects.filter(kickoff__startswith=today),
        'upcoming_matches': Match.objects.filter(kickoff__gte=today)[:5],
        'num_competitions': Competition.objects.count(),
        'num_matches': Match.objects.count(),
        'num_teams': Team.objects.count(),
        'num_players': Player.objects.count(),
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


class CompetitionListView(generic.ListView):
    model = Competition


class MatchListView(generic.ListView):
    model = Match
    paginate_by = 15


class MatchDetailView(generic.ListView):
    model = Match


class MatchesByCompetitionListView(LoginRequiredMixin, generic.ListView): # just trying out loginrequired. not necessary
    model = Match
    paginate_by = 15
    template_name = 'soccer/matches_by_competition.html'

    def get_queryset(self):
        return Match.objects.filter(competition_id=self.request.resolver_match.kwargs['comp_id'])
