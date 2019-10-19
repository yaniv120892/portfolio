from django.shortcuts import render, get_object_or_404
from .models import Job
import os
from django.conf import settings
from django.http import HttpResponse, Http404


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})


def download_cv(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'CV-YanivDaye-SW-Eng.docx')
    print(file_path)
    print(os.path.exists(file_path))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
