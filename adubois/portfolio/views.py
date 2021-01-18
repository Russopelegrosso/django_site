from django.shortcuts import render, redirect
from .models import MyWorks
from .forms import MyWorkForm


def portfolio(request):
    works = MyWorks.objects.all()
    return render(request, 'portfolio/portfolio_page.html',{'works' : works})

def create(request):
    error = ''
    if request.method == 'POST':
        form = MyWorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверные данные'
    form = MyWorkForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'portfolio/create_page.html', context)