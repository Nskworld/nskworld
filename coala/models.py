import pytz
from datetime import timedelta
from django.db import models
from django.utils import timezone


def custom_strptime(time_str):
    """HH:mmのような時間も許容するカスタムstrptime関数"""
    if ':' not in time_str:
        raise ValueError("Invalid time format")
    
    hour, minute = map(int, time_str.split(":"))
    
    # 24:30を0:30に変換するような処理
    hour %= 24
    
    return timedelta(hours=hour, minutes=minute)

class Record(models.Model):
    """ 睡眠記録モデル """
    created_at = models.DateTimeField(auto_now_add=True)
    time_falling_asleep = models.CharField(max_length=5)
    time_getting_up = models.CharField(max_length=5)  
    time_going_bed = models.CharField(max_length=5)
    updated_at = models.DateTimeField(auto_now=True)

    def format_created_at(self):
        """ 作成日時を文字列に変換する
        Returns:
            str: 「yyyy年mm月dd日」のフォーマット文字列
        """
        return self.created_at.strftime("%Y年%m月%d日")

    def time_of_sleeping(self):
        """ 睡眠時間を算出する
        Returns:
            str: 睡眠時間
        """
        falling_asleep_time = custom_strptime(self.time_falling_asleep)
        getting_up_time = custom_strptime(self.time_getting_up)
        
        if getting_up_time >= falling_asleep_time:
            time_diff = getting_up_time - falling_asleep_time
        else:
            time_diff = (getting_up_time + timedelta(days=1)) - falling_asleep_time
            
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes = remainder // 60
        
        return f"{hours}時間{minutes}分"
    

class Performance(models.Model):
    """ パフォーマンスモデル """
    performance = models.CharField(max_length=20)
    registered_datetime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.performance
    
    def registered_date(self):
        """ 登録日のフォーマットを整形する
        Returns:
            str: 登録日
        """
        return self.registered_datetime.strftime("%Y年%m月%d日%H時%M分")


class Challenge(models.Model):
    """ チャレンジモデル

    evaluation:
        0: 未評価
        1: 継続する
        2: 止める
    """
    challenge = models.CharField(max_length=250)
    evaluation = models.IntegerField(default=0)
    registered_datetime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.challenge
     
    # TODO: Performanceのと全く同じなのでまとめる
    def registered_date(self):
        """ 登録日のフォーマットを整形する
        Returns:
            str: 登録日
        """
        return self.registered_datetime.strftime("%Y年%m月%d日")
