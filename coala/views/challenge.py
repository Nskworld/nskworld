from django.shortcuts import render, get_object_or_404, redirect
from ..models import Challenge
from ..forms.challenge import ChallengeForm, EvaluationForm

def challenge_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'coala/challenges/challenge_list.html', {'challenges': challenges})

def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    return render(request, 'coala/challenges/challenge_detail.html', {'challenge': challenge})

def challenge_new(request):
    if request.method == "POST":
        form = ChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.save()
            return redirect('challenge_list')
    else:
        form = ChallengeForm()
    return render(request, 'coala/challenges/challenge_edit.html', {'form': form})

def challenge_edit(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    if request.method == "POST":
        form = ChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.save()
            return redirect('challenge_list')
    else:
        form = ChallengeForm(instance=challenge)
    return render(request, 'coala/challenges/challenge_edit.html', {'form': form})

def evaluation_edit(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    if request.method == "POST":
        form = EvaluationForm(request.POST, instance=challenge)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.save()
            return redirect('challenge_list')
    else:
        form = EvaluationForm(instance=challenge)
    return render(request, 'coala/challenges/evaluation_edit.html', {'form': form})


def challenge_delete(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    challenge.delete()
    return redirect('challenge_list')