from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Challenge

SOLVED_KEY = 'solved_challenges'


def solved_ids(request):
    return set(request.session.get(SOLVED_KEY, []))


def challenge_list(request):
    challenges = Challenge.objects.all()
    solved = solved_ids(request)
    total_points = sum(c.points for c in challenges if c.pk in solved)
    context = {
        'challenges': challenges,
        'solved': solved,
        'total_points': total_points,
    }
    return render(request, 'home/challenge_list.html', context)


def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    solved = solved_ids(request)
    is_solved = challenge.pk in solved

    if request.method == 'POST':
        if challenge.check_flag(request.POST.get('flag', '')):
            solved.add(challenge.pk)
            request.session[SOLVED_KEY] = sorted(solved)
            messages.success(request, 'Correct flag! Challenge solved.')
            return redirect('home:challenge_detail', pk=challenge.pk)
        messages.error(request, 'That flag is not correct. Try again.')

    return render(request, 'home/challenge_detail.html', {
        'challenge': challenge,
        'is_solved': is_solved,
    })
