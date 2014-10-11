from django.conf import settings
from django.db import models


class TrainingCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'training categories'


class TrainingType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.name


class SessionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()
    venue = models.CharField(max_length=200, default='OUCofA session')
    arrows_shot = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return 'Session for %s on %s' % (self.user, self.date)


class SessionSection(models.Model):
    session = models.ForeignKey(SessionLog)
    training_type = models.ForeignKey(TrainingType)
    time = models.PositiveIntegerField()
    notes = models.TextField(blank=True, default='')

    def __unicode__(self):
        return '%s minutes on %s' % (self.time, self.training_type)


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()
    shot_round = models.CharField(max_length=200)
    score = models.PositiveIntegerField()
    competition = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s: %s' % (self.shot_round, self.score)
