from django.db import models

#class User(models.Model):
    #login = models.CharField(max_length=25)
    #password = models.CharField(max_length=255)
 #   email = models.EmailField()
 #   first_name = models.CharField(max_length=120, null=True, blank=True)
 #   last_name = models.CharField(max_length=120, null=True, blank=True)
 #   timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
 #   updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
 #   def __str__(self):
 #       return str(self.email)

#class Poll(models.Model):
#    question      = models.CharField(max_length = 255)
#
#    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#    #date_creation = models.DateField()
#    #date_ending   = models.DateField()
#
#    def __unicode__(self):
#        return smart_unicode(self.question)
#
#class Answer(models.Model):
#    answer = models.CharField(max_length=255)
#    votes = models.IntegerField()
#
#    def __unicode__(self):
#        return smart_unicode(self.answer)



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
    poll  = models.ForeignKeyey(Poll)
    n_o_votes = models.IntegerField()


    def __str__(self):
        return str(self.first_name)

class Vote(models.Model):
    poll  = models.ForeignKey(Poll)
    answer = models.ForeignKey(Answer)
    user  = models.ForeignKey(User)


