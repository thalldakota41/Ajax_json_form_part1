from django.shortcuts import render, HttpResponse, redirect 
#from models import *
from django.core import serializers

def index (request):
    return render(request, "landing.html")

def all_json(request):
    users = User.objects.all()
    users_json =serializers.serialize("json", users)
    return HttpResponse(users_json, content_type='application/json')

def all_html(request):
    users = Users.objects.all()
    return render(request, "all.html", {"users": users})
