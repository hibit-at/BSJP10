from django.shortcuts import render

from app.models import Ranking

# Create your views here.

def index(request):
    data = Ranking.objects.order_by('date').reverse().all()
    for d in data:
        d.date = f'{d.date.month}-{d.date.day}'
        d.n0 = d.n0 + '.jpg'
        d.n1 = d.n1 + '.jpg'
        d.n2 = d.n2 + '.jpg'
        d.n3 = d.n3 + '.jpg'
        d.n4 = d.n4 + '.jpg'
        d.n5 = d.n5 + '.jpg'
        d.n6 = d.n6 + '.jpg'
        d.n7 = d.n7 + '.jpg'
        d.n8 = d.n8 + '.jpg'
        d.n9 = d.n9 + '.jpg'
    params = {'data' : data}
    return render(request, 'index.html', params)
