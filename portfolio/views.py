from django.shortcuts import render
from .models import Project


def index(request):
    project = Project.objects.all()

    return render(request, 'index.html', {'project': project})
