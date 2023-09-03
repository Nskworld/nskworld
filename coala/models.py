from django.db import models

class Record(models.Model):
    time_going_bed = models.IntegerField()
    time_falling_asleep = models.IntegerField()
    time_getting_up = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def convert_time(self, time_value):
        """ 選択された数値を30分刻みの時間表記に変換します

        Args:
            time_value (int): 0から47までの整数

        Returns:
            str: 0:00から30分刻みでtime_valueを割り当てた時に該当する値を時刻表記した文字列
        """
        if time_value < 0 or time_value > 47:
            return "Unknown"

        hours = time_value // 2
        minutes = (time_value % 2) * 30
        return f"{hours}:{minutes:02d}"

    def convert_time_going_bed(self):
        return self.convert_time(self.time_going_bed)

    def convert_time_falling_asleep(self):
        return self.convert_time(self.time_falling_asleep)

    def convert_time_getting_up(self):
        return self.convert_time(self.time_getting_up)


