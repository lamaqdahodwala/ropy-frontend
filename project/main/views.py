from django.shortcuts import render
import requests
# Create your views here.
def index(req):
    return render(req, 'index.html')

def byUsername(req):
    requests.post
    return render(req, 'index.html')