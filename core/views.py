from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hellotime (request):
    now = datetime.datetime.now()
    return HttpResponse(f"<h1>Hello, World!</h1> <p>It's {now}. </p>")

def screenprint(request):
    return render(request, "core/screenprint.html")

def mbb(request):
    return render(request, "core/mbb.html")
# comments comments comments
