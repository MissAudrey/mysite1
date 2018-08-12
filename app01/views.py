from django.shortcuts import render,HttpResponse,reverse

# Create your views here.
#
def index(request):
    user_list = ['mary','tom','jessica']
    return render(request,'index.html',{'user_list':user_list})

# def index(request,a1):
#     # print(a1)
#     # p = reverse('n1',args=(2,))
#     p = reverse('n1',kwargs={'a1':222222222})
#     print(p)
#     return HttpResponse('.....')

def login(request):
    return render(request,'login.html')

# def edit(request,a1):
#     print(a1)
#     return HttpResponse('....')


# url(r'^edit/(\w+)/(\w+)/',views.edit)  按位置参数传参
# url(r'^edit/(?P<a1>\w+)/(?P<a2>\w+)/',views.edit) 与views里对应参数对应，
def edit(request,a1,a2): # 如果参数设置为*args,**kargs时，参数类型要保持一致，即上面两种形式
    print(a1,a2)
    return HttpResponse('.....')