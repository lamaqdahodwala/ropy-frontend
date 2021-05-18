from django.shortcuts import render
import requests
import django.core.handlers.wsgi as wsgi
# Create your views here.
def index(req:wsgi.WSGIRequest):
    return render(req, 'index.html')

def byUsername(req:wsgi.WSGIRequest):
    username = req.POST.get('username')
    request = requests.get('http://127.0.0.1:8000/person/{u}'.format(u=username))
    print(request.text)
    return render(req, 'index.html')