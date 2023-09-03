from django.shortcuts import render
from ..models import Performance
from collections import defaultdict

def performance_chart(request):
    performances = Performance.objects.all().order_by('registered_datetime')
    
    data_dict = defaultdict(list)
    
    for p in performances:
        hour_str = p.registered_datetime.strftime("%Y-%m-%d %H:00")
        data_dict[hour_str].append(p.performance)
    
    labels = list(data_dict.keys())
    data = [sum(map(int, v))/len(v) for v in data_dict.values()]  # 平均値
    
    return render(request, 'performance_chart.html', {'labels': labels, 'data': data})
