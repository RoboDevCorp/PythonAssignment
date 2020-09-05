from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import URLField
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from shorturl.models import UrlDetails

# Create your views here.


def analytics(request, token):
    print('analytics on')
    print(request.method)
    try:
        fetched_url = UrlDetails.objects.filter(short_url=token)[0]
        print('token: '+token)
        print(fetched_url.long_url)
        return render(request,'AnalyticsDashboard.html',{'long_url':fetched_url.long_url, 'short_url':fetched_url.short_url, 'count':fetched_url.number_hits})
    except:
        return render(request,'AnalyticsDashboard.html',{'message':"Incorrect short URL entered.<br> Did you want to create a short URL"})

    