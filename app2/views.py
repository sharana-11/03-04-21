from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Index of app2</h1>")
def sample2(request):
    return render(request,"app2/qsp2.html")