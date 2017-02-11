from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .models import Competition, Match, Team, Player, TeamPlayerRelationship


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


class MatchDetailView(generic.DetailView):
    model = Match


class MatchesByCompetitionListView(LoginRequiredMixin, generic.ListView): # just trying out loginrequired. not necessary
    model = Match
    paginate_by = 15
    template_name = 'soccer/matches_by_competition.html'

    def get_queryset(self):
        return Match.objects.filter(competition_id=self.request.resolver_match.kwargs['comp_id'])

    def get_context_data(self, **kwargs):
        context = super(MatchesByCompetitionListView, self).get_context_data(**kwargs)
        context['comp_name'] = Competition.objects.get(pk=self.request.resolver_match.kwargs['comp_id']).__str__()
        return context


class TeamListView(generic.ListView):
    model = Team
    paginate_by = 15


class TeamDetailView(generic.DetailView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        qs = TeamPlayerRelationship.objects.filter(team=context['object'], current=True)
        players = Player.objects.filter(id__in=qs.values_list('player_id'))
        context['players'] = players
        return context


class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 15


class PlayerDetailView(generic.DetailView):
    model = Player
