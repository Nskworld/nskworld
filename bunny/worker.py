import threading

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
