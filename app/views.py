from django.shortcuts import render

from app.models import Ranking

# Create your views here.

def index(request):
    data = Ranking.objects.order_by('date').reverse().all()
    for d in data:
        d.date = f'{d.date.day}'
    params = {'data' : data}
    return render(request, 'index.html', params)
