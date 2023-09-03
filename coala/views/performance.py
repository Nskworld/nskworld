from django.shortcuts import render, get_object_or_404, redirect
from ..models import Performance
from ..forms.performance import PerformanceForm

def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'coala/performances/performance_list.html', {'performances': performances})

def performance_new(request):
    if request.method == "POST":
        form = PerformanceForm(request.POST)
        if form.is_valid():
            performance = form.save(commit=False)
            performance.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'coala/performances/performance_edit.html', {'form': form})

def performance_edit(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == "POST":
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            performance = form.save(commit=False)
            performance.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm(instance=performance)
    return render(request, 'coala/performances/performance_edit.html', {'form': form})

def performance_delete(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    performance.delete()
    return redirect('performance_list')