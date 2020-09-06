import urllib.parse
from .models import MobilePhone
from django.db.models import Avg
from django.shortcuts import render,redirect
from .form import RequestForm

def estimate_url(request):
    form = RequestForm()
    shorts = MobilePhone.objects.all()
    # 评论数量
    counter = MobilePhone.objects.all().count()
    # 情感倾向
    sent_avg = f" {MobilePhone.objects.aggregate(Avg('sentiments'))['sentiments__avg']:0.2f} "
    # 正向数量
    queryset = MobilePhone.objects.values('sentiments')
    condtions = {'sentiments__gte': 0.5}
    plus = queryset.filter(**condtions).count()
    # 负向数量
    queryset = MobilePhone.objects.values('sentiments')
    condtions = {'sentiments__lt': 0.5}
    minus = queryset.filter(**condtions).count()
    return render(request,'index.html',locals())

def request_url(request,name):
    if request.method == 'POST':
        try:
            condtions = {}
            form = RequestForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if cd['text']:
                    cd['text']= urllib.parse.unquote(cd['text'])
                    condtions['title__contains'] = cd['text']
                if cd['start_time']:
                    condtions['comment_date__gte'] = cd['start_time']
                if cd['end_time']:
                    condtions['comment_date__lte'] = cd['end_time']
                shorts = MobilePhone.objects.filter(**condtions)
                counter = MobilePhone.objects.filter(**condtions).count()
                # 情感倾向
                sent_avg = f"{MobilePhone.objects.filter(**condtions).aggregate(Avg('sentiments'))['sentiments__avg']:0.2f}"
                # 正向数量
                queryset = MobilePhone.objects.filter(**condtions).values('sentiments')
                condtions = {'sentiments__gte': 0.5}
                plus = queryset.filter(**condtions).count()
                # 负向数量
                queryset = MobilePhone.objects.filter(**condtions).values('sentiments')
                condtions = {'sentiments__lt': 0.5}
                minus = queryset.filter(**condtions).count()
                return render(request, 'index.html',locals())
        except Exception:
            form = RequestForm()
            point = '没有您搜索的信息...'
            return render(request, 'index.html',locals())

    if request.method == "GET":
        form = RequestForm()
        return render(request, 'index.html',locals())
