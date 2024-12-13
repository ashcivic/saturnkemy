from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def file_manager(request):
    uploaded_file_url = None
    uploaded_files = os.listdir(settings.MEDIA_ROOT)  # Lista os arquivos na pasta de media

    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        # Recarregar a lista de arquivos após o upload
        uploaded_files = os.listdir(settings.MEDIA_ROOT)

    return render(request, 'gestor/file_manager.html', {
        'uploaded_file_url': uploaded_file_url,
        'uploaded_files': uploaded_files  # Passa a lista de arquivos para o template
    })
