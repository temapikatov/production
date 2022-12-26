from django.http import request, HttpResponse
from .models import *
import pandas as pd
# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


def home(request):
    item = Baka.objects.all().values()
    df = pd.DataFrame(item)
    ch = (len(df.axes[0]) * (len(df.axes[1]) - 1))
    percent = df.isnull().sum().sum() / ch * 100
    mydict = {
        "df": df.to_html(),
        "percent": percent
    }
    return render(request, 'index.html', context=mydict)


def download(request):
    item = Baka.objects.all().values()
    df = pd.DataFrame(item)
    df.to_csv("output.csv")
    fileObj = open('output.csv', 'rb')
    response = HttpResponse(fileObj,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="output.csv"'
    return (response)


class home_view(APIView):
    def get(self, request):
        csv_data = pd.read_csv('output.csv', keep_default_na=False)
        df = pd.DataFrame(csv_data)
        a = df.to_dict()
        # z = json.dumps(a)
        # df = df.fillna('1')
        ch = (len(df.axes[0]) * (len(df.axes[1]) - 2))
        # ch1 = sum(1 for line in open("output.csv") if line.isspace()) / ch * 100
        ch1 = (len(df[df['name']==''])+len(df[df['gender']==''])) / ch * 100
        a['percent'] = ch1
        return Response(a)
