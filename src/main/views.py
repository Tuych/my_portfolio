from django.shortcuts import render
from .models import AboutMe, Skills
from django.shortcuts import get_object_or_404
from datetime import date
from .models import Projects


def index(request):
    my_info = get_object_or_404(AboutMe)
    skills = Skills.objects.all()

    projects = Projects.objects.all()

    context = {
        'info': my_info,
        'skills': skills,
        'projects': projects,
        'navbar_section': True,
    }
    return render(request, 'main/index.html', context)


def portfolio_detail(request, pk):
    project = get_object_or_404(Projects, id=pk)
    context = {
        'project': project
    }
    return render(request, 'main/portfolio-details.html', context)


def custom_404(request, exception):
    return render(request, 'main/404.html', status=404)
