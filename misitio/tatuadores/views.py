from django.shortcuts import render
from tatuadores.models import Notice


def index(request):
    Notices = Notice.objects.all()
    return render(request, 'index.html', {'Notice': Notices})

def principal(request):
    return render(request, 'opinion.html')
