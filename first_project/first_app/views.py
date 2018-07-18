from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AcessRecord

def index(request):
# Create your views here.
  webpages_list=AcessRecord.objects.order_by('date')
  date_dict = {'acessrecord':webpages_list}
  return render(request,'first_app/index.html',context=date_dict)
