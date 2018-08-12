from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    user_list={'a','b00'}
    return render(request,'index.html',{'user_list':user_list})