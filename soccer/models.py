from datetime import date

from django.db import models

YEAR_CHOICES = [(y, y) for y in range(1800, 2501)]


class League(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    TEAM_TYPES = ((1, 'National'), (2, 'League'))

    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(choices=TEAM_TYPES)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=255)
    stadium = models.CharField(max_length=255, blank=True, null=True)
    league = models.ForeignKey(League, models.SET_NULL, blank=True, null=True)
    year_started = models.IntegerField(choices=YEAR_CHOICES)
    active = models.BooleanField(default=True)
    previous_name = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255)
    owner = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITIONS = (
        ('GK', 'Goalkeeper'),
        ('D', 'Defender'),
        ('LB', 'Left Back'),
        ('CB', 'Center Back'),
        ('RB', 'Right Back'),
        ('M', 'Midfielder'),
        ('LM', 'Left Midfielder'),
        ('CM', 'Center Midfielder'),
        ('RM', 'Right Midfielder'),
        ('F', 'Forward'),
        ('LF', 'Left Forward'),
        ('CF', 'Center Forward'),
        ('RF', 'Right Forward'),
    )

    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField()
    height = models.IntegerField(blank=True, null=True, help_text='height in cm')
    position = models.CharField(max_length=3, choices=POSITIONS)
    number = models.IntegerField(blank=True, null=True, help_text='Number most often worn')
    country = models.CharField(max_length=255)
    country_2 = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    caps = models.IntegerField(default=0)
    twitter_handle = models.CharField(max_length=255, blank=True, null=True)
    instagram_handle = models.CharField(max_length=255, blank=True, null=True)
    college = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    wikipedia = models.URLField(blank=True, null=True)
    fun_facts = models.TextField(blank=True, null=True)

    @property
    def age(self):
        today = date.today()
        # Take away 1 year if birthday hasnt come this year.
        return today.year - self.birthdate.year - \
               ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    def __str__(self):
        return '{name}'.format(name=self.name, age=self.age)


class TeamPlayerRelationship(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    current = models.BooleanField(default=True)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)


class Competition(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(choices=YEAR_CHOICES)
    league = models.ForeignKey(League, models.SET_NULL, blank=True, null=True)
    participants = models.ManyToManyField(Team, related_name="competition_participated")
    champion = models.ForeignKey(Team, models.PROTECT, blank=True, null=True, related_name="competition_won")

    def __str__(self):
        return '{} - {}'.format(self.year, self.name)


class Match(models.Model):
    competition = models.ForeignKey(Competition, models.CASCADE)
    venue = models.CharField(max_length=255)
    kickoff = models.DateTimeField(help_text='UTC Time')
    home_team = models.ForeignKey(Team, models.PROTECT, related_name="home_matches")
    away_team = models.ForeignKey(Team, models.PROTECT, related_name="away_matches")
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)
    home_penalty_score = models.IntegerField(blank=True, null=True)
    away_penalty_score = models.IntegerField(blank=True, null=True)
    winner = models.CharField(max_length=4, choices=(('home', 'home'), ('away', 'away')), blank=True, null=True)

    def __str__(self):
        return '[{}]: {} {} - {} {}'.format(self.competition, self.home_team, self.home_score, self.away_score,
                                            self.away_team)

    class Meta:
        verbose_name_plural = "matches"

class GoalScored(models.Model):
    match = models.ForeignKey(Match, models.CASCADE)
    player = models.ForeignKey(Player, models.PROTECT)
    minutes = models.IntegerField()

    def __str__(self):
        return self.match, self.player, self.minutes

    class Meta:
        verbose_name_plural = "goals scored"


class Statistics(models.Model):
    games_played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()


class TeamAllTimeStatistics(Statistics):
    team = models.ForeignKey(Team, models.PROTECT)
    goals_for = models.IntegerField(help_text='Usually abbreviated as F')
    goals_against = models.IntegerField(help_text='Usually abbreviated as A')
    goal_difference = models.IntegerField(help_text='Usually abbreviated as GD')
    points = models.IntegerField()

    def __str__(self):
        return self.team

    class Meta:
        verbose_name_plural = "team all time statistics"


class TeamCompetitionStatistics(TeamAllTimeStatistics):
    competition = models.ForeignKey(Competition, models.CASCADE)

    def __str__(self):
        return '{team} ({competition})'.format(team=self.team, competition=self.competition)

    class Meta:
        verbose_name_plural = "team competition statistics"


class PlayerCareerStatistics(Statistics):
    player = models.ForeignKey(Player, models.PROTECT)
    minutes_played = models.IntegerField()
    yellow_cards = models.IntegerField(help_text='Usually abbreviated as YC')
    red_cards = models.IntegerField(help_text='Usually abbreviated as RC')


class GoalkeeperCareerStatistics(PlayerCareerStatistics):
    saves = models.IntegerField(help_text='Usually abbreviated as SV')
    goals_allowed = models.IntegerField(help_text='Usually abbreviated as GA')
    shots_on_goal_against = models.IntegerField(help_text='Usually abbreviated as SOG')
    shots_against = models.IntegerField(help_text='Usually abbreviated as S')
    clean_sheets = models.IntegerField(help_text='Usually abbreviated as CS')

    def __str__(self):
        return self.player

    class Meta:
        verbose_name_plural = "goalkeeper career statistics"


class OutfieldPlayerCareerStatistics(PlayerCareerStatistics):
    goals = models.IntegerField()
    assists = models.IntegerField(help_text='Usually abbreviated as A')
    shots_on_goal = models.IntegerField(help_text='Usually abbreviated as SG. Sometimes called shots on target.')
    shots = models.IntegerField(help_text='Usually abbreviated as SH.')

    def __str__(self):
        return self.player

    class Meta:
        verbose_name_plural = "outfield player career statistics"


class GoalkeeperCompetitionStatistics(GoalkeeperCareerStatistics):
    competition = models.ForeignKey(Competition, models.CASCADE)

    def __str__(self):
        return '{player} ({competition})'.format(player=self.player, competition=self.competition)

    class Meta:
        verbose_name_plural = "goalkeeper competition statistics"


class OutfieldPlayerCompetitionStatistics(OutfieldPlayerCareerStatistics):
    competition = models.ForeignKey(Competition, models.CASCADE)

    def __str__(self):
        return '{player} ({competition})'.format(player=self.player, competition=self.competition)

    class Meta:
        verbose_name_plural = "outfield player competition statistics"
