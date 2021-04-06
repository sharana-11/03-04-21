from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Index1</h1>")
def sample1(request):
    return render(request,"app1/qsp.html")