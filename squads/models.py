import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from embed_video.fields import EmbedVideoField

from .utils import natural_time


class Squad(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['pk']

    def stats(self):
        stats = []
        today = datetime.date.today()
        this_week_sunday = today - datetime.timedelta(days=(today.weekday() + 1) % 7)
        this_week_saturday = this_week_sunday + datetime.timedelta(days=6)
        last_week_sunday = this_week_sunday - datetime.timedelta(days=7)
        last_week_saturday = this_week_saturday - datetime.timedelta(days=7)
        sessions = SessionLog.objects.prefetch_related('sessionsection_set')
        this_week_sessions = sessions.filter(date__range=[this_week_sunday, this_week_saturday])
        last_week_sessions = sessions.filter(date__range=[last_week_sunday, last_week_saturday])
        this_week = models.Prefetch('sessionlog_set', queryset=this_week_sessions, to_attr='this_week')
        last_week = models.Prefetch('sessionlog_set', queryset=last_week_sessions, to_attr='last_week')
        users = self.user_set.prefetch_related(this_week, last_week)
        arrow_counter = lambda sessions: sum(session.arrows_shot or 0 for session in sessions)
        section_minute_counter = lambda sections: sum(section.time or 0 for section in sections)
        minute_counter = lambda sessions: sum(section_minute_counter(session.sessionsection_set.all()) for session in sessions)
        stats.append({
            'type': 'Arrows shot',
            'this_week': self.get_stat_order(users, 'this_week', arrow_counter),
            'last_week': self.get_stat_order(users, 'last_week', arrow_counter),
        })
        stats.append({
            'type': 'All training time',
            'this_week': self.get_stat_order(users, 'this_week', minute_counter, natural_time),
            'last_week': self.get_stat_order(users, 'last_week', minute_counter, natural_time),
        })
        return stats

    def get_stat_order(self, users, week, func, display_func=None):
        users = [{'archer': user.first_name, 'value': func(getattr(user, week))} for user in users]
        users = sorted(users, key=lambda u: u['value'], reverse=True)
        if display_func is not None:
            for u in users:
                u['value'] = display_func(u['value'])
        return users


class User(AbstractUser):
    squad = models.ForeignKey(Squad, blank=True, null=True)
    public_profile = models.BooleanField(default=False)

    def uid(self):
        return self.social_auth.get(provider='facebook').uid


class TrainingCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'training categories'
        ordering = ['pk']


class TrainingType(models.Model):
    category = models.ForeignKey(TrainingCategory)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['pk']


class SessionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()
    venue = models.CharField(max_length=200, default='OUCofA session')
    arrows_shot = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, default='')

    def __unicode__(self):
        return 'Session for %s on %s' % (self.user, self.date)

    class Meta:
        ordering = ['-date']


class SessionSection(models.Model):
    session = models.ForeignKey(SessionLog)
    training_type = models.ForeignKey(TrainingType)
    time = models.PositiveIntegerField('Time (in minutes)')

    def __unicode__(self):
        return '%s minutes on %s' % (self.time, self.training_type)


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()
    shot_round = models.CharField(max_length=200)
    score = models.PositiveIntegerField()
    competition = models.BooleanField(default=False)
    notes = models.TextField(blank=True, default='')

    def __unicode__(self):
        return '%s: %s' % (self.shot_round, self.score)

    class Meta:
        ordering = ['-date']


class CoachNote(models.Model):
    subject = models.ForeignKey(User)
    author = models.ForeignKey(User, related_name='+')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField('Message')

    def __unicode__(self):
        return 'Notes on %s by %s' % (self.subject, self.author)

    class Meta:
        ordering = ['-timestamp']


class Video(models.Model):
    subject = models.ForeignKey(User)
    date = models.DateField()
    link = EmbedVideoField('Youtube link')
    notes = models.TextField(blank=True, default='')

    def __unicode__(self):
        return 'Video of %s on %s' % (self.subject, self.date)

    class Meta:
        ordering = ['-date']
