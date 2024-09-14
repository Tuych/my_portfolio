from django.shortcuts import render
from .models import AboutMe, Skills
from django.shortcuts import get_object_or_404
from datetime import date
from .models import Projects


def index(request):
    my_info = get_object_or_404(AboutMe)
    skills = Skills.objects.all()

    projects = Projects.objects.all()

    today = date.today()
    age = (today.year - 2000)

    context = {
        'info': my_info,
        'age': age,
        'skills': skills,
        'projects': projects
        }
    return render(request, 'main/index.html', context)


def portfolio_detail(request, pk):
    project = get_object_or_404(Projects, id=pk)
    context = {
        'project': project
    }
    return render(request, 'main/portfolio-details.html', context)