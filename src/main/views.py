from django.shortcuts import render
from .models import AboutMe, Skills
from django.shortcuts import get_object_or_404
from datetime import date


def index(request):
    my_info = get_object_or_404(AboutMe)
    skills = Skills.objects.all()

    today = date.today()
    age = (today.year - 2000)

    context = {
        'info': my_info,
        'age': age,
        'skills': skills,
        }
    return render(request, 'main/index.html', context)
