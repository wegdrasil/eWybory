from django.contrib import admin

from .models import User, Poll, Answer, Vote

#class UserAdmin(admin.ModelAdmin):
#    class Meta:
#        model = User

class PollAdmin(admin.ModelAdmin):
    class Meta:
        model = Poll

class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer

class VoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Vote

admin.site.register(Poll, PollAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Vote, VoteAdmin)