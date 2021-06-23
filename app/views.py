from django.db.models.query import QuerySet
from django.shortcuts import render

from app.models import Ranking

# Create your views here.


def index(request):
    years = [str(i) for i in range(2020,2022)]
    years.reverse()
    months = [str(i).zfill(2) for i in range(1,13)]
    months.reverse()
    year_by_list = []
    for y in years:
        month_by_list = []
        for m in months:
            data = Ranking.objects.filter(date__year=y).filter(date__month=m).order_by('date').reverse()
            if len(data) == 0:
                continue
            month_by_list.append({'month' : int(m) , 'data' : data})
        year_by_list.append({'year' : y, 'data' : month_by_list})
    params = {'year_by' : year_by_list}
    return render(request, 'index.html', params)
