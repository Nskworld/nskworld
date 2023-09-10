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
    # UTC -> JST に変換するための設定
    jst = pytz.timezone('Asia/Tokyo')
    performances = Performance.objects.all().order_by('registered_datetime')
    
    
    data_dict = defaultdict(list)
    labels = []
    # 文字列を整数にマッピング
    performance_mapping = {
        'bad': 0,
        'not so good': 1,
        'so-so': 2,
        'good': 3,
        'awesome': 4,
    }
    prev_date_str = None  # 直前のレコードの日付を保存するための変数
    
    for p in performances:
        # registered_datetimeをJSTに変換
        registered_datetime_jst = p.registered_datetime.astimezone(jst)
        
        date_str = registered_datetime_jst.strftime("%Y-%m-%d")
        time_str = registered_datetime_jst.strftime("%H:00")
        
        # 同一日に複数レコードが作成された場合、2レコード目以降に時間のみ表示する
        if prev_date_str == date_str:
            hour_str = time_str
        else:
            hour_str = f"{time_str}\n{date_str}"
            prev_date_str = date_str
        
        labels.append(hour_str)
        performance_value = performance_mapping.get(p.performance, 0)
        
        data_dict[hour_str].append(performance_value)
    
    labels = list(data_dict.keys())
    data = [sum(v)/len(v) for v in data_dict.values()]  # 平均値
    
    return render(request, 'coala/monitoring/monitoring.html', {'labels': labels, 'data': data})
