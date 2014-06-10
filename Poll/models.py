from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserType(models.Model):
    user = models.OneToOneField(User)

    type = models.IntegerField(default=0, null=False)

    def getType(self):
        return self.type

    def __str__(self):
        return self.user.username

class Poll(models.Model):
    question   = models.CharField(max_length=256, null=False, blank=False)
    date_start = models.DateTimeField()
    date_end   = models.DateTimeField()
    type = models.IntegerField()

    def __str__(self):
        return str(self.question)

    def timespent(self):
        return int((timezone.now()-self.date_start)/(self.date_end - self.date_start)*100)


class Answer(models.Model):
    first_name = models.CharField(max_length=120, null=False, blank=False)
    last_name = models.CharField(max_length=120, null=False, blank=False)
    poll = models.ForeignKey(Poll)
    n_o_votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.first_name)

class Vote(models.Model):
    poll = models.ForeignKey(Poll)
    answer = models.ForeignKey(Answer)
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.id)


