from django.shortcuts import render
from ..models import Performance
from collections import defaultdict

def monitoring(request):
    """ モニタリングする情報を載せる関数

    Args:
        request

    Returns:
        各種モニタリング情報
        ※ 現状は時間ごとのパフォーマンスのグラフのみ表示している
    """
    performances = Performance.objects.all().order_by('registered_datetime')
    
    data_dict = defaultdict(list)
    
    for p in performances:
        hour_str = p.registered_datetime.strftime("%Y-%m-%d %H:00")
        data_dict[hour_str].append(p.performance)
    
    labels = list(data_dict.keys())
    data = [sum(map(int, v))/len(v) for v in data_dict.values()]  # 平均値
    
    return render(request, 'monitoring.html', {'labels': labels, 'data': data})
