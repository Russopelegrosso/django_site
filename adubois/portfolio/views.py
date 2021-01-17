from django.shortcuts import render
from .models import MyWorks


def portfolio(request):
    works = MyWorks.objects.all()
    return render(request, 'portfolio/portfolio_page.html',{'works' : works})

def create(request):

    return render(request, 'portfolio/create_page.html',{})