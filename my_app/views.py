from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    html = "<html><body>you are hitting the hello world view ! </body></html>" 
    return HttpResponse(html)

def hello_temp(request):
    return render(request,"hello_temp.html")
