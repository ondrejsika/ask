# python
import json

# django
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# django contrib
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

# libs

# project
from ask.models import Poll, Question, UserAnswer, Payout, Profile
from ask.forms import ProfileForm


@login_required
def home_view(request):
    unanwered_polls = Poll.objects.exclude(id__in=request.user.profile.completed_polls.values_list('id', flat=True))

    return render(request, 'home.html', {
        'unanwered_polls': unanwered_polls,
    })


@login_required
def poll_view(request, poll_id, question_id=None):
    poll = Poll.objects.get(id=poll_id)
    if question_id:
        question = Question.objects.get(id=question_id)
    else:
        answered = Question.objects.filter(useranswer__user=request.user, poll=poll)
        unanswered_questions = Question.objects.filter(poll=poll).exclude(id__in=answered.values_list('id', flat=True))
        if unanswered_questions.count():
            return HttpResponseRedirect(reverse('poll_question', args=(poll_id, unanswered_questions.first().id)))
        return HttpResponseRedirect(reverse('poll_done', args=(poll_id, )))

    return render(request, 'poll.html', {
        'poll': poll,
        'question': question,
    })


@login_required
def answer_process(request, poll_id, question_id):
    question = Question.objects.get(poll_id=poll_id, id=question_id)
    answer = UserAnswer(user=request.user, poll_id=question.poll_id, question_id=question.id)
    answer.answer = request.GET['answer']
    answer.save()
    return HttpResponseRedirect(request.GET['next'])


@login_required
def poll_done_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    answered = Question.objects.filter(useranswer__user=request.user, poll=poll)
    unanswered_questions = Question.objects.filter(poll=poll).exclude(id__in=answered.values_list('id', flat=True))
    if unanswered_questions.count() == 0:
        request.user.profile.completed_polls.add(poll)
        request.user.profile.save()

    return render(request, 'poll_done.html', {
        'poll': poll,
    })


@login_required
def payouts_view(request):
    payouts = Payout.objects.filter(user=request.user)

    return render(request, 'payouts.html', {
        'payouts': payouts,
    })

@login_required
def settings_view(request):
    data = request.POST if request.POST.get('form') == 'profile_form' else None
    profile_form = ProfileForm(data, instance=request.user.profile)
    if profile_form.is_valid():
        profile_form.save()
        return HttpResponseRedirect(reverse('settings')+'?msg=Ulozeno')

    data = request.POST if request.POST.get('form') == 'password_change_form' else None
    password_change_form = PasswordChangeForm(request.user, data)
    if password_change_form.is_valid():
        password_change_form.save()
        return HttpResponseRedirect(reverse('settings')+'?msg=Nastaveno')

    return render(request, 'settings.html', {
        'msg': request.GET.get('msg'),
        'profile_form': profile_form,
        'password_change_form': password_change_form,
    })


def register_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        Profile(user=user).save()
        return HttpResponseRedirect(reverse('register_done'))
    return render(request, 'register_user.html', {
        'form': form,
    })


def register_done(request):
    return render(request, 'register_done.html')
