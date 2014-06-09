from django import forms

from .models import User, Poll, Answer


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ('question',)


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('first_name',)


