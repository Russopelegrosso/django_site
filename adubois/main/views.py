from django.shortcuts import render


def index(request):
    cintext={
        'title': 'Main Page',
    }
    return render(request, 'main/index.html', cintext)


def about(request):
    return render(request, 'main/about.html')

