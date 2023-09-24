# views.py
from django.shortcuts import render
from .forms import UploadCSVForm

def upload_csv(request):
    """ 一括処理用のCSVファイルをアップロードする """
    message = ''

    if request.method == "POST":
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with open(f'media/upload_cache/{request.FILES["csv_file"].name}', 'wb+') as destination:
                    for chunk in request.FILES["csv_file"].chunks():
                        destination.write(chunk)
                message = "ファイルアップロードに成功しました"
            except Exception as e:
                message = "ファイルアップロードに失敗しました: " + str(e)
        else:
            message = "ファイルアップロードに失敗しました"

    else:
        form = UploadCSVForm()

    return render(request, 'bunny/upload.html', {'form': form, 'message': message})
