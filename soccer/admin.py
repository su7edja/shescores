from django.contrib import admin

from .models import Competition, Match, GoalScored, League, Team, Player, TeamPlayerRelationship, \
    TeamAllTimeStatistics, TeamCompetitionStatistics, GoalkeeperCareerStatistics, OutfieldPlayerCareerStatistics, \
    GoalkeeperCompetitionStatistics, OutfieldPlayerCompetitionStatistics


@admin.register(TeamPlayerRelationship)
class TeamPlayerRelationshipAdmin(admin.ModelAdmin):
    list_display = ('team', 'player', 'current')
    list_filter = ('team', 'current')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('kickoff', 'competition', 'home_team', 'home_score', 'away_score', 'away_team')
    list_filter = ('competition', 'home_team', 'away_team')

admin.site.register(Competition)
admin.site.register(GoalScored)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(TeamAllTimeStatistics)
admin.site.register(TeamCompetitionStatistics)
admin.site.register(GoalkeeperCareerStatistics)
admin.site.register(OutfieldPlayerCareerStatistics)
admin.site.register(GoalkeeperCompetitionStatistics)
admin.site.register(OutfieldPlayerCompetitionStatistics)
