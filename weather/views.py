from django.shortcuts import render


def home(request):
    return render(request, 'weather/home.html', {})


def about(request):
    return render(request, 'weather/about.html', {})
