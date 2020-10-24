from django.shortcuts import render
from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects
    response = render(request, 'jobs/home.html', {'jobs':jobs})
    return response
