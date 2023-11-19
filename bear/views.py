from django.shortcuts import render, get_object_or_404, redirect
from .models import Log
from .forms import LogForm

def log_list(request):
    logs = Log.objects.all()
    return render(request, 'logs/log_list.html', {'logs': logs})

def log_detail(request, pk):
    log = get_object_or_404(Log, pk=pk)
    return render(request, 'logs/log_detail.html', {'log': log})

def log_new(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.save()
            return redirect('log_list')
    else:
        form = LogForm()
    return render(request, 'logs/log_edit.html', {'form': form})

def log_edit(request, pk):
    log = get_object_or_404(Log, pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            log.save()
            return redirect('log_list')
    else:
        form = LogForm(instance=log)
    return render(request, 'logs/log_edit.html', {'form': form})

def log_delete(request, pk):
    log = get_object_or_404(Log, pk=pk)
    log.delete()
    return redirect('log_list')
