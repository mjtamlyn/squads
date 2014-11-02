from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from embed_video.fields import EmbedVideoField


class Squad(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['pk']


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
