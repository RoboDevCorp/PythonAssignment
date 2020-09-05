from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import URLField
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .register import RegisterUrlForm
from .urlshortner import urlshortner
from .models import UrlDetails

# Create your views here.

def generatetoken(request):

    if request.method == 'POST':
        long_url_ = request.POST.get('long_url')
        print('Entered URL : '+str(long_url_))
        is_valid_url = validate_url(long_url_)
        message = ''
        if is_valid_url:
            print(is_valid_url)
            message = is_valid_url
        else :
            print('Ready')
            try:
                register_long_url = RegisterUrlForm(request.POST)
                RegisteringUrl = register_long_url.save(commit=False)
                generated_token = urlshortner().generate_token()
                new_short_url = 'http://127.0.0.1:8000/urlshortner/'+generated_token
                RegisteringUrl.short_url = generated_token
                print(generated_token)
                print(register_long_url)
                RegisteringUrl.save()
                message = "The shorturl generated is: "
                return render(request,'urlshortner.html',{'message':message,'short_url':new_short_url})
                #<a href='"+ new_short_url+"' target='_blank'>"+ new_short_url+"</a>"
            except ValueError as ve:
                print(ve)
                message = 'Either the entered URL is invalid or is already present in your records'
                #message for invalid URL
        return render(request,'urlshortner.html',{'message':message})
    else:
        return render(request,'urlshortner.html')

def validate_url(url):
    validate = URLValidator()    
    if url:        
        try:
            validate(url)
        except ValidationError as e:
            return e

def navigate(request, token):
    print('navigations on')
    print(request.method)
    try:
        fetched_url = UrlDetails.objects.filter(short_url=token)[0]
        print('token: '+token)
        print(fetched_url.long_url)
        fetched_url.number_hits += 1
        print(fetched_url.number_hits)
        fetched_url.save()
        return redirect(fetched_url.long_url)
    except:
        return render(request,'urlshortner.html',{'message':"Incorrect short URL entered.<br> Did you want to create a short URL"})

# @api_view([GET])
# def navigate(request, token):

    