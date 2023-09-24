import csv
import threading
from datetime import datetime
from django.utils import timezone

from ..coala.models import Performance

class MultiThreadWorker:
    def __init__(self, num_threads=3):
        self.num_threads = num_threads
        self.threads = []

    # 関数を指定してスレッドを起動するメソッド
    def run_in_threads(self, func):
        for i in range(self.num_threads):
            thread = threading.Thread(target=func, args=(i,))
            thread.start()
            self.threads.append(thread)

        for thread in self.threads:
            thread.join()

        # リストを空にして次の実行のためにクリアする
        self.threads = []
        
        return print("All threads have finished!")
    
class BulkRegistrationPerformance:
    def __init__(self):
        # エラーデータを保存するためのリスト
        self.error_data = []

    def create_performance(self, row):
        try:
            performance = row['Performance']
            date_str = row['Date']
            time_val = int(row['Time'])

            # 時間の整数値をdatetimeオブジェクトに変換
            registered_datetime_str = f"{date_str} {time_val}:00:00"
            registered_datetime = datetime.strptime(registered_datetime_str, "%Y-%m-%d %H:%M:%S")
            registered_datetime = timezone.make_aware(registered_datetime)

            return Performance(performance=performance, registered_datetime=registered_datetime)
    
        except ValueError as ve:
            # 例外処理：整数への変換エラーや日付フォーマットのエラーなど
            self.error_data.append(row)
            print(f"Error with row {row}: {ve}")
            return None
        except KeyError:
            # カラムが存在しない場合の例外処理
            self.error_data.append(row)
            print(f"Error with row {row}: Missing required column")
            return None
    
    def save_data(self, performance_obj):
        if performance_obj:
            performance_obj.save()
            
    def run_by_chunk(self, chunk_index, chunks):
        chunk = chunks[chunk_index]
        for row in chunk:
            perf = self.create_performance(row)
            self.save_data(perf)

    def process_csv_in_threads(self, filename, num_threads=3):
        with open(filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            all_rows = list(reader)

            chunk_size = 10000
            chunks = [all_rows[i:i+chunk_size] for i in range(0, len(all_rows), chunk_size)]

            worker = MultiThreadWorker(num_threads=num_threads)

            # 関数を部分的に適用して、chunkのインデックスを引数として受け取る新しい関数を作成します。
            func_with_chunks = lambda i: self.run_by_chunk(i, chunks)
            worker.run_in_threads(func_with_chunks)

        # エラーデータをCSVとして保存
        with open('error_data.csv', 'w', newline='') as error_file:
            writer = csv.DictWriter(error_file, fieldnames=['Performance', 'Date', 'Time'])
            writer.writeheader()
            writer.writerows(self.error_data)


