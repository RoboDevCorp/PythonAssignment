from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import URLField
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from shorturl.models import UrlDetails
# Create your views here.

def search(request):
    
    print('navigations on')
    print(request.method)
    try:
        fetched_url = UrlDetails.objects.all()
        keyword = request.POST['seach-url']
        fetched_url = fetched_url.filter(long_url__icontains=keyword)
        print(fetched_url)

        return render(request,'search.html',{'fetched_url':fetched_url})
    except:
        return render(request,'search.html',{'message':"Incorrect short URL entered.<br> Did you want to create a short URL"})
