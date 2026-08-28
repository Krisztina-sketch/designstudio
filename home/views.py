from django.shortcuts import render
from orders.models import DesignService


def home(request):
    services = DesignService.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'home/index.html', context)
