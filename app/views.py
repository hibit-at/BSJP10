from itertools import chain

from django.shortcuts import render

from app.models import Ranking

# Create your views here.


def index(request):
    freq = request.GET.get('q')
    if freq != 'day' and freq != 'month':
        freq = 'week'
    print(freq)
    years = [str(i) for i in range(2020,2022)]
    years.reverse()
    months = [str(i).zfill(2) for i in range(1,13)]
    months.reverse()
    year_by_list = []
    for y in years:
        month_by_list = []
        for m in months:
            data = Ranking.objects.filter(date__year=y).filter(date__month=m)
            if freq=='day':
                data = data.order_by('date').reverse()
            elif freq=='month':
                data = data.filter(date__day = 1)
            else:
                data1 = data.filter(date__day = 1)
                data2 = data.filter(date__day = 8)
                data3 = data.filter(date__day = 15)
                data4 = data.filter(date__day = 22)
                data = list(chain(data4,data3,data2,data1))
            if len(data) == 0:
                continue
            month_by_list.append({'month' : int(m) , 'data' : data})
        year_by_list.append({'year' : y, 'data' : month_by_list})
    params = {'year_by' : year_by_list, 'freq' : freq}
    return render(request, 'index.html', params)
