import pytz
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
    
    # 文字列を整数にマッピング
    performance_mapping = {
        'bad': 0,
        'not so good': 1,
        'so-so': 2,
        'good': 3,
        'awesome': 4,
    }
    
    # UTC -> JST に変換するための設定
    jst = pytz.timezone('Asia/Tokyo')
    
    data_dict = defaultdict(list)
    
    for p in performances:
        # registered_datetimeをJSTに変換
        registered_datetime_jst = p.registered_datetime.astimezone(jst)
        
        hour_str = registered_datetime_jst.strftime("%Y-%m-%d %H:00")
        performance_value = performance_mapping.get(p.performance, 0)
        data_dict[hour_str].append(performance_value)
    
    labels = list(data_dict.keys())
    data = [sum(v)/len(v) for v in data_dict.values()]  # 平均値
    
    return render(request, 'coala/monitoring/monitoring.html', {'labels': labels, 'data': data})
