from django.contrib import admin

from .models import Poll, Answer, Vote, UserType


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
admin.site.register(UserType)