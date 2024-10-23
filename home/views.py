from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')#ye vo wala hai yo post request se milega
        password = request.POST.get('password')
        contact = Contact(name = name1 , password = password)
        # messages.success(request, 'your login was successful')
        contact.save()#saves table

    return render(request,'index.html')

def about(request):
    return HttpResponse('this is the about page')

def event(request):
    return HttpResponse('this is the event page')

def community(request):
    return HttpResponse('this is the community page')