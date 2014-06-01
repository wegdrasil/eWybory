from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template import Context, loader
from Poll.models import Poll
from django.http import HttpResponse

from .forms import UserForm

def home(request):
    context = RequestContext(request)


    category_list = Poll.objects.order_by('-question')[:5]
    context_dict = {'polles': category_list}

    # Render the response and send it back!

    # if form.is_valid():
    #     save_it = form.save(commit=False)
    #     save_it.save()
    #     messages.success(request, "We will be in touch")
    #     return HttpResponseRedirect('/thank-you/')


    return render_to_response('home.html',
                              context_dict,
                              context_instance=RequestContext(request))
def fu():
    pass


def thankyou(request):

    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def voting(request):

    return render_to_response("voting.html",
                              locals(),
                              context_instance=RequestContext(request))

def result(request):

    return render_to_response("result.html",
                              locals(),
                              context_instance=RequestContext(request))

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()


    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered}, context)

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)

#@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')