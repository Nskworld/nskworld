import pytz
from django.shortcuts import render
from ..models import Performance, Record
from collections import defaultdict


def monitoring(request):
    """ モニタリングする情報を載せる関数

    Args:
        request

    Returns:
        各種モニタリング情報
    """
    
    jst = pytz.timezone('Asia/Tokyo')   # UTC -> JST に変換するための設定
    performances = Performance.objects.all().order_by('registered_datetime')
    records = Record.objects.all().order_by('created_at')
    
    # パフォーマンスグラフを表示するための処理
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
    performance_data = [sum(v)/len(v) for v in data_dict.values()]  # 平均値
    
    
    # 睡眠時間グラフを表示するための処理
    sleep_data_dict = defaultdict(list)
    
    for r in records:
        date_str = r.format_created_at().replace("年", "-").replace("月", "-").replace("日", "")
        time_of_sleeping = r.time_of_sleeping()
        hours, minutes = map(int, time_of_sleeping.replace("時間", " ").replace("分", "").split())
        sleep_duration = hours + minutes / 60.0  # 睡眠時間を小数点の時間に変換
        sleep_data_dict[date_str].append(sleep_duration)
    
    sleep_data_dict_with_time = {}
    for label in labels:
        date_str = label.split('\n')[-1]
        sleep_duration_avg = sum(sleep_data_dict.get(date_str, [0])) / len(sleep_data_dict.get(date_str, [1]))
        sleep_data_dict_with_time[label] = sleep_duration_avg
        
    sleep_data = [sleep_data_dict_with_time.get(label, None) for label in labels]
    
    return render(request, 'coala/monitoring/monitoring.html', {'labels': labels, 'performance_data': performance_data, 'sleep_data': sleep_data})

