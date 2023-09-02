from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Emotion
from ..forms.emotion import EmotionForm

def emotion_list(request):
    emotions = Emotion.objects.all()
    return render(request, 'snake/emotion_list.html', {'emotions': emotions})


def emotion_new(request):
    if request.method == "POST":
        form = EmotionForm(request.POST)
        if form.is_valid():
            emotion = form.save(commit=False)
            emotion.save()
            return redirect('emotion_list')
    else:
        form = EmotionForm()
    return render(request, 'snake/emotion_edit.html', {'emotion': emotion})


def emotion_delete(request, pk):
    emotion = get_object_or_404(Emotion, pk=pk)
    emotion.delete()
    return redirect('emotion_list')
