# views.py
import os
from django.conf import settings
from django.shortcuts import render 
from .alert import SendMessageToSlack
from .forms import UploadCSVForm
from .worker import BulkRegistrationPerformance

def upload_csv(request):
    """ 一括処理用のCSVファイルをアップロードする """
    message = ''
    webhook_url = settings.WEBHOOK_URL

    if request.method == 'POST':
        file_path = f'media/upload_cache/{request.FILES["csv_file"].name}'
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with open(file_path, 'wb+') as destination:
                    for chunk in request.FILES["csv_file"].chunks():
                        destination.write(chunk)  
                worker = BulkRegistrationPerformance()
                worker.process_csv_in_threads(file_path)
                message = 'ファイルアップロードに成功しました'
                os.remove(file_path)
            except Exception as e:
                message = 'ファイルアップロードに失敗しました: ' + str(e)
        else:
            message = 'ファイルアップロードに失敗しました'
    else:
        form = UploadCSVForm()

    SendMessageToSlack(webhook_url, message)
    return render(request, 'bunny/upload.html', {'form': form, 'message': message})
