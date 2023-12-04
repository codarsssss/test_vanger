from django.shortcuts import render

from .models import SliderImage


def index(request):
    images = SliderImage.published.all()

    context = {
        'title': 'Главная',
        'images': images,
    }
    return render(request, 'home_app/index.html', context=context)
