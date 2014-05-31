from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

from .forms import UserForm

def home(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, "We will be in touch")
        return HttpResponseRedirect('/thank-you/')

    return render_to_response("user.html",
                              locals(),
                              context_instance=RequestContext(request))

def thankyou(request):

    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def createpoll(request):

    return render_to_response("createpoll.html",
                              locals(),
                              context_instance=RequestContext(request))