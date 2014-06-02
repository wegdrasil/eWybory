from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.utils import simplejson
from django.contrib.auth import authenticate, login, logout
from django.template import Context, loader
from Poll.models import Poll, Answer, Vote
from django.http import HttpResponse

from .forms import UserForm, PollForm

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


def thankyou(request):


    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    # p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice =pk=request.POST['Answer']
    except (KeyError):
        # Pokaz ponownie formularz do glosowania.
         return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        # Zawsze zwróć HttpResponseRedirect po udanym obsłużeniu danych z POST.
        # To zapewnia, że dane nie zostaną wysłane dwa razy, jeżeli użytkownik
        # kliknie w przeglądarce przycisk Wstecz .
         return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))




    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def voting(request, Poll_id):
     #form = PollForm(request.POST or None)
     #db_get_data = form.Meta.model.objects.all()
     #
     #for cur in db_get_data:
     #    for field in cur._meta.fields: # field is a django field
     #        if field.name == 'question':
     #             print(field.name)
     #
     #if form.is_valid():
     #    save_it = form.save(commit=False)
     #    save_it.save()
     #    messages.success(request, "We will be in touch")
     #    return HttpResponseRedirect('/thankyou/')

    #foo = Poll.objects.order_by('-question')[:5]
    #context_dict = {'polles': category_list}

    #p = Poll.objects.order_by('question')#.first()
    if not request.user.is_authenticated():
        return render_to_response("badlogin.html",
                                   locals(),
                                   context_instance=RequestContext(request))
    else:
        p = Poll.objects.all()
        a = Answer.objects.all()

        selected_poll = {}
        for i in p:
            if i.id == int(Poll_id):
                selected_poll = {'poll': i.question}


        selected_answers = []
        for i in a:
            if i.poll_id == int(Poll_id):
                selected_answers.append(i)

        selected_poll.update({'answers': selected_answers})

        print()


        return render_to_response("voting.html",
                                   selected_poll,
                                   context_instance=RequestContext(request))

def result(request):

    browser_stats = [["Chrome", 52.9], ["Firefox", 27.7], ["Opera", 1.6],
                     ["Internet Explorer", 12.6], ["Safari", 4]]

    json_list = simplejson.dumps(browser_stats)

    return render_to_response("result.html",
                                {'json_list': json_list},
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