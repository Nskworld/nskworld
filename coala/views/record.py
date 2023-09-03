from django.shortcuts import render, get_object_or_404, redirect
from ..models import Record
from ..forms.record import RecordForm

def record_list(request):
    records = Record.objects.all()
    return render(request, 'coala/records/record_list.html', {'records': records})

def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'coala/records/record_detail.html', {'record': record})

def record_new(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('record_list')
    else:
        form = RecordForm()
    return render(request, 'coala/records/record_edit.html', {'form': form})

def record_edit(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'coala/records/record_edit.html', {'form': form})

def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    record.delete()
    return redirect('record_list')