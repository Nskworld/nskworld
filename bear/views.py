import base64
import boto3
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Log
from .forms import LogForm

def upload_to_s3(file):
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    file_name = file.name
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    s3.upload_fileobj(file, bucket_name, file_name)
    return file_name

def get_image_from_s3(image_id):
    s3_client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    try:
        file = s3_client.get_object(Bucket=bucket_name, Key=image_id)
        return file['Body'].read()
    except Exception as e:
        print(f"Error getting file {image_id} from S3: {e}")
        return None

def encode_image(image_data):
    return base64.b64encode(image_data).decode('utf-8')

def log_list(request):
    logs = Log.objects.all()
    return render(request, 'bear/log_list.html', {'logs': logs})

def log_detail(request, pk):
    log = get_object_or_404(Log, pk=pk)
    image_data = get_image_from_s3(log.image_id)
    if image_data:
        encoded_image = encode_image(image_data)
    else:
        encoded_image = None
    context = {
        'log': log,
        'encoded_image': encoded_image
    }
    return render(request, 'bear/log_detail.html', context)

def log_new(request):
    if request.method == "POST":
        form = LogForm(request.POST, request.FILES)
        
        if form.is_valid():
            log = form.save(commit=False)
            image = request.FILES.get('image')
            if image:
                image_id = upload_to_s3(image)
                log.image_id = image_id
            log.save()
            return redirect('log_list')
    else:
        form = LogForm()
    return render(request, 'bear/log_edit.html', {'form': form})

def log_edit(request, pk):
    log = get_object_or_404(Log, pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST, request.FILES, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            log.save()
            return redirect('log_list')
    else:
        form = LogForm(instance=log)
    return render(request, 'bear/log_edit.html', {'form': form})

def log_delete(request, pk):
    log = get_object_or_404(Log, pk=pk)
    log.delete()
    return redirect('log_list')
