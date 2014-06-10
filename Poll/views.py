from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.utils import simplejson
from django.contrib.auth import authenticate, login, logout
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.template import Context, loader
from Poll.models import Poll, Answer, Vote, User, UserType
from django.http import HttpResponse
from django.utils import timezone

from .forms import UserForm, PollForm

def home(request):
    context = RequestContext(request)


    category_list = Poll.objects.order_by('-question')[:5]


    context_dict = {'polles': category_list}


    return render_to_response('home.html',
                              context_dict,
                              context_instance=RequestContext(request))


def thankyou(request):

    selected_choices_id = []
    selected_choices_id = request.POST.getlist('Answer')
    for i in range(len(selected_choices_id)):
        selected_choices_id[i] = str(selected_choices_id[i]).strip('/')
    print(selected_choices_id)


    try:

        p = Answer.objects.get(id=selected_choices_id[0]).poll

        answers = []
        for i in range(len(selected_choices_id)):
            answers.append(Answer.objects.filter(pk=selected_choices_id[i])[0])

        print(answers)

        if Vote.objects.filter(user=request.user.id, poll=p).exists():
            messages.error(request, "Przecież już głosowałeś!")

        else:
            for a in answers:
                print(a)
                a.n_o_votes += 1
                a.save()
                no = a.n_o_votes

                v = Vote(poll=p, answer=a, user=request.user)
                v.save()

            messages.success(request, "Dziękujemy za oddanie głosu")

    except (KeyError):
         return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))
    else:
         return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def voting(request, Poll_id):

    p = Poll.objects.get(id=Poll_id)

    if not request.user.is_authenticated():
        return render_to_response("badlogin.html",
                                   locals(),
                                   context_instance=RequestContext(request))

    elif p.type != request.user.usertype.getType() or request.user.usertype.getType() == 0:

        messages.error(request, "Nie masz uprawnień do głosowania w tej ankiecie!")
        return render_to_response("voting.html",
                           locals(),
                           context_instance=RequestContext(request))

    elif p.date_end < timezone.now():

        selected_poll = Poll_id

        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=results.pdf'

        pdf = canvas.Canvas(response)
        p = Poll.objects.filter(pk=selected_poll)

        pdf.drawString(100, 800, "Wyniki ankiety: " + p[0].question)

        a = Answer.objects.all()

        v = Vote.objects.filter(poll=selected_poll)

        peoplevoted = 0
        allpeople = len(UserType.objects.filter(type=p[0].type))

        for u in User.objects.all():
            peoplevoted += v.filter(user=u.id).count()

        for i in  range(len(a)):

            if a[i].poll.id == int(selected_poll):

                pdf.drawString(100, 750 - (i*12), str(a[i].first_name) + " " + a[i].last_name + "  " + str(int(a[i].n_o_votes/len(v)*100)) + "%")

        pdf.drawString(100, 500, "W ankiecie wzielo udzial " + str(peoplevoted) + " osob.")
        pdf.drawString(100, 475, "Liczba uprawnionych do glosowania: " + str(allpeople) + ".")
        pdf.drawString(100, 450, "Frekwencja wynosi " + str(int(peoplevoted/allpeople*100.0)) + " %.")


        pdf.showPage()
        pdf.save()
        return response

    else:
        p = Poll.objects.all()
        a = Answer.objects.all()

        selected_poll = {}
        for i in p:
            if i.id == int(Poll_id):
                selected_poll = {'poll': i}


        selected_answers = []
        for i in a:
            if i.poll_id == int(Poll_id):
                selected_answers.append(i)

        selected_poll.update({'answers': selected_answers})

        print()


        return render_to_response("voting.html",
                                   selected_poll,
                                   context_instance=RequestContext(request))

def result(request, Poll_id):

    poll = Poll_id

    results = []
    for a in  Answer.objects.all():
        if a.poll.id == int(poll):
            results.append([a.first_name + " " + a.last_name, a.n_o_votes])

    json_list = simplejson.dumps(results)

    return render_to_response("result.html",
                               # {'json_list': json_list},
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

            ut = UserType(user=user, type=0)
            ut.save()

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









