from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse('this is the about page')

def event(request):
    return HttpResponse('this is the event page')

def community(request):
    return HttpResponse('this is the community page')