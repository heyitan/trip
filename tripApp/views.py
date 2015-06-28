from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from models import Resort
from utils import render


def index(request):
    spot_list = Resort.objects.order_by('rate_star')
    #return HttpResponse(template.render(context))
    for s in spot_list:
        print s.id, type(s.id)
    return render(request, 'trip/main.html', {'spot_list': spot_list})

def detail(request, spot_id):
    spot = get_object_or_404(Resort, id=spot_id)
    return render(request, 'trip/detail.html', {'spot': spot})

# Create your views here.
