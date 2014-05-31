from django.db import models

class User(models.Model):
    login = models.CharField(max_length=25, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    first_name = models.CharField(max_length=120, null=False, blank=False)
    last_name = models.CharField(max_length=120, null=False, blank=False)
    typ = models.IntegerField() #mozliwe ze wyjebiemy

    def __str__(self):
        return str(self.login)

class Poll(models.Model):
    question  = models.CharField(max_length=25, null=False, blank=False)
    date_start = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_end = models.DateTimeField()
    type = models.IntegerField()
    def __str__(self):
        return str(self.question)


class Answer(models.Model):
    first_name = models.CharField(max_length=120, null=False, blank=False)
    last_name = models.CharField(max_length=120, null=False, blank=False)
    poll  = models.ForeignKey(Poll)
    n_o_votes = models.IntegerField()


    def __str__(self):
        return str(self.first_name)

class Vote(models.Model):
    poll  = models.ForeignKey(Poll)
    answer = models.ForeignKey(Answer)
    user  = models.ForeignKey(User)

    def __str__(self):
        return str(self.id)


